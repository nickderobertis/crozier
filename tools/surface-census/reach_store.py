"""The golden-reach store: what each golden test and hand-written fixture executed,
recorded so that it survives a rebuild, and the rule deciding what a change re-runs.

This module is the store's one reader and writer. `golden-reach.py measure` and
`handwritten-fixtures.py measure` write it, `report` reads it back, and the
`census-repin` verb (``tools/surface-census/census-repin.py``) carries it from a
saved base to the tree at ``HEAD``. The base artifact CI publishes
(``golden-reach-base-<sha>``, one ``base.json.gz``) is this store, byte for byte.

The document (``schema`` 1)
---------------------------
The artifact name, its one file, the top-level keys (``TOP_LEVEL``) and the drift
bound (``MAX_AGE_DAYS``, ``MAX_STEPS``) are the contract stated once in
``docs/openapi-surface-coverage.md`` ("Repinning: the store, the base and `just
census-repin`"), which ``reach_store_test.py`` holds these constants to. This
reader refuses any ``schema`` but 1. What the contract leaves to it is below.

**A function key** is ``<file>::<path>``: the repository-relative source file,
then the item path inside it, read off the source — modules by name, an
inherent method as ``Type::name``, a trait impl's method as
``<Type as Trait>::name``, a trait's default method as ``Trait::name``, and a
``fn`` nested in a ``fn`` as ``outer::inner``. Generic parameters are dropped, so
every instantiation of a generic function is one key, and a closure is part of
the ``fn`` item enclosing it (its regions, and its tokens in that item's digest).
Two items of one file with the same path (``#[cfg(windows)]`` and
``#[cfg(not(windows))]`` twins) are told apart by a ``#2``, ``#3`` suffix in
source order. Every file also has the pseudo-function ``<file>::{items}``: the
file's tokens outside every ``fn`` item, attributes of those items included,
which owns any counter region outside a ``fn`` (a ``const`` initializer). Items
under ``#[cfg(test)]`` are not part of either: the measured binaries never
compile them.

``start``/``end`` are the item's 1-indexed first and last line, ``digest`` the
SHA-256 (first 32 hex digits) of its **normalized token stream** — every token
of the item, attributes included, comments and whitespace dropped. Optional final
commas in ordinary lists are dropped for rustfmt reflow; single-element tuple
commas and every comma inside a macro invocation, macro definition or attribute
are retained because those can carry meaning — and
``regions`` the item's counter regions (executed or not: the *universe*), in
the region encoding below, sorted.

**The region encoding.** A region is ``[t0, o0, t1, o1]``: its start and its
(exclusive) end, each a token index into its function's token stream and a byte
offset from that token's first byte — the start from the last token starting at
or before it, the end from the last token starting before it (so an end right
after a token is that token's length, whatever follows it). Because the position is relative to the
item's own tokens, it maps every region exactly onto its line and column in any
later tree where the item's digest is unchanged, through comments, whitespace
and rustfmt reflow inside or above it. llvm-cov reports byte columns; a
boundary that falls inside whitespace (none does in crozier's measured regions
today) is kept as an offset past the token before it, exact while that
whitespace is.

**An entry** is ``{"commit": <40-hex>, "regions": {<function key>: [i, …]}}``:
the commit the test (or fixture) last executed at, and per function it
executed, the indices of its executed regions into that function's
``regions``. The set of keys is the set of functions the run executed. A
fixture entry declaring a generation setting also carries ``"control"``, the
same map for its run without the setting.

The carry rule
--------------
``plan`` decides what a step re-runs; the rule it implements is stated for
readers in the coverage index beside the contract, and ``reach_store_test.py``
proves each of its cases over a real git history.
"""

from __future__ import annotations

import bisect
import contextlib
import datetime
import gzip
import hashlib
import json
import os
import re
import subprocess
import sys
import tomllib
import zlib
from collections.abc import Generator, Iterable, Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import IO, Any, NamedTuple, NoReturn, NotRequired, TypedDict

SCHEMA = 1
ITEMS = "{items}"
DIGEST_HEX = 32
MAX_AGE_DAYS = 7
MAX_STEPS = 20
REPIN = "just census-repin"
SHA = re.compile(r"[0-9a-f]{40}")
DIGEST = re.compile(rf"[0-9a-f]{{{DIGEST_HEX}}}")
# A golden test or hand-written fixture name: it becomes a file name, so no path in it.
NAME = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.-]*")


class StoreError(ValueError):
    """A store that is not schema 1, or not one this module wrote."""


def fail(message: str) -> NoReturn:
    raise SystemExit(f"golden-reach: {message}")


class Token(NamedTuple):
    """One Rust token: byte offsets `[start, end)` into its file, and its text."""

    start: int
    end: int
    text: str


_IDENT = re.compile(r"(?:r#)?[A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*")
_NUMBER = re.compile(r"[0-9][0-9A-Za-z_]*(?:\.[0-9][0-9A-Za-z_]*)?")
_RAW = re.compile(r'(?:b|c)?r(#*)"')
_PREFIXED = re.compile(r'(?:b|c)?"')


def tokenize(source: bytes) -> list[Token]:
    """Every token of a Rust source file, comments and whitespace dropped.

    Strings, raw strings, char and byte literals are one token each (so their
    braces and quotes never desynchronize a scan); punctuation is one token per
    character, which keeps every counter-region boundary on a token boundary.
    Bytes are read as Latin-1, so offsets are byte offsets.
    """
    text = source.decode("latin-1")
    tokens: list[Token] = []
    i, n = 0, len(text)
    while i < n:
        match text[i]:
            case " " | "\t" | "\r" | "\n" | "\f" | "\v":
                i += 1
            case "/" if text.startswith("//", i):
                newline = text.find("\n", i)
                i = n if newline == -1 else newline + 1
            case "/" if text.startswith("/*", i):
                i = _comment_end(text, i)
            case _:
                end = _token_end(text, i)
                tokens.append(Token(i, end, text[i:end]))
                i = end
    return tokens


def _comment_end(text: str, i: int) -> int:
    """Just past the (nested) block comment opening at `i`."""
    depth, i = 1, i + 2
    while i < len(text) and depth:
        if text.startswith("/*", i):
            depth, i = depth + 1, i + 2
        elif text.startswith("*/", i):
            depth, i = depth - 1, i + 2
        else:
            i += 1
    return i


def _token_end(text: str, i: int) -> int:
    """Just past the token starting at `i`: a literal whole, an identifier or number, else one character."""
    n, c = len(text), text[i]
    char = i + (1 if c == "'" else 2)
    match c:
        case _ if (raw := _RAW.match(text, i)) is not None:
            closer = '"' + raw.group(1)
            end = text.find(closer, raw.end())
            return n if end == -1 else end + len(closer)
        case _ if (quoted := _PREFIXED.match(text, i)) is not None:
            j = quoted.end()
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            return min(j + 1, n)
        case "'" | "b" if (c == "'" or text.startswith("b'", i)) and (width := _char_width(text, char)):
            return char + width + 1
        case "'":
            # A lifetime or label: the quote and the identifier after it.
            ident = _IDENT.match(text, i + 1)
            return ident.end() if ident else i + 1
        case _ if (ident := _IDENT.match(text, i)) is not None:
            return ident.end()
        case _ if (number := _NUMBER.match(text, i)) is not None:
            return number.end()
        case _:
            return i + 1


