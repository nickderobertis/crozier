"""What a measurement may write about a host's own identifiers.

A run, branch or node name is written by whoever planned the work, so it can hold a
private repository's name, and every file a measurement writes may be committed to this
public repository. No list of private names belongs here, so the outputs carry a digest of
every such identifier rather than the identifier filtered: a digest still tells two
changes apart and stays stable across runs, and the `pr` column says which change a row is.
"""

from __future__ import annotations

import hashlib
import re
import urllib.parse
from collections.abc import Callable, Iterable


def opaque(identifier: str) -> str:
    """The form an identifier takes in any output: one-way and stable across runs."""
    return "id-" + hashlib.sha256(identifier.encode("utf-8")).hexdigest()[:12]


def public_window(spec: str) -> str:
    """A --window as outputs state it: a `runs:` window names runs; commit shas are already public."""
    kind, _, value = spec.partition(":")
    return f"runs:{','.join(opaque(run) for run in value.split(','))}" if kind == "runs" else spec


def public_url(url: str) -> str:
    """A GitHub request as a ledger records it: its branch filter is the one part naming a host identifier."""
    return re.sub(r"([?&]branch=)([^&]*)", lambda m: m.group(1) + opaque(urllib.parse.unquote(m.group(2))), url)


def redactor(names: Iterable[str]) -> Callable[[str], str]:
    """Replace each named identifier where it stands as a whole token of free text, such as a CI log line."""
    ordered = sorted({name for name in names if name}, key=len, reverse=True)
    if not ordered:
        return lambda text: text
    by_name = {name.casefold(): opaque(name) for name in ordered}
    pattern = re.compile(rf"(?<![\w-])(?:{'|'.join(map(re.escape, ordered))})(?![\w-])", re.IGNORECASE)
    return lambda text: pattern.sub(lambda m: by_name[m.group().casefold()], text)
