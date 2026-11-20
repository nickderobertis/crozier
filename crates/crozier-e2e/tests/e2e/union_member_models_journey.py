"""Exercise the query-union member models of `union-inheritance/query-union-member-models`.

usage: union_member_models_journey.py SDK_SRC

SDK_SRC is a generated SDK's `src/` directory holding the `fern` package. Each
parameter's union alias is validated with pydantic: a closed or open object
member's payload parses into its named model with its fields, and `None` is
accepted exactly where the document declares the member nullable. Prints one
line per check and exits 0 only when all hold; exits 2 on a usage error.
"""

from __future__ import annotations

import pathlib
import sys


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage: union_member_models_journey.py SDK_SRC", file=sys.stderr)
        return 2
    src = pathlib.Path(argv[0])
    if not (src / "fern" / "__init__.py").is_file():
        print(f"{src}: must contain the generated fern package", file=sys.stderr)
        return 2
    sys.path.insert(0, str(src))
    import fern
    import pydantic

    def parse(alias: str, value: object) -> object:
        return pydantic.TypeAdapter(getattr(fern, alias)).validate_python(value)

    def rejects(alias: str, value: object) -> bool:
        try:
            parse(alias, value)
        except pydantic.ValidationError:
            return True
        return False

    kiln = parse("ListFiringsRequestKiln", {"any": True, "all": False})
    assert type(kiln).__name__ == "ListFiringsRequestKilnAll", type(kiln)
    assert (kiln.any, kiln.all_) == (True, False), kiln
    assert parse("ListFiringsRequestKiln", ["k1", "k2"]) == ["k1", "k2"]
    print("kiln: {any, all} parses into ListFiringsRequestKilnAll")

    cone = parse("ListFiringsRequestCone", {"cone": 6, "shelf": "top"})
    assert type(cone).__name__ == "ListFiringsRequestConeCone", type(cone)
    assert (cone.cone, cone.shelf) == (6, "top"), cone
    print("cone: {cone, shelf} parses into ListFiringsRequestConeCone")

    glaze = parse("ListFiringsRequestGlaze", {})
    assert type(glaze).__name__ == "ListFiringsRequestGlazeOne", type(glaze)
    assert parse("ListFiringsRequestGlaze", "matte") == "matte"
    print("glaze: {} parses into ListFiringsRequestGlazeOne")

    # Only the atmosphere members declare `nullable: true`.
    assert parse("ListFiringsRequestAtmosphere", None) is None
    assert parse("ListFiringsRequestAtmosphere", [None, "reduction"])[0] is None
    for alias in ("ListFiringsRequestKiln", "ListFiringsRequestCone", "ListFiringsRequestGlaze"):
        assert rejects(alias, None), f"{alias} accepted None"
    print("null: accepted by atmosphere's nullable members only")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
