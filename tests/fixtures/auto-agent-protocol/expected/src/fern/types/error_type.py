

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorType(enum.StrEnum):
    AAP_ERROR = "aap.error"

    def visit(self, aap_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ErrorType.AAP_ERROR:
            return aap_error()
