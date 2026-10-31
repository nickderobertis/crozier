

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValidationErrorsType(enum.StrEnum):
    VALIDATION = "validation"

    def visit(self, validation: typing.Callable[[], T_Result]) -> T_Result:
        if self is ValidationErrorsType.VALIDATION:
            return validation()
