

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdasRgi(enum.StrEnum):
    """
    Recommended gear indicator
    """

    NONE = "None"
    UP = "Up"
    DOWN = "Down"
    UP_DOWN = "UpDown"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        up: typing.Callable[[], T_Result],
        down: typing.Callable[[], T_Result],
        up_down: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdasRgi.NONE:
            return none()
        if self is AdasRgi.UP:
            return up()
        if self is AdasRgi.DOWN:
            return down()
        if self is AdasRgi.UP_DOWN:
            return up_down()
