

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListGlazesRequestFiringItem(enum.StrEnum):
    BISQUE = "bisque"
    GLAZE = "glaze"
    RAKU = "raku"

    def visit(
        self,
        bisque: typing.Callable[[], T_Result],
        glaze: typing.Callable[[], T_Result],
        raku: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListGlazesRequestFiringItem.BISQUE:
            return bisque()
        if self is ListGlazesRequestFiringItem.GLAZE:
            return glaze()
        if self is ListGlazesRequestFiringItem.RAKU:
            return raku()
