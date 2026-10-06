

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListBedsRequestXVentMode(enum.StrEnum):
    OPEN = "open"
    SHUT = "shut"

    def visit(self, open: typing.Callable[[], T_Result], shut: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListBedsRequestXVentMode.OPEN:
            return open()
        if self is ListBedsRequestXVentMode.SHUT:
            return shut()
