

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConflictErrorBodyErrorCode(enum.StrEnum):
    CONFLICT = "CONFLICT"

    def visit(self, conflict: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConflictErrorBodyErrorCode.CONFLICT:
            return conflict()