def _char_width(text: str, j: int) -> int:
    """The width of a char literal's body starting at `j` (after its quote), or 0 for a lifetime."""
    if j >= len(text):
        return 0
    if text[j] == "\\":
        close = text.find("'", j + 2)
        return close - j if close != -1 and close - j <= 12 else 0
    lead = ord(text[j])
    width = 1 if lead < 0x80 else 2 if lead < 0xE0 else 3 if lead < 0xF0 else 4
    return width if text.startswith("'", j + width) else 0


def _matches(tokens: list[Token]) -> dict[int, int]:
    """Opening bracket index -> its closing index, for `()`, `[]` and `{}`."""
    stack: list[int] = []
    out: dict[int, int] = {}
    for index, token in enumerate(tokens):
        match token.text:
            case "(" | "[" | "{":
                stack.append(index)
            case ")" | "]" | "}" if stack:
                out[stack.pop()] = index
    return out


@dataclass
class Unit:
    """One `fn` item: its token span (attributes from `first`, the item proper from `item`)."""

    key: str
    first: int
    item: int
    last: int
    const_fn: bool
    trait_ctx: bool
    golden_name: str = ""


@dataclass
class Item:
    """One item at module, impl or trait level (the e2e suite's attribution reads these)."""

    key: str
    kind: str
    first: int
    last: int
    attributes: tuple[str, ...]


@dataclass
class ParsedFile:
    """A source file's tokens, its `fn` units, its other items and its test-only spans."""

    path: str
    source: bytes
    tokens: list[Token]
    units: list[Unit]
    items: list[Item]
    test_spans: list[tuple[int, int]]
    test_modules: list[str]
    line_starts: list[int] = field(default_factory=list)

    def position(self, offset: int) -> tuple[int, int]:
        """A byte offset as llvm-cov's 1-based `(line, column)`."""
        line = bisect.bisect_right(self.line_starts, offset)
        return line, offset - self.line_starts[line - 1] + 1

    def offset(self, line: int, column: int) -> int:
        return self.line_starts[line - 1] + column - 1


_QUALIFIERS = {"pub", "const", "async", "unsafe", "extern", "default", "safe"}
_ITEM_KEYWORDS = {"fn", "mod", "impl", "trait", "struct", "enum", "union", "type", "const", "static", "use"}


def _is_cfg_test(tokens: list[Token], lo: int, hi: int) -> bool:
    return [t.text for t in tokens[lo:hi]] == ["cfg", "(", "test", ")"]


def parse(path: str, source: bytes) -> ParsedFile:
    """Every `fn` unit and item of one Rust source file, keyed as the module docstring says."""
    tokens = tokenize(source)
    match = _matches(tokens)
    units: list[Unit] = []
    items: list[Item] = []
    test_spans: list[tuple[int, int]] = []
    test_modules: list[str] = []
    _scan_items(tokens, match, 0, len(tokens), [], False, units, items, test_spans, test_modules)
    seen: dict[str, int] = {}
    for unit in units:
        seen[unit.key] = seen.get(unit.key, 0) + 1
        if seen[unit.key] > 1:
            unit.key = f"{unit.key}#{seen[unit.key]}"
    starts = [0] + [index + 1 for index, byte in enumerate(source) if byte == 0x0A]
    return ParsedFile(path, source, tokens, units, items, test_spans, test_modules, starts)


def _attributes(tokens: list[Token], match: dict[int, int], i: int, hi: int) -> tuple[int, bool, list[str]]:
    """Skip the outer attributes at `i`; return where the item starts, whether one is `cfg(test)`, and their texts."""
    test = False
    texts: list[str] = []
    while i < hi and tokens[i].text == "#":
        j = i + 1
        if j < hi and tokens[j].text == "!":
            j += 1
        if j < hi and tokens[j].text == "[" and j in match:
            close = match[j]
            test = test or _is_cfg_test(tokens, j + 1, close)
            texts.append("".join(t.text for t in tokens[j + 1 : close]))
            i = close + 1
        else:
            break
    return i, test, texts


def _item_end(tokens: list[Token], match: dict[int, int], i: int, hi: int, kind: str) -> int:
    """The last token index of the item whose keyword is at `i`."""
    statement = kind in {"const", "static", "use", "type", "crate", "let"}
    j = i
    while j < hi:
        text = tokens[j].text
        if text == ";":
            return j
        if text in ("(", "[") and j in match:
            j = match[j] + 1
            continue
        if text == "{" and j in match:
            if statement:
                j = match[j] + 1
                continue
            return match[j]
        j += 1
    return hi - 1


def _type_name(tokens: list[Token], lo: int, hi: int) -> str:
    """The last path segment's identifier of a type in `tokens[lo:hi]`, generics dropped."""
    depth, name = 0, ""
    for index in range(lo, hi):
        text = tokens[index].text
        match text:
            case "<":
                depth += 1
            # The `>` of a `->` closes nothing.
            case ">" if not (index and tokens[index - 1].text == "-"):
                depth -= 1
            case "dyn" | "mut" | "const" | "for" | "where" | "impl":
                pass
            case _ if depth == 0 and _IDENT.fullmatch(text):
                name = text
    return name.removeprefix("r#") or "_"


def _scan_items(
    tokens: list[Token],
    match: dict[int, int],
    lo: int,
    hi: int,
    path: list[str],
    trait_ctx: bool,
    units: list[Unit],
    items: list[Item],
    test_spans: list[tuple[int, int]],
    test_modules: list[str],
) -> None:
    i = lo
    while i < hi:
        first = i
        i, test, attributes = _attributes(tokens, match, i, hi)
        if i >= hi:
            break
        if tokens[i].text == ";":
            i += 1
            continue
        start = i
        while i < hi and (tokens[i].text in _QUALIFIERS or (tokens[i].text.startswith('"') and i > start)):
            if tokens[i].text == "pub" and i + 1 < hi and tokens[i + 1].text == "(" and i + 1 in match:
                i = match[i + 1] + 1
                continue
            if tokens[i].text == "const" and i + 1 < hi and tokens[i + 1].text not in _QUALIFIERS | {"fn"}:
                break
            if tokens[i].text == "default" and i + 1 < hi and tokens[i + 1].text not in _QUALIFIERS | {"fn", "type"}:
                break
            i += 1
        if i >= hi:
            break
        keyword = tokens[i].text
        # A macro invocation or `macro_rules!` at item level: one opaque item.
        if i + 1 < hi and tokens[i + 1].text == "!" and keyword not in _ITEM_KEYWORDS:
            j = i + 2
            if j < hi and _IDENT.fullmatch(tokens[j].text):
                j += 1
            end = match.get(j, j) if j < hi else hi - 1
            if end + 1 < hi and tokens[end + 1].text == ";":
                end += 1
            label = f"macro_rules! {tokens[i + 2].text}" if keyword == "macro_rules" and i + 2 < hi else f"{keyword}!"
            items.append(Item("::".join([*path, label]), "macro", first, end, tuple(attributes)))
            if test:
                test_spans.append((first, end))
            i = end + 1
            continue
        if keyword == "extern" and i + 1 < hi and tokens[i + 1].text == "crate":
            keyword = "crate"
        end = _item_end(tokens, match, i, hi, keyword)
        name = tokens[i + 1].text.removeprefix("r#") if i + 1 < hi else ""
        if test:
            test_spans.append((first, end))
            if keyword == "mod" and tokens[end].text == ";":
                test_modules.append(name)
            i = end + 1
            continue
        match keyword:
            case "fn" if _IDENT.fullmatch(name):
                body = _fn_body(tokens, match, i, end + 1)
                const_fn = any(t.text == "const" for t in tokens[start:i])
                key = "::".join([*path, name])
                items.append(Item(key, "fn", first, end, tuple(attributes)))
                if body is not None:
                    units.append(Unit(key, first, start, end, const_fn, trait_ctx))
                    _scan_nested(tokens, match, body + 1, end, [*path, name], units)
            case "mod" if tokens[end].text == "}":
                items.append(Item("::".join([*path, name]), "mod", first, end, tuple(attributes)))
                opening = _first_brace(tokens, i, end)
                _scan_items(
                    tokens, match, opening + 1, end, [*path, name], False, units, items, test_spans, test_modules
                )
            case "impl" | "trait" if tokens[end].text == "}":
                opening = _first_brace(tokens, i, end)
                if keyword == "trait":
                    owner, inside_trait = name, True
                else:
                    header = list(range(i + 1, opening))
                    at_for = next(
                        (k for k in header if tokens[k].text == "for" and _depth(tokens, i + 1, k) == 0),
                        None,
                    )
                    where = next((k for k in header if tokens[k].text == "where"), opening)
                    if at_for is not None:
                        trait = _type_name(tokens, i + 1, at_for)
                        owner, inside_trait = f"<{_type_name(tokens, at_for + 1, where)} as {trait}>", True
                    else:
                        owner, inside_trait = _type_name(tokens, i + 1, where), False
                items.append(Item("::".join([*path, f"{keyword} {owner}"]), keyword, first, end, tuple(attributes)))
                _scan_items(
                    tokens,
                    match,
                    opening + 1,
                    end,
                    [*path, owner],
                    inside_trait,
                    units,
                    items,
                    test_spans,
                    test_modules,
                )
            case _:
                label = name if _IDENT.fullmatch(name) else keyword
                items.append(Item("::".join([*path, f"{keyword} {label}"]), keyword, first, end, tuple(attributes)))
        i = end + 1


