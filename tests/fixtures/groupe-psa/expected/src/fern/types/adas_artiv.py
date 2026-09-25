

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdasArtiv(enum.StrEnum):
    """
    Respect of inter vehicle time assist (ARTIV)
    """

    NOT_SELECTED = "NotSelected"
    SELECTED = "Selected"
    UNAVAILABLE = "Unavailable"

    def visit(
        self,
        not_selected: typing.Callable[[], T_Result],
        selected: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdasArtiv.NOT_SELECTED:
            return not_selected()
        if self is AdasArtiv.SELECTED:
            return selected()
        if self is AdasArtiv.UNAVAILABLE:
            return unavailable()
