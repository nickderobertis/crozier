

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActListResponseActionsItemAttentionState(enum.StrEnum):
    NEEDS_ATTENTION = "needs_attention"
    CLEAR = "clear"

    def visit(self, needs_attention: typing.Callable[[], T_Result], clear: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActListResponseActionsItemAttentionState.NEEDS_ATTENTION:
            return needs_attention()
        if self is ActListResponseActionsItemAttentionState.CLEAR:
            return clear()