def _depth(tokens: list[Token], lo: int, hi: int) -> int:
    depth = 0
    for index in range(lo, hi):
        match tokens[index].text:
            case "<":
                depth += 1
            # The `>` of a `->` closes nothing.
            case ">" if tokens[index - 1].text != "-":
                depth -= 1
    return depth


def _first_brace(tokens: list[Token], lo: int, hi: int) -> int:
    return next(k for k in range(lo, hi + 1) if tokens[k].text == "{")


def _fn_body(tokens: list[Token], match: dict[int, int], i: int, hi: int) -> int | None:
    """The `{` opening the body of the `fn` at `i`, or None for a declaration."""
    j = i + 2
    while j < hi:
        text = tokens[j].text
        if text == ";":
            return None
        if text in ("(", "[") and j in match:
            j = match[j] + 1
            continue
        if text == "{":
            return j
        j += 1
    return None


def _scan_nested(tokens: list[Token], match: dict[int, int], lo: int, hi: int, path: list[str], units: list[Unit]):
    """Every `fn` item nested inside a function body, as `outer::inner`."""
    j = lo
    while j < hi:
        if tokens[j].text == "fn" and j + 1 < hi and _IDENT.fullmatch(tokens[j + 1].text):
            body = _fn_body(tokens, match, j, hi)
            if body is None or body not in match:
                j += 1
                continue
            start = j
            while start > lo and tokens[start - 1].text in _QUALIFIERS:
                start -= 1
            first = start
            while first > lo and tokens[first - 1].text == "]":
                opening = next((k for k, v in match.items() if v == first - 1), None)
                if opening is None or opening - 1 < lo or tokens[opening - 1].text != "#":
                    break
                first = opening - 1
            end = match[body]
            name = tokens[j + 1].text.removeprefix("r#")
            const_fn = any(t.text == "const" for t in tokens[start:j])
            units.append(Unit("::".join([*path, name]), first, start, end, const_fn, False))
            _scan_nested(tokens, match, body + 1, end, [*path, name], units)
            j = end + 1
            continue
        j += 1


def _digest(texts: Iterable[str]) -> str:
    joined = "\x1f".join(texts).encode("latin-1")
    return hashlib.sha256(joined).hexdigest()[:DIGEST_HEX]


@dataclass
class Function:
    """One function key of a tree: where its tokens are, and their digest."""

    key: str
    file: ParsedFile
    indices: list[int]  # token indices into `file.tokens`, in order
    digest: str
    start: int
    end: int
    const_fn: bool = False
    trait_ctx: bool = False
    _starts: list[int] = field(default_factory=list)

    def encode(self, offset: int, *, end: bool = False) -> list[int]:
        """A byte offset as `[token index, offset from that token's start]` within this function.

        A start counts from the last token starting at or before it; an (exclusive)
        end from the last token starting before it, so an end right after a token is
        that token's length whatever follows it — a bracket at once, or a trailing
        comma and a newline after a reflow.
        """
        if not self._starts:
            self._starts = [self.file.tokens[k].start for k in self.indices]
        k = max((bisect.bisect_left if end else bisect.bisect_right)(self._starts, offset) - 1, 0)
        return [k, offset - self._starts[k]]

    def decode(self, position: list[int]) -> int:
        if not self._starts:
            self._starts = [self.file.tokens[k].start for k in self.indices]
        if not 0 <= position[0] < len(self._starts):
            raise StoreError(f"{self.key}: token index {position[0]} is outside its {len(self._starts)} tokens")
        offset = self._starts[position[0]] + position[1]
        if offset > len(self.file.source):
            raise StoreError(f"{self.key}: offset {position} lands past the end of {self.file.path}")
        if not self._starts[0] <= offset <= self.file.tokens[self.indices[-1]].end:
            raise StoreError(f"{self.key}: offset {position} lands outside its function")
        return offset


@dataclass
class Tree:
    """The measured crate's sources at one tree: every function key, and how to place a region."""

    root: Path
    functions: dict[str, Function]
    files: dict[str, ParsedFile]
    _spans: dict[str, list[tuple[int, int, Function]]] = field(default_factory=dict)
    _starts: dict[str, list[int]] = field(default_factory=dict)

    def owner(self, file: str, offset: int) -> Function | None:
        """The innermost `fn` item holding `offset`, else the file's `{items}` pseudo-function.

        Items nest or are disjoint, so walking back from the last item starting at
        or before `offset`, the first that still holds it is the innermost.
        """
        spans = self._spans.get(file)
        if spans is None:
            parsed = self.files.get(file)
            if parsed is None:
                return None
            spans = []
            for function in self.functions.values():
                if function.file is parsed and not function.key.endswith(f"::{ITEMS}"):
                    lo = parsed.tokens[function.indices[0]].start
                    hi = parsed.tokens[function.indices[-1]].end
                    spans.append((lo, hi, function))
            spans.sort(key=lambda span: (span[0], -span[1]))
            self._spans[file] = spans
            self._starts[file] = [span[0] for span in spans]
        index = bisect.bisect_right(self._starts[file], offset) - 1
        while index >= 0:
            lo, hi, function = spans[index]
            if offset < hi:
                return function
            index -= 1
        return self.functions.get(f"{file}::{ITEMS}")

    def encode(self, file: str, region: Iterable[int]) -> tuple[str, list[int]] | None:
        """`(function key, [t0, o0, t1, o1])` for an llvm-cov `[line, col, line, col]` region of `file`."""
        line0, col0, line1, col1 = region
        parsed = self.files.get(file)
        if parsed is None:
            return None
        start, end = parsed.offset(line0, col0), parsed.offset(line1, col1)
        function = self.owner(file, start)
        if function is None:
            return None
        return function.key, function.encode(start) + function.encode(end, end=True)

    def decode(self, key: str, encoded: list[int]) -> tuple[str, tuple[int, int, int, int]]:
        function = self.functions.get(key)
        if function is None:
            raise StoreError(f"function {key} is not in this tree")
        parsed = function.file
        start, end = function.decode(encoded[:2]), function.decode(encoded[2:])
        if start > end:
            raise StoreError(f"{key}: decoded region {encoded} starts after its end")
        line0, col0 = parsed.position(start)
        line1, col1 = parsed.position(end)
        return parsed.path, (line0, col0, line1, col1)

    def table(self) -> dict[str, FunctionRecord]:
        """Every function's record at this tree, its counter regions not yet known (empty)."""
        return {
            key: {
                "file": function.file.path,
                "start": function.start,
                "end": function.end,
                "digest": function.digest,
                "regions": [],
            }
            for key, function in sorted(self.functions.items())
        }


