"""Drive a naming-acceptance measurement's generated SDK through its public client.

Usage: naming_acceptance_runtime.py JOURNEY SDK_SRC

JOURNEY is one of `colliding-request`, `colliding-responses`,
`colliding-control` (#944) or `recursive-alias-dependents` (#922); SDK_SRC is
the generated SDK's `src/` directory. Each request goes through an
`httpx.MockTransport`, so nothing leaves the process.

Exit status: 0 when the journey holds; 1 with the failing check's message;
2 on a usage error.
"""

from __future__ import annotations

import importlib
import json
import pkgutil
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

import httpx


def client(handler: Callable[[httpx.Request], httpx.Response]) -> Any:
    from fern import FernApi

    return FernApi(
        base_url="https://slash.example.com", httpx_client=httpx.Client(transport=httpx.MockTransport(handler))
    )


def colliding_request() -> None:
    """Each colliding component's own model builds the body, sent as declared."""
    from fern import KilnGlazeCoat, KilnGlazeCoat2

    sent: list[object] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(json.loads(request.content))
        return httpx.Response(204)

    client(handler).create_records(left=KilnGlazeCoat2(left="matte"), right=KilnGlazeCoat(right=3))
    if sent != [{"left": {"left": "matte"}, "right": {"right": 3}}]:
        raise SystemExit(f"colliding-request: sent {sent!r}")


def colliding_responses() -> None:
    """Each operation's declared response parses into its own component's class."""
    from fern import KilnGlazeCoat, KilnGlazeCoat2

    bodies = {"/left": {"left": "matte"}, "/right": {"right": 3}}

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=bodies[request.url.path])

    api = client(handler)
    left = api.get_left()
    right = api.get_right()
    if not isinstance(left, KilnGlazeCoat2) or left.left != "matte":
        raise SystemExit(f"colliding-responses: get_left returned {left!r}")
    if not isinstance(right, KilnGlazeCoat) or right.right != 3:
        raise SystemExit(f"colliding-responses: get_right returned {right!r}")


def colliding_control() -> None:
    """The one component's response parses into its class."""
    from fern import KilnGlazeCoat

    def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"left": "matte"})

    left = client(handler).get_left()
    if not isinstance(left, KilnGlazeCoat) or left.left != "matte":
        raise SystemExit(f"colliding-control: get_left returned {left!r}")


def recursive_alias_dependents() -> None:
    """Every module imports, and the dependent model holds a recursive object."""
    import fern

    for module in pkgutil.walk_packages(fern.__path__, "fern."):
        importlib.import_module(module.name)
    from fern.types.fit_summary import FitSummary

    summary = FitSummary(report={"engine": "nuts", "inference_diagnostics": {"chains": [1, {"ok": True}]}})
    if summary.report.engine != "nuts":
        raise SystemExit(f"recursive-alias-dependents: built {summary!r}")


JOURNEYS: dict[str, Callable[[], None]] = {
    "colliding-request": colliding_request,
    "colliding-responses": colliding_responses,
    "colliding-control": colliding_control,
    "recursive-alias-dependents": recursive_alias_dependents,
}


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in JOURNEYS:
        print(f"usage: {Path(sys.argv[0]).name} {{{','.join(JOURNEYS)}}} SDK_SRC", file=sys.stderr)
        raise SystemExit(2)
    sys.path.insert(0, sys.argv[2])
    JOURNEYS[sys.argv[1]]()
    print(f"{sys.argv[1]}: ok")


if __name__ == "__main__":
    main()
