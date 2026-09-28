

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HttpForwardValidateActionValidationMode(enum.StrEnum):
    STRICT = "STRICT"
    LOG_ONLY = "LOG_ONLY"

    def visit(self, strict: typing.Callable[[], T_Result], log_only: typing.Callable[[], T_Result]) -> T_Result:
        if self is HttpForwardValidateActionValidationMode.STRICT:
            return strict()
        if self is HttpForwardValidateActionValidationMode.LOG_ONLY:
            return log_only()