def _module_file(directory: Path, base: Path, name: str) -> list[Path]:
    return [directory / f"{name}.rs", directory / name / "mod.rs", base / name / f"{name}.rs"]


# These words introduce a grouped expression or pattern, rather than a call's
# argument list. `fn(T,)`, `Fn(T,)`, constructors and ordinary calls are lists.
_GROUP_BEFORE_PAREN = frozenset(
    {
        "return",
        "break",
        "yield",
        "if",
        "while",
        "match",
        "for",
        "in",
        "let",
        "else",
        "loop",
        "async",
        "move",
        "unsafe",
        "const",
        "static",
        "type",
        "where",
        "as",
        "impl",
        "trait",
        "struct",
        "enum",
        "mod",
        "use",
        "pub",
        "mut",
        "ref",
        "dyn",
        "await",
    }
)


def _formatting_commas(tokens: list[Token]) -> list[bool]:
    """Commas rustfmt may add to ordinary lists, never punctuation a macro can inspect.

    A singleton tuple's comma is its type/value/pattern constructor. In a call
    or parameter list a final comma is optional; in other parentheses it is
    optional only when another top-level comma already makes a tuple. Angle
    pairs and closure parameter pipes are skipped while counting, so commas
    inside either cannot turn a singleton tuple into an apparent multi-element
    tuple. A comparison or bitwise expression mistaken for a delimiter pair
    only preserves an extra comma (a conservative re-run).
    """
    pairs = _matches(tokens)
    opened = {end: start for start, end in pairs.items()}
    protected = [False] * len(tokens)

    def protect(start: int) -> None:
        if start in pairs:
            for index in range(start, pairs[start] + 1):
                protected[index] = True

    for index, token in enumerate(tokens):
        match token.text:
            case "#":
                start = index + 1
                if start < len(tokens) and tokens[start].text == "!":
                    start += 1
                if start < len(tokens) and tokens[start].text == "[":
                    protect(start)
            case "!" if index and index + 1 in pairs:
                previous = tokens[index - 1].text
                raw = index >= 3 and [t.text for t in tokens[index - 3 : index - 1]] == ["r", "#"]
                if _IDENT.fullmatch(previous) and (previous not in _GROUP_BEFORE_PAREN or raw):
                    protect(index + 1)
            case "macro_rules" if index + 1 < len(tokens) and tokens[index + 1].text == "!":
                # The name can be a raw identifier (`r#name`), too.
                for start in range(index + 2, min(index + 6, len(tokens))):
                    if start in pairs:
                        protect(start)
                        break

    def multiple_tuple_elements(start: int, end: int) -> bool:
        top, index = [], start + 1
        while index < end:
            if index in pairs:
                index = pairs[index] + 1
            else:
                top.append(index)
                index += 1
        angles, angle_pairs = [], {}
        pipe, pipe_pairs = None, {}
        for index in top:
            if tokens[index].text == "|":
                if pipe is None:
                    pipe = index
                else:
                    pipe_pairs[pipe] = index
                    pipe = None
            if tokens[index].text == "<":
                angles.append(index)
            elif tokens[index].text == ">" and angles and (not index or tokens[index - 1].text not in ("-", "=")):
                angle_pairs[angles.pop()] = index
        commas, skip = 0, -1
        for index in top:
            if index <= skip:
                continue
            if index in angle_pairs:
                skip = angle_pairs[index]
            elif index in pipe_pairs:
                skip = pipe_pairs[index]
            elif tokens[index].text == ",":
                commas += 1
        return commas > 1

    excluded = [False] * len(tokens)
    for index, token in enumerate(tokens[:-1]):
        closer = tokens[index + 1].text
        if token.text != "," or protected[index] or closer not in (")", "]", "}", ">"):
            continue
        if closer == ")":
            start = opened.get(index + 1)
            if start is None:
                continue
            previous = tokens[start - 1].text if start else ""
            raw = start >= 3 and [t.text for t in tokens[start - 3 : start - 1]] == ["r", "#"]
            call = (
                (bool(_IDENT.fullmatch(previous)) and (previous not in _GROUP_BEFORE_PAREN or raw))
                or previous in (")", "]")
                or (previous == ">" and start >= 2 and tokens[start - 2].text != "-")
            )
            if not call and not multiple_tuple_elements(start, index + 1):
                continue
        excluded[index] = True
    return excluded


def read_tree(root: Path, sources: Mapping[str, bytes] | None = None) -> Tree:
    """Parse every `src/**/*.rs` of the tree at `root` (or of `sources`, `path -> bytes`).

    A file only a `#[cfg(test)] mod name;` declares is test-only and not measured.
    """
    if sources is None:
        sources = {
            path.relative_to(root).as_posix(): path.read_bytes()
            for path in sorted((root / "src").rglob("*.rs"))
            if path.is_file()
        }
    parsed = {path: parse(path, data) for path, data in sorted(sources.items())}
    test_only: set[str] = set()
    for path, file in parsed.items():
        here = Path(path)
        directory = here.parent if here.name in ("mod.rs", "lib.rs", "main.rs") else here.parent / here.stem
        for name in file.test_modules:
            for candidate in _module_file(directory, here.parent, name):
                test_only.add(candidate.as_posix())
    functions: dict[str, Function] = {}
    files: dict[str, ParsedFile] = {}
    for path, file in parsed.items():
        if path in test_only:
            continue
        files[path] = file
        excluded = _formatting_commas(file.tokens)
        inside = [False] * len(file.tokens)
        tested = [False] * len(file.tokens)
        for lo, hi in file.test_spans:
            for k in range(lo, hi + 1):
                tested[k] = True
        for unit in file.units:
            if tested[unit.item]:
                continue
            indices = [k for k in range(unit.first, unit.last + 1) if not excluded[k]]
            key = f"{path}::{unit.key}"
            functions[key] = Function(
                key,
                file,
                indices,
                _digest(file.tokens[k].text for k in indices),
                file.position(file.tokens[unit.first].start)[0],
                file.position(file.tokens[unit.last].start)[0],
                unit.const_fn,
                unit.trait_ctx,
            )
            for k in range(unit.item, unit.last + 1):
                inside[k] = True
        rest = [k for k in range(len(file.tokens)) if not inside[k] and not excluded[k] and not tested[k]]
        last_line = file.position(max(len(file.source) - 1, 0))[0]
        functions[f"{path}::{ITEMS}"] = Function(
            f"{path}::{ITEMS}",
            file,
            rest,
            _digest(file.tokens[k].text for k in rest),
            1,
            last_line,
        )
    return Tree(root, functions, files)


class FunctionRecord(TypedDict):
    """One `functions` value: where the item is in its tree, its token digest, its counter regions."""

    file: str
    start: int
    end: int
    digest: str
    regions: list[list[int]]


