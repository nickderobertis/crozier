

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BookPilotRequestTug(enum.StrEnum):
    NONE = "none"
    ONE = "one"
    TWO = "two"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        one: typing.Callable[[], T_Result],
        two: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BookPilotRequestTug.NONE:
            return none()
        if self is BookPilotRequestTug.ONE:
            return one()
        if self is BookPilotRequestTug.TWO:
            return two()
