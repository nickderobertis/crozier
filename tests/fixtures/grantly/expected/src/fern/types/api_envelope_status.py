

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiEnvelopeStatus(enum.StrEnum):
    SUCCESS = "success"
    ERROR = "error"

    def visit(self, success: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiEnvelopeStatus.SUCCESS:
            return success()
        if self is ApiEnvelopeStatus.ERROR:
            return error()
