

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFavouritesRequestRepresentation(enum.StrEnum):
    FLAT = "flat"
    TREE = "tree"

    def visit(self, flat: typing.Callable[[], T_Result], tree: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetFavouritesRequestRepresentation.FLAT:
            return flat()
        if self is GetFavouritesRequestRepresentation.TREE:
            return tree()
