#!/usr/bin/env python3
"""Refresh the vendored llmlint plugin set and the lock that records it.

The judged tier resolves its rules from `llmlint-plugins/` (files committed
here), not from the network at job time — see `docs/llmlint-plugins.md` for why.
This script is the ONLY way that set moves: it re-fetches each recorded URL at
its recorded `@pin`, rewrites the vendored copy, and rewrites
`llmlint-plugins/lock.json` (resolved version, content hash, rule names) so an
upstream rule change lands as a reviewable diff.

Usage (needs network, plus `llmlint` on PATH to name each plugin's rules):

    just llmlint-plugins-refresh        # ./tools/llmlint/llmlint-plugins.py refresh

`url`/`pin`/`file`/`name` in the lock are the hand-edited inputs — add a plugin
by adding an entry with those four fields (and its path to `llmlint.yml`), then
refresh. Every other field is generated; editing one by hand is what the
offline suite in `tools/llmlint/tests/llmlint_plugins_test.py` catches.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path, PurePosixPath
from typing import Any, NoReturn

REPO = Path(__file__).resolve().parents[2]
# Every vendored plugin document lives here; the lock may name nothing outside it.
VENDOR_DIR = "llmlint-plugins"
LOCK = REPO / VENDOR_DIR / "lock.json"
FETCH_TIMEOUT_SECONDS = 30
# The hand-edited fields of a lock entry; refresh generates the rest.
INPUT_FIELDS = ("name", "url", "pin", "file")
# A plugin config declares its version on a top-level `version:` line; that
# declared version is what a consumer's `@pin` ranges over and what identifies a
# cache entry, so it is the version the lock records.
VERSION_LINE = re.compile(r"^version:[ \t]*(?P<version>[^\s#]+)", re.MULTILINE)
#: Test seam, as `CROZIER_CORPUS_PIN_ORIGIN` is for the corpus pins: when set,
#: it replaces the scheme and host of each recorded URL FOR THE FETCH ONLY, so
#: the boundary suite can drive a whole refresh against its own loopback server.
#: It never changes the URL the lock records, and any value that is not a
#: loopback origin is refused, so it cannot redirect a fetch off this machine.
ORIGIN_ENV = "CROZIER_LLMLINT_PLUGINS_ORIGIN"
LOOPBACK_ORIGIN = re.compile(r"http://(?:127\.0\.0\.1|localhost):([0-9]{1,5})")


def fail(message: str, remedy: str) -> NoReturn:
    print(f"llmlint-plugins: {message}", file=sys.stderr)
    print(f"llmlint-plugins: {remedy}", file=sys.stderr)
    raise SystemExit(1)


def load_lock() -> dict[str, Any]:
    try:
        lock = json.loads(LOCK.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"no lock at {LOCK.relative_to(REPO)}", "restore it from git history")
    except json.JSONDecodeError as error:
        fail(f"{LOCK.relative_to(REPO)} is not valid JSON: {error}", "fix the JSON")
    if not isinstance(lock, dict) or not isinstance(lock.get("plugins"), list) or not lock["plugins"]:
        fail(f"{LOCK.relative_to(REPO)} declares no plugins", "add a plugin entry")
    for index, plugin in enumerate(lock["plugins"]):
        missing = [
            key
            for key in INPUT_FIELDS
            if not isinstance(plugin, dict) or not isinstance(plugin.get(key), str) or not plugin[key]
        ]
        if missing:
            fail(
                f"{LOCK.relative_to(REPO)} plugin #{index + 1} lacks {', '.join(missing)}",
                "give every plugin entry a non-empty name, url, pin and file (docs/llmlint-plugins.md)",
            )
        rules = plugin.get("rules", [])
        if not isinstance(rules, list) or not all(isinstance(rule, str) and rule for rule in rules):
            fail(
                f"{LOCK.relative_to(REPO)} plugin #{index + 1} has `rules` {rules!r}, not a list of rule names",
                "restore the lock from git, or delete the field and refresh to regenerate it",
            )
        if not isinstance(plugin.get("bundled", False), bool):
            fail(
                f"{LOCK.relative_to(REPO)} plugin #{index + 1} has `bundled` {plugin['bundled']!r}, not a boolean",
                'write `"bundled": true` for a plugin llmlint ships, or drop the field for a vendored one',
            )
        file = PurePosixPath(plugin["file"])
        vendored = (REPO / VENDOR_DIR).resolve()
        # A relative path's first part is the vendor directory only when it is
        # neither absolute nor a drive or backslash spelling; resolving catches a
        # symlink that leads back out.
        if (
            ".." in file.parts
            or len(file.parts) < 2
            or file.parts[0] != VENDOR_DIR
            or not (REPO / file).resolve().is_relative_to(vendored)
        ):
            fail(
                f"{LOCK.relative_to(REPO)} plugin #{index + 1} file {plugin['file']!r} is not under {VENDOR_DIR}/",
                f"record a relative path inside {VENDOR_DIR}/ with no '..' (e.g. {VENDOR_DIR}/base.llmlint.yml)",
            )
    return lock


def satisfies(pin: str, version: str) -> bool:
    """A pin is a dotted-component prefix: `@1` accepts any 1.x, `@1.2` any 1.2.x."""
    pinned = pin.split(".")
    return version.split(".")[: len(pinned)] == pinned


def fetch_url(url: str) -> str:
    """The URL a fetch of `url` reads: `url` itself, or its path on the test origin."""
    origin = os.environ.get(ORIGIN_ENV)
    if origin is None:
        return url
    port = LOOPBACK_ORIGIN.fullmatch(origin)
    if not port or not 1 <= int(port.group(1)) <= 65535:
        fail(
            f"{ORIGIN_ENV}={origin!r} is not a loopback origin",
            f"unset {ORIGIN_ENV}; it exists only for the boundary suite's own server",
        )
    return origin + urllib.parse.urlsplit(url).path


def fetch(url: str) -> str:
    if not url.startswith("https://"):
        fail(f"plugin URL is not https: {url}", "record an https:// URL in the lock")
    request = urllib.request.Request(fetch_url(url), headers={"User-Agent": "crozier-llmlint-plugins"})
    try:
        with urllib.request.urlopen(request, timeout=FETCH_TIMEOUT_SECONDS) as response:
            data = response.read()
    except (urllib.error.URLError, TimeoutError) as error:
        fail(f"could not fetch {url}: {error}", "check the network and the recorded URL, then re-run")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as error:
        fail(
            f"{url} served a document that is not UTF-8 ({error})",
            "check that the recorded URL names the rule document itself, or report it upstream",
        )
    raise AssertionError("unreachable")


def declared_version(url: str, document: str) -> str:
    match = VERSION_LINE.search(document)
    if match is None:
        fail(
            f"{url} declares no top-level `version:`",
            "a plugin must be versioned for a pin to mean anything; report it upstream",
        )
    return match.group("version").strip("\"'")


def rules_by_source(plugins: list[dict[str, Any]]) -> dict[str, list[str]]:
    """Ask llmlint which rules each plugin contributes, keyed by its source.

    llmlint is the only authority on that mapping (it merges plugins, applies
    `override`, and rejects duplicate names), so the lock records what llmlint
    itself resolved rather than a second YAML reading of the same files.
    """
    entries = [
        f"{plugin['url']}@{plugin['pin']}" if plugin.get("bundled") else str(REPO / plugin["file"])
        for plugin in plugins
    ]
    config = "plugins:\n" + "".join(f'  - "{entry}"\n' for entry in entries)
    config += "agents:\n  default:\n    harness: claude-code\n"
    with tempfile.TemporaryDirectory() as scratch:
        path = Path(scratch) / "llmlint.yml"
        path.write_text(config, encoding="utf-8")
        try:
            resolved = subprocess.run(
                ["llmlint", "config", "--sources", "-c", str(path), "--cwd", str(REPO)],
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            fail("llmlint is not on PATH", "install it with `just setup-llmlint`")
        if resolved.returncode != 0:
            fail(
                f"llmlint could not resolve the refreshed plugin set: {resolved.stderr.strip()}",
                "fix the reported plugin, then re-run",
            )
    remedy = (
        "check that `llmlint --version` is the release `just setup-llmlint` installs"
        " (reinstall it with that recipe), then re-run"
    )
    try:
        reported = json.loads(resolved.stdout)
    except json.JSONDecodeError as error:
        fail(f"`llmlint config --sources` printed no JSON document ({error})", remedy)
    sources = reported.get("sources") if isinstance(reported, dict) else None
    rules = sources.get("rules") if isinstance(sources, dict) else None
    if not isinstance(rules, dict):
        fail("`llmlint config --sources` reported no `sources.rules` object", remedy)
    by_source: dict[str, list[str]] = {}
    for rule, origin in sorted(rules.items()):
        source = origin.get("source") if isinstance(origin, dict) else None
        if not isinstance(source, str) or not source:
            fail(f"`llmlint config --sources` reported rule {rule!r} without a source string", remedy)
        by_source.setdefault(source, []).append(rule)
    return by_source


def llmlint_version() -> str:
    """The installed llmlint's version, the last word of `llmlint --version`."""
    try:
        reported = subprocess.run(["llmlint", "--version"], capture_output=True, text=True, check=False)
    except FileNotFoundError:
        fail("llmlint is not on PATH", "install it with `just setup-llmlint`")
    words = reported.stdout.split()
    if reported.returncode != 0 or not words:
        fail(
            f"`llmlint --version` exited {reported.returncode} and printed {reported.stdout.strip()!r}, no version",
            "reinstall llmlint with `just setup-llmlint`, then re-run",
        )
    return words[-1]


