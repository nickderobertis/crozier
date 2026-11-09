

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunObjectIncompleteDetailsReason(enum.StrEnum):
    """
    The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.
    """

    MAX_COMPLETION_TOKENS = "max_completion_tokens"
    MAX_PROMPT_TOKENS = "max_prompt_tokens"

    def visit(
        self, max_completion_tokens: typing.Callable[[], T_Result], max_prompt_tokens: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is RunObjectIncompleteDetailsReason.MAX_COMPLETION_TOKENS:
            return max_completion_tokens()
        if self is RunObjectIncompleteDetailsReason.MAX_PROMPT_TOKENS:
            return max_prompt_tokens()
