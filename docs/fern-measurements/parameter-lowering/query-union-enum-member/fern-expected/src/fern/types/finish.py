

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Finish(enum.StrEnum):
    RAW = "raw"
    BRUSHED = "brushed"
    CALENDERED = "calendered"

    def visit(
        self,
        raw: typing.Callable[[], T_Result],
        brushed: typing.Callable[[], T_Result],
        calendered: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Finish.RAW:
            return raw()
        if self is Finish.BRUSHED:
            return brushed()
        if self is Finish.CALENDERED:
            return calendered()
