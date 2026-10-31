

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenapiValidationErrorsType(enum.StrEnum):
    OPENAPI = "openapi"

    def visit(self, openapi: typing.Callable[[], T_Result]) -> T_Result:
        if self is OpenapiValidationErrorsType.OPENAPI:
            return openapi()
