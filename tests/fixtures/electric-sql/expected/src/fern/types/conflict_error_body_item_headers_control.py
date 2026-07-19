

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConflictErrorBodyItemHeadersControl(enum.StrEnum):
    MUST_REFETCH = "must-refetch"

    def visit(self, must_refetch: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConflictErrorBodyItemHeadersControl.MUST_REFETCH:
            return must_refetch()