class Entry(TypedDict):
    """One `tests` or `fixtures` value: the commit it last ran at, and per function its executed regions."""

    commit: str
    regions: dict[str, list[int]]
    control: NotRequired[dict[str, list[int]]]


class Store(TypedDict):
    """A schema-1 store, its keys exactly `TOP_LEVEL`."""

    schema: int
    commit: str
    rustc: str
    llvm: str
    full_at: str
    steps_since_full: int
    measured_at: str
    tests: dict[str, Entry]
    fixtures: dict[str, Entry]
    functions: dict[str, FunctionRecord]


# The schema-1 keys, in the order the contract lists them: the model's own fields.
TOP_LEVEL = tuple(Store.__annotations__)


def _valid_regions(value: Any) -> bool:
    """Token-relative regions: four whole numbers each, the start not after the end.

    Whether a token index lies inside its function is known only against a tree,
    so `Tree.decode` refuses one that does not.
    """
    return isinstance(value, list) and all(
        isinstance(r, list)
        and len(r) == 4
        and all(type(n) is int and n >= 0 for n in r)
        and (r[0], r[1]) <= (r[2], r[3])
        for r in value
    )


def _valid_entry(value: Any, functions: Mapping[str, Any]) -> bool:
    if not isinstance(value, dict) or not isinstance(value.get("commit"), str) or not SHA.fullmatch(value["commit"]):
        return False
    for name in ("regions", "control"):
        if name == "control" and name not in value:
            continue
        executed = value.get(name)
        if not isinstance(executed, dict):
            return False
        for key, indices in executed.items():
            universe = functions.get(key, {}).get("regions")
            if (
                universe is None
                or not isinstance(indices, list)
                or not all(type(i) is int and 0 <= i < len(universe) for i in indices)
            ):
                return False
    return True


def validate(store: Any, where: str) -> Store:
    """`store` if it is a schema-1 store, else a `StoreError` naming what is wrong."""
    if not isinstance(store, dict):
        raise StoreError(f"{where} is not a JSON object")
    if type(store.get("schema")) is not int or store["schema"] != SCHEMA:
        raise StoreError(f"{where} is schema {store.get('schema')!r}; this reader reads schema {SCHEMA} only")
    if set(store) != set(TOP_LEVEL):
        raise StoreError(f"{where} carries the keys {sorted(store)}, not exactly {list(TOP_LEVEL)}")
    for name in ("commit", "full_at"):
        if not isinstance(store[name], str) or not SHA.fullmatch(store[name]):
            raise StoreError(f"{where}'s `{name}` is not a 40-hex commit")
    if type(store["steps_since_full"]) is not int or store["steps_since_full"] < 0:
        raise StoreError(f"{where}'s `steps_since_full` is not a whole number")
    if not all(isinstance(store[name], str) and store[name] for name in ("rustc", "llvm", "measured_at")):
        raise StoreError(f"{where}'s `rustc`, `llvm` and `measured_at` must be non-empty strings")
    try:
        measured_at(store)
    except ValueError as error:
        raise StoreError(f"{where}'s `measured_at` is not ISO 8601 ({error})") from error
    functions = store["functions"]
    if not isinstance(functions, dict) or not all(
        isinstance(key, str)
        and isinstance(value, dict)
        and isinstance(value.get("file"), str)
        and key.startswith(f"{value['file']}::")
        and type(value.get("start")) is int
        and type(value.get("end")) is int
        and 1 <= value["start"] <= value["end"]
        and isinstance(value.get("digest"), str)
        and DIGEST.fullmatch(value["digest"]) is not None
        and _valid_regions(value.get("regions"))
        for key, value in functions.items()
    ):
        raise StoreError(
            f"{where}'s `functions` is not a map of `<file>::<path>` -> its file, a 1-based start <= end, "
            f"a {DIGEST_HEX}-hex digest and token-relative regions"
        )
    for name in ("tests", "fixtures"):
        entries = store[name]
        if not isinstance(entries, dict) or not all(NAME.fullmatch(key) for key in entries):
            raise StoreError(f"{where}'s `{name}` names an entry that is not a plain test or fixture name")
        if not all(_valid_entry(e, functions) for e in entries.values()):
            raise StoreError(f"{where}'s `{name}` holds an entry that is not a commit and executed-region indices")
    return store


def measured_at(store: Mapping[str, object]) -> datetime.datetime:
    stamp = datetime.datetime.fromisoformat(str(store["measured_at"]).replace("Z", "+00:00"))
    return stamp if stamp.tzinfo else stamp.replace(tzinfo=datetime.UTC)


def load(path: Path) -> Store:
    """Read a store (gzip JSON) and validate it, or raise `StoreError`."""
    try:
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError, EOFError, zlib.error) as error:
        raise StoreError(f"{path} is not a gzip-compressed JSON store ({error})") from error
    return validate(data, str(path))


