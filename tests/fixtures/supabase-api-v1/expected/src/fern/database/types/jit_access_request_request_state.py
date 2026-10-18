

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class JitAccessRequestRequestState(enum.StrEnum):
    ENABLED = "enabled"
    DISABLED = "disabled"

    def visit(self, enabled: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is JitAccessRequestRequestState.ENABLED:
            return enabled()
        if self is JitAccessRequestRequestState.DISABLED:
            return disabled()
