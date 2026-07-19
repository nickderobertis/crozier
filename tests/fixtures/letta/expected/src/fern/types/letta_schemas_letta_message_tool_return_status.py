

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LettaSchemasLettaMessageToolReturnStatus(enum.StrEnum):
    SUCCESS = "success"
    ERROR = "error"

    def visit(self, success: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is LettaSchemasLettaMessageToolReturnStatus.SUCCESS:
            return success()
        if self is LettaSchemasLettaMessageToolReturnStatus.ERROR:
            return error()
