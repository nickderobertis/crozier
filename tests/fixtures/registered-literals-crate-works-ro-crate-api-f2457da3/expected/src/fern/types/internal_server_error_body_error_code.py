

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InternalServerErrorBodyErrorCode(enum.StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"

    def visit(self, internal_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is InternalServerErrorBodyErrorCode.INTERNAL_ERROR:
            return internal_error()
