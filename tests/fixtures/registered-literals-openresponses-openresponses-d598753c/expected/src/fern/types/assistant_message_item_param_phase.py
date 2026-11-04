

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantMessageItemParamPhase(enum.StrEnum):
    """
    Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`). For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend phase on all assistant messages. Omitting it can degrade performance. Not used for user messages.
    """

    COMMENTARY = "commentary"
    FINAL_ANSWER = "final_answer"

    def visit(self, commentary: typing.Callable[[], T_Result], final_answer: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssistantMessageItemParamPhase.COMMENTARY:
            return commentary()
        if self is AssistantMessageItemParamPhase.FINAL_ANSWER:
            return final_answer()
