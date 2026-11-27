

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssemblyValidationStatusType(enum.StrEnum):
    ERROR = "ERROR"
    WARNING = "WARNING"

    def visit(self, error: typing.Callable[[], T_Result], warning: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssemblyValidationStatusType.ERROR:
            return error()
        if self is AssemblyValidationStatusType.WARNING:
            return warning()