def save(store: Store, path: Path) -> None:
    """Write `store` to `path` atomically, gzip-compressed and byte-stable for one content."""
    validate(store, "the store being written")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    payload = json.dumps(store, sort_keys=True, separators=(",", ":")).encode("utf-8")
    with temporary.open("wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, filename="") as handle:
        handle.write(payload)
    os.replace(temporary, path)


def toolchain(root: Path) -> tuple[str, str]:
    """Opaque identities from `rustc -vV`: release/hash/host, and its bundled LLVM version."""
    run = subprocess.run(["rustc", "-vV"], cwd=root, capture_output=True, text=True)
    if run.returncode != 0:
        fail(f"`rustc -vV` exited {run.returncode}: {run.stderr.strip()[-300:]}; install the pinned toolchain")
    fields = dict(line.split(": ", 1) for line in run.stdout.splitlines() if ": " in line)
    missing = [
        name
        for name in ("release", "commit-hash", "LLVM version", "host")
        if not fields.get(name, "").strip() or fields[name] in ("?", "unknown")
    ]
    if missing:
        fail(f"`rustc -vV` omitted a usable {', '.join(missing)}; install the pinned toolchain before measuring")
    return f"{fields['release']} {fields['commit-hash']} {fields['host']}", fields["LLVM version"]


def now_iso() -> str:
    return datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def universe_table(tree: Tree, universe: Mapping[str, Iterable[Iterable[int]]]) -> dict[str, FunctionRecord]:
    """The store's `functions` for `tree`, each with its counter regions from an llvm-cov universe."""
    table = tree.table()
    regions: dict[str, set[tuple[int, ...]]] = {key: set() for key in table}
    for file, spans in universe.items():
        for span in spans:
            placed = tree.encode(file, span)
            if placed is not None:
                regions.setdefault(placed[0], set()).add(tuple(placed[1]))
    for key, value in table.items():
        value["regions"] = [list(r) for r in sorted(regions.get(key, ()))]
    return table


def entry_regions(
    tree: Tree, functions: Mapping[str, FunctionRecord], hit: Mapping[str, Iterable[Iterable[int]]]
) -> dict[str, list[int]]:
    """An entry's `regions` map: per function, the indices of `hit`'s regions in `functions`."""
    index = {key: {tuple(r): i for i, r in enumerate(value["regions"])} for key, value in functions.items()}
    out: dict[str, set[int]] = {}
    for file, spans in hit.items():
        for span in spans:
            placed = tree.encode(file, span)
            if placed is None:
                continue
            position = index.get(placed[0], {}).get(tuple(placed[1]))
            if position is None:
                fail(
                    f"an executed region of {file} {list(span)} is not one of {placed[0]}'s counter regions; "
                    f"the export and the build disagree — re-run `{REPIN}`"
                )
            out.setdefault(placed[0], set()).add(position)
    return {key: sorted(indices) for key, indices in sorted(out.items())}


def remap(
    entry_map: Mapping[str, list[int]], old: Mapping[str, FunctionRecord], new: Mapping[str, FunctionRecord]
) -> dict[str, list[int]] | None:
    """Carry an entry's indices from `old`'s universe to `new`'s; None when a region is gone."""
    out: dict[str, list[int]] = {}
    for key, indices in entry_map.items():
        if key not in new:
            return None
        where = {tuple(r): i for i, r in enumerate(new[key]["regions"])}
        moved = []
        for i in indices:
            position = where.get(tuple(old[key]["regions"][i]))
            if position is None:
                return None
            moved.append(position)
        out[key] = sorted(moved)
    return out


def positions(
    tree: Tree, functions: Mapping[str, FunctionRecord], indices: Mapping[str, list[int]] | None = None
) -> dict[str, set[tuple[int, int, int, int]]]:
    """Absolute llvm-cov regions per file: the universe, or one entry's executed set."""
    out: dict[str, set[tuple[int, int, int, int]]] = {}
    for key, value in functions.items():
        chosen = value["regions"] if indices is None else [value["regions"][i] for i in indices.get(key, ())]
        for encoded in chosen:
            file, region = tree.decode(key, encoded)
            out.setdefault(file, set()).add(region)
    return out


def stale_functions(tree: Tree, functions: Mapping[str, FunctionRecord]) -> list[str]:
    """The keys whose digest in `functions` differs from `tree` (or that only one side has)."""
    here = {key: function.digest for key, function in tree.functions.items()}
    there = {key: value["digest"] for key, value in functions.items()}
    return sorted(key for key in here.keys() | there.keys() if here.get(key) != there.get(key))


# Paths whose change no function digest can attribute: every test re-runs.
NON_ATTRIBUTABLE = (
    re.compile(r"templates/.*"),
    re.compile(r"assets/.*"),
    re.compile(r"rust-toolchain(\.toml)?"),
    re.compile(r"build\.rs"),
    re.compile(r"\.cargo/config(\.toml)?"),
    re.compile(r"src/(?!.*(?:\.rs|\.md|/project\.json)$).*"),
    re.compile(r"tools/corpus/corpus_sources\.py"),
    re.compile(r"tools/corpus/corpus_remote_ref_pins\.py"),
    re.compile(r"crates/crozier-e2e/Cargo\.toml"),
)
FIXTURES = "tests/fixtures/"
CORPUS_SOURCES = "tests/fixtures/corpus-sources/"
ROW_KEYED = (
    "tests/fixtures/corpus-sources.tsv",
    "tests/fixtures/corpus-aliases.tsv",
    "tests/fixtures/corpus-remote-ref-pins.tsv",
)
# What a hand-written fixture's run reads: its document, and its setting.
FIXTURE_INPUTS = ("openapi.yml", "evidence.toml")
E2E = "crates/crozier-e2e/tests/"
HANDWRITTEN = "docs/openapi-surface/handwritten/"


class Plan(NamedTuple):
    """What a step does: a full measurement (with its reason), or which tests and fixtures re-run."""

    full: str | None
    tests: frozenset[str]
    fixtures: frozenset[str]
    changed: tuple[str, ...]
    reasons: Mapping[str, str]


def git(root: Path, *args: str, check: bool = True) -> str:
    run = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    if check and run.returncode != 0:
        fail(f"`git {' '.join(args)}` exited {run.returncode}: {run.stderr.strip()[-300:]}")
    return run.stdout


def changed_paths(root: Path, base: str, head: str = "HEAD") -> list[str]:
    return sorted(line for line in git(root, "diff", "--name-only", "--no-renames", base, head).splitlines() if line)


def show(root: Path, commit: str, path: str) -> bytes | None:
    run = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=root, capture_output=True)
    return run.stdout if run.returncode == 0 else None


def release_only(root: Path, base: str, path: str) -> bool:
    """Whether `path` (Cargo.toml or Cargo.lock) differs from `base` only in crozier's own version."""
    old, new = show(root, base, path), (root / path).read_bytes() if (root / path).is_file() else None
    if old is None or new is None:
        return False
    try:
        before, after = tomllib.loads(old.decode("utf-8")), tomllib.loads(new.decode("utf-8"))
    except (tomllib.TOMLDecodeError, UnicodeDecodeError):
        return False
    for document in (before, after):
        package = document.get("package")
        if isinstance(package, dict) and package.get("name") == "crozier":
            package.pop("version", None)
        if isinstance(package, list):
            for entry in package:
                if isinstance(entry, dict) and entry.get("name") == "crozier":
                    entry.pop("version", None)
    return before == after


def _row_keys(root: Path, base: str, path: str) -> set[str] | None:
    """The first-column keys of the rows a row-keyed TSV gained or lost since `base`."""
    old = show(root, base, path)
    new = (root / path).read_bytes() if (root / path).is_file() else b""
    if old is None:
        return None
    before = set(old.decode("utf-8", "replace").splitlines())
    after = set(new.decode("utf-8", "replace").splitlines())
    keys = set()
    for line in before ^ after:
        if line.strip() and not line.startswith("#"):
            keys |= {cell.strip() for cell in line.split("\t")[:2] if cell.strip()}
    return keys


E2E_ROOT = "crates/crozier-e2e/tests"
# Identifiers so common that following them would make every item reachable.
_PATH_WORDS = frozenset({"crate", "super", "self", "Self", "std", "core", "alloc"})


def _item_name(item: Item) -> str:
    """The identifier code refers to an item by: its own name, an impl's type, a macro's name."""
    last = item.key.rsplit("::", 1)[-1]
    match item.kind:
        case "impl" | "trait":
            owner = last.split(" ", 1)[1] if " " in last else last
            return owner.removeprefix("<").split(" as ", 1)[0].rstrip(">")
        case "macro":
            return last.removeprefix("macro_rules! ").rstrip("!")
        case _:
            return last.split(" ", 1)[-1]


class _Suite(NamedTuple):
    """Every item of the e2e suite at one tree, and which of them its golden tests can reach."""

    items: dict[str, dict[str, tuple[Item, str]]]  # path -> item key -> (item, digest)
    reachable: frozenset[tuple[str, str]]  # (path, item key)
    strings: frozenset[str]  # string literals the reachable items carry


_CLOSURE_OPENERS = frozenset({"(", ",", "=", "move", "{", ";", ">", "return", "["})


