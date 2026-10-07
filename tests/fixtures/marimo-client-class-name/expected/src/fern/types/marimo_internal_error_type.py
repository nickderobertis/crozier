

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoInternalErrorType(enum.StrEnum):
    INTERNAL = "internal"

    def visit(self, internal: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoInternalErrorType.INTERNAL:
            return internal()
