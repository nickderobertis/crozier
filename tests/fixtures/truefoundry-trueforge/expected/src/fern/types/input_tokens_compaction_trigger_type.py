

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InputTokensCompactionTriggerType(enum.StrEnum):
    """
    Trigger compaction when the estimated input reaches a token limit.
    """

    INPUT_TOKENS = "input_tokens"

    def visit(self, input_tokens: typing.Callable[[], T_Result]) -> T_Result:
        if self is InputTokensCompactionTriggerType.INPUT_TOKENS:
            return input_tokens()