def describe(plugin: dict[str, Any]) -> str:
    version = plugin.get("version", "bundled")
    return f"{plugin['name']} {version} ({len(plugin.get('rules', []))} rules)"


def refresh() -> int:
    lock = load_lock()
    before = {plugin["name"]: dict(plugin) for plugin in lock["plugins"]}
    for plugin in lock["plugins"]:
        if plugin.get("bundled"):
            continue
        document = fetch(plugin["url"])
        version = declared_version(plugin["url"], document)
        if not satisfies(plugin["pin"], version):
            fail(
                f"{plugin['url']} declares version {version}, which its pin @{plugin['pin']} rejects",
                f"widen or bump `pin` for {plugin['name']} in {LOCK.relative_to(REPO)} deliberately",
            )
        target = REPO / plugin["file"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(document, encoding="utf-8")
        plugin["version"] = version
        plugin["sha256"] = hashlib.sha256(document.encode("utf-8")).hexdigest()

    by_source = rules_by_source(lock["plugins"])
    for plugin in lock["plugins"]:
        if plugin.get("bundled"):
            plugin["captured_with_llmlint"] = llmlint_version()
            source = f"{plugin['url']}@{plugin['pin']}"
        else:
            source = str(REPO / plugin["file"])
        plugin["rules"] = by_source.get(source, [])
        if not plugin["rules"]:
            fail(
                f"{plugin['name']} contributed no rules to the resolved config",
                "check the plugin document, then re-run",
            )

    LOCK.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")

    moved = [
        plugin
        for plugin in lock["plugins"]
        # Whole-entry compare, so a moved version, hash, or rule list all count.
        if before[plugin["name"]] != plugin
    ]
    if not moved:
        print(f"llmlint-plugins: unchanged ({len(lock['plugins'])} plugins)")
        return 0
    for plugin in moved:
        was = set(before[plugin["name"]].get("rules", []))
        now = set(plugin["rules"])
        print(f"llmlint-plugins: {describe(plugin)}")
        for rule in sorted(now - was):
            print(f"  + {rule}")
        for rule in sorted(was - now):
            print(f"  - {rule}")
    print("llmlint-plugins: review the diff and commit llmlint-plugins/ together")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "command",
        choices=["refresh"],
        help="refresh: re-fetch every recorded plugin at its pin and rewrite the lock",
    )
    parser.parse_args(argv)
    return refresh()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
