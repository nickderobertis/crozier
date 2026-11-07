

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorResponseErrorCode(enum.StrEnum):
    TWO = "2"
    TEN = "10"
    ELEVEN = "11"

    def visit(
        self,
        two: typing.Callable[[], T_Result],
        ten: typing.Callable[[], T_Result],
        eleven: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorResponseErrorCode.TWO:
            return two()
        if self is ErrorResponseErrorCode.TEN:
            return ten()
        if self is ErrorResponseErrorCode.ELEVEN:
            return eleven()
