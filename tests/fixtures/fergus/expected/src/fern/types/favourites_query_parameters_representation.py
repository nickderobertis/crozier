

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FavouritesQueryParametersRepresentation(enum.StrEnum):
    FLAT = "flat"
    TREE = "tree"

    def visit(self, flat: typing.Callable[[], T_Result], tree: typing.Callable[[], T_Result]) -> T_Result:
        if self is FavouritesQueryParametersRepresentation.FLAT:
            return flat()
        if self is FavouritesQueryParametersRepresentation.TREE:
            return tree()