def _references(tokens: list[Token], lo: int, hi: int) -> set[str]:
    """The identifiers of `tokens[lo:hi + 1]` that can name an item rather than a local.

    A local shadows an item of the same name within its scope: a `let` binding
    from the end of its statement to the end of its enclosing block, a `for`
    binding and a closure's parameters within their bodies, and a function's
    parameters within its body. A use inside such a scope names the local; every
    other identifier is a reference. Pattern bindings in `match` and `if let` are
    not followed, which only over-approximates what the suite reaches.
    """
    span = tokens[lo : hi + 1]
    match = _matches(span)
    enclosing: list[int] = [len(span) - 1] * len(span)
    stack: list[int] = []
    for k, token in enumerate(span):
        match token.text:
            case "{":
                stack.append(match.get(k, len(span) - 1))
            case "}" if stack:
                stack.pop()
        if stack:
            enclosing[k] = stack[-1]
    scopes: dict[str, list[tuple[int, int]]] = {}
    binders: set[int] = set()

    def bind(position: int, start: int, stop: int) -> None:
        name = span[position].text
        if _IDENT.fullmatch(name) and name not in ("mut", "ref", "_") and not name[0].isupper():
            scopes.setdefault(name, []).append((start, stop))
            binders.add(position)

    def statement_end(k: int, closer: str) -> int:
        depth = 0
        for j in range(k + 1, len(span)):
            text = span[j].text
            if depth == 0 and text == closer:
                return j
            if text in "([{":
                depth += 1
            elif text in ")]}":
                depth -= 1
                if depth < 0:
                    return j
        return len(span) - 1

    for k, token in enumerate(span):
        match token.text:
            case "let":
                end = statement_end(k, ";")
                stop = next((j for j in range(k + 1, end) if span[j].text in ("=", ":")), end)
                for j in range(k + 1, stop):
                    bind(j, end, enclosing[k])
            case "for":
                body = statement_end(k, "{")
                stop = next((j for j in range(k + 1, body) if span[j].text == "in"), body)
                for j in range(k + 1, stop):
                    bind(j, body, match.get(body, len(span) - 1))
            case "fn" if k + 1 < len(span) and _IDENT.fullmatch(span[k + 1].text):
                opening = next((j for j in range(k + 2, len(span)) if span[j].text in ("(", "{", ";")), None)
                if opening is None or span[opening].text != "(" or opening not in match:
                    continue
                body = next((j for j in range(match[opening], len(span)) if span[j].text in ("{", ";")), None)
                if body is None or span[body].text != "{":
                    continue
                for j in range(opening + 1, match[opening]):
                    if span[j + 1].text == ":" and span[j + 2].text != ":":
                        bind(j, body, match.get(body, len(span) - 1))
            case "|" if k and span[k - 1].text in _CLOSURE_OPENERS:
                closing = next((j for j in range(k + 1, len(span)) if span[j].text == "|"), None)
                if closing is None:
                    continue
                body = closing + 1
                if body < len(span) and span[body].text == "-":
                    body = next((j for j in range(body, len(span)) if span[j].text == "{"), body)
                stop = match.get(body, statement_end(closing, ","))
                colon = False
                for j in range(k + 1, closing):
                    match span[j].text:
                        case ":":
                            colon = True
                        case ",":
                            colon = False
                        case _ if not colon:
                            bind(j, closing, stop)
    found = set()
    for k, token in enumerate(span):
        if k in binders or not _IDENT.fullmatch(token.text):
            continue
        if any(start <= k <= stop for start, stop in scopes.get(token.text, ())):
            continue
        found.add(token.text)
    return found


def _suite(sources: Mapping[str, bytes], roots: frozenset[str]) -> _Suite:
    """Parse the suite and follow identifiers from its golden tests (see `e2e_attribution`)."""
    parsed: dict[str, tuple[list[Item], list[Token]]] = {}
    for path, data in sources.items():
        file = parse(path, data)
        parsed[path] = (file.items, file.tokens)
    by_name: dict[str, list[tuple[str, Item]]] = {}
    items: dict[str, dict[str, tuple[Item, str]]] = {}
    queue: list[tuple[str, Item]] = []
    for path, (found, tokens) in parsed.items():
        items[path] = {}
        for item in found:
            texts = [t.text for t in tokens[item.first : item.last + 1]]
            items[path][item.key] = (item, _digest(texts))
            name = _item_name(item)
            by_name.setdefault(name, []).append((path, item))
            if name in roots or (item.kind == "macro" and roots & set(texts)):
                queue.append((path, item))
    seen: set[tuple[str, str]] = set()
    names: set[str] = set()
    strings: set[str] = set()
    # What each file's reachable items refer to: a `use` resolves names for its own module only.
    used: dict[str, set[str]] = {}
    while queue:
        path, item = queue.pop()
        if (path, item.key) in seen or item.kind == "use":
            continue
        seen.add((path, item.key))
        tokens = parsed[path][1]
        strings.update(
            t.text for t in tokens[item.first : item.last + 1] if t.text.startswith(('"', 'r"', 'r#"', 'b"'))
        )
        references = _references(tokens, item.first, item.last) - _PATH_WORDS
        used.setdefault(path, set()).update(references)
        for text in references - names:
            names.add(text)
            queue.extend(by_name.get(text, ()))
    for path, (found, tokens) in parsed.items():
        for item in found:
            if item.kind != "use" or path not in used:
                continue
            texts = [t.text for t in tokens[item.first : item.last + 1]]
            leaves = {text for k, text in enumerate(texts) if k + 1 == len(texts) or texts[k + 1] != ":"}
            if "*" in texts or leaves & used[path]:
                seen.add((path, item.key))
    return _Suite(items, frozenset(seen), frozenset(strings))


def e2e_attribution(
    root: Path, base: str, paths: Iterable[str], tests: Iterable[str], constants: Mapping[str, str]
) -> tuple[set[str], str | None]:
    """The golden tests a change to the e2e suite re-runs, or the reason it re-runs every test.

    A golden test's own `fn`, or the `Corpus` literal it drives, re-runs that test.
    Any other changed item re-runs every test only when the golden tests can reach
    it: following identifiers from their functions (and from the macro invocation
    naming them), through every item those identifiers name and every impl block of
    a type they name. A `#[test]` function, or an item no golden test reaches (a
    corpus list another test iterates, a helper of an unrelated journey), re-runs
    nothing. A changed non-Rust file under the suite re-runs every test when a
    string a reachable item carries names it.
    """
    tests = frozenset(tests)
    roots = tests | frozenset(constants)
    files = sorted(p.relative_to(root).as_posix() for p in (root / E2E_ROOT).rglob("*.rs") if p.is_file())
    changed = sorted(set(paths))
    new_sources = {path: (root / path).read_bytes() for path in files}
    old_sources = dict(new_sources)
    for path in changed:
        if not path.endswith(".rs"):
            continue
        old = show(root, base, path)
        if old is None:
            old_sources.pop(path, None)
        else:
            old_sources[path] = old
    after, before = _suite(new_sources, roots), _suite(old_sources, roots)
    rerun: set[str] = set()
    for path in changed:
        if not path.endswith(".rs"):
            leaf = path.rsplit("/", 1)[-1]
            if any(leaf in text for text in after.strings | before.strings):
                return set(), f"{path} changed, and code the golden tests reach names it"
            continue
        old_items, new_items = before.items.get(path, {}), after.items.get(path, {})
        for key in sorted(old_items.keys() | new_items.keys()):
            was, now = old_items.get(key), new_items.get(key)
            if was is not None and now is not None and was[1] == now[1]:
                continue
            entry = now if now is not None else was
            assert entry is not None
            item = entry[0]
            name = _item_name(item)
            if item.kind == "fn" and name in tests:
                rerun.add(name)
                continue
            if item.kind == "const" and name in constants:
                rerun.add(constants[name])
                continue
            if item.kind == "fn" and any(a == "test" or a.startswith("test") for a in item.attributes):
                continue
            if (path, key) in after.reachable or (path, key) in before.reachable:
                return set(), f"{path}: `{key}` changed, and the golden tests reach it"
    return rerun, None


@dataclass(frozen=True)
class Inputs:
    """What one golden test reads besides the crate: its fixture directory and its source names."""

    test: str
    api: str
    names: frozenset[str]


