

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SourceLifecycleAdmission(enum.StrEnum):
    OPEN = "open"
    ALLOWLISTED = "allowlisted"

    def visit(self, open: typing.Callable[[], T_Result], allowlisted: typing.Callable[[], T_Result]) -> T_Result:
        if self is SourceLifecycleAdmission.OPEN:
            return open()
        if self is SourceLifecycleAdmission.ALLOWLISTED:
            return allowlisted()