def plan(
    root: Path,
    base: Store,
    tree: Tree,
    tests: Mapping[str, Inputs],
    fixtures: Iterable[str],
    golden_constants: Mapping[str, str],
    versions: tuple[str, str],
    now: datetime.datetime | None = None,
) -> Plan:
    """Which tests and fixtures re-run from `base` to the tree at `root`'s HEAD (see the module docstring)."""
    fixtures = set(fixtures)

    def full(reason: str) -> Plan:
        return Plan(reason, frozenset(tests), frozenset(fixtures), (), {})

    now = now or datetime.datetime.now(datetime.UTC)
    if (base["rustc"], base["llvm"]) != versions:
        return full(
            f"the base was measured with rustc {base['rustc']} and llvm {base['llvm']}, "
            f"this tree builds with rustc {versions[0]} and llvm {versions[1]}"
        )
    age = now - measured_at(base)
    if age > datetime.timedelta(days=MAX_AGE_DAYS):
        return full(f"the base was measured {age.days} days ago, more than {MAX_AGE_DAYS}")
    if base["steps_since_full"] + 1 > MAX_STEPS:
        return full(
            f"a step from the base would be {base['steps_since_full'] + 1} since a full measurement, over {MAX_STEPS}"
        )
    paths = changed_paths(root, base["commit"])
    rerun: dict[str, str] = {}
    rerun_fixtures: dict[str, str] = {}
    by_api: dict[str, list[str]] = {}
    by_name: dict[str, list[str]] = {}
    for inputs in tests.values():
        by_api.setdefault(inputs.api, []).append(inputs.test)
        for name in inputs.names:
            by_name.setdefault(name, []).append(inputs.test)
    for path in paths:
        if path in ("Cargo.toml", "Cargo.lock"):
            if not release_only(root, base["commit"], path):
                return full(f"{path} changed beyond crozier's own version")
            continue
        for pattern in NON_ATTRIBUTABLE:
            if pattern.fullmatch(path):
                return full(f"{path} changed, and no function digest can attribute it")
        if path.startswith(E2E):
            continue
        if path.startswith(CORPUS_SOURCES):
            name = path[len(CORPUS_SOURCES) :].split("/", 1)[0]
            for test in by_name.get(name, []) + by_api.get(name, []):
                rerun.setdefault(test, f"its source document changed ({path})")
        elif path in ROW_KEYED:
            keys = _row_keys(root, base["commit"], path)
            if keys is None:
                return full(f"{path} is new since the base")
            for key in keys:
                for test in by_name.get(key, []) + by_api.get(key, []):
                    rerun.setdefault(test, f"its {Path(path).name} row changed")
        elif path.startswith(FIXTURES) and path.count("/") >= 3:
            api = path[len(FIXTURES) :].split("/", 1)[0]
            for test in by_api.get(api, []):
                rerun.setdefault(test, f"its golden's fixture tree changed ({path})")
        elif path.startswith(HANDWRITTEN) and path.count("/") == 4:
            name, _, leaf = path[len(HANDWRITTEN) :].partition("/")
            if name in fixtures and leaf in FIXTURE_INPUTS:
                rerun_fixtures.setdefault(name, f"its fixture changed ({path})")
    suite = [path for path in paths if path.startswith(E2E)]
    if suite:
        attributed, reason = e2e_attribution(root, base["commit"], suite, tests, golden_constants)
        if reason:
            return full(reason)
        for test in attributed:
            rerun.setdefault(test, "its own e2e test or Corpus literal changed")
    functions = base["functions"]
    changed = stale_functions(tree, functions)
    old_functions: dict[str, Function] = {}
    old_files: set[str] = set()
    for key in changed:
        if key.endswith(f"::{ITEMS}"):
            return full(f"{key.rsplit('::', 1)[0]} changed outside function bodies")
        here, there = tree.functions.get(key), functions.get(key)
        if there is not None and there["file"] not in old_files:
            path = there["file"]
            source = show(root, base["commit"], path)
            if source is None:
                return full(f"the base source for `{key}` is unavailable")
            old_functions.update(read_tree(root, {path: source}).functions)
            old_files.add(path)
        old = old_functions.get(key)
        if (here is not None and here.const_fn) or (old is not None and old.const_fn):
            return full(f"`{key}` is a const fn, evaluated where no counter runs")
        if (here is None or there is None) and (
            " as " in key or (here is not None and here.trait_ctx) or (old is not None and old.trait_ctx)
        ):
            return full(f"`{key}` was added to or removed from a trait or trait impl")
    changed_set = set(changed)
    try:
        for key, record in functions.items():
            if key not in changed_set:
                for region in record["regions"]:
                    tree.decode(key, region)
    except StoreError as error:
        return full(f"the base has unusable counter regions: {error}")
    for name, entry in base["tests"].items():
        if name in tests and name not in rerun:
            hit = sorted(set(entry["regions"]) & changed_set)
            if hit:
                rerun[name] = f"it executed changed {hit[0]}" + (f" and {len(hit) - 1} more" if len(hit) > 1 else "")
    for name in tests:
        if name not in base["tests"]:
            rerun.setdefault(name, "it has no base entry")
    for name, entry in base["fixtures"].items():
        if name in fixtures and name not in rerun_fixtures:
            executed = set(entry["regions"]) | set(entry.get("control", {}))
            hit = sorted(executed & changed_set)
            if hit:
                rerun_fixtures[name] = f"it executed changed {hit[0]}"
    for name in fixtures:
        if name not in base["fixtures"]:
            rerun_fixtures.setdefault(name, "it has no base entry")
    reasons = {**{f"test {k}": v for k, v in rerun.items()}, **{f"fixture {k}": v for k, v in rerun_fixtures.items()}}
    return Plan(None, frozenset(rerun), frozenset(rerun_fixtures), tuple(changed), reasons)


def cache_root() -> Path:
    base = os.environ.get("XDG_CACHE_HOME") or ""
    return (Path(base) if os.path.isabs(base) else Path.home() / ".cache") / "crozier"


def lock_path() -> Path:
    return cache_root() / "instrumented-measurement.lock"


# How deeply this process holds the lock: the verb nests both measurements inside one hold.
_HELD = {"depth": 0}


@contextlib.contextmanager
def instrumented_lock(label: str) -> Generator[None]:
    """Hold the host-wide lock around an instrumented build or run; say so while waiting.

    Re-entrant within one process, so the verb holds it across both measurements.
    """
    if _HELD["depth"]:
        _HELD["depth"] += 1
        try:
            yield
        finally:
            _HELD["depth"] -= 1
        return
    path = lock_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = path.open("a+")
    try:
        if not _try_lock(handle):
            print(
                f"{label}: waiting for the instrumented-measurement lock {path} "
                "(another instrumented measurement holds it; at most one runs on a host)",
                file=sys.stderr,
                flush=True,
            )
            _lock(handle)
            print(f"{label}: took the instrumented-measurement lock", file=sys.stderr, flush=True)
        _HELD["depth"] = 1
        try:
            yield
        finally:
            _HELD["depth"] = 0
            _unlock(handle)
    finally:
        handle.close()


def _try_lock(handle: IO[str]) -> bool:
    if sys.platform == "win32":
        import msvcrt

        try:
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            return True
        except OSError:
            return False
    import fcntl

    try:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        return True
    except BlockingIOError:
        return False


def _lock(handle: IO[str]) -> None:
    if sys.platform == "win32":
        import msvcrt

        while True:
            try:
                msvcrt.locking(handle.fileno(), msvcrt.LK_LOCK, 1)
                return
            except OSError:
                continue
    import fcntl

    fcntl.flock(handle.fileno(), fcntl.LOCK_EX)


def _unlock(handle: IO[str]) -> None:
    if sys.platform == "win32":
        import msvcrt

        with contextlib.suppress(OSError):
            msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        return
    import fcntl

    fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
