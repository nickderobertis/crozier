

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StopReasonType(enum.StrEnum):
    END_TURN = "end_turn"
    ERROR = "error"
    LLM_API_ERROR = "llm_api_error"
    INVALID_LLM_RESPONSE = "invalid_llm_response"
    INVALID_TOOL_CALL = "invalid_tool_call"
    MAX_STEPS = "max_steps"
    MAX_TOKENS_EXCEEDED = "max_tokens_exceeded"
    NO_TOOL_CALL = "no_tool_call"
    TOOL_RULE = "tool_rule"
    CANCELLED = "cancelled"
    REQUIRES_APPROVAL = "requires_approval"
    CONTEXT_WINDOW_OVERFLOW_IN_SYSTEM_PROMPT = "context_window_overflow_in_system_prompt"

    def visit(
        self,
        end_turn: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        llm_api_error: typing.Callable[[], T_Result],
        invalid_llm_response: typing.Callable[[], T_Result],
        invalid_tool_call: typing.Callable[[], T_Result],
        max_steps: typing.Callable[[], T_Result],
        max_tokens_exceeded: typing.Callable[[], T_Result],
        no_tool_call: typing.Callable[[], T_Result],
        tool_rule: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        requires_approval: typing.Callable[[], T_Result],
        context_window_overflow_in_system_prompt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StopReasonType.END_TURN:
            return end_turn()
        if self is StopReasonType.ERROR:
            return error()
        if self is StopReasonType.LLM_API_ERROR:
            return llm_api_error()
        if self is StopReasonType.INVALID_LLM_RESPONSE:
            return invalid_llm_response()
        if self is StopReasonType.INVALID_TOOL_CALL:
            return invalid_tool_call()
        if self is StopReasonType.MAX_STEPS:
            return max_steps()
        if self is StopReasonType.MAX_TOKENS_EXCEEDED:
            return max_tokens_exceeded()
        if self is StopReasonType.NO_TOOL_CALL:
            return no_tool_call()
        if self is StopReasonType.TOOL_RULE:
            return tool_rule()
        if self is StopReasonType.CANCELLED:
            return cancelled()
        if self is StopReasonType.REQUIRES_APPROVAL:
            return requires_approval()
        if self is StopReasonType.CONTEXT_WINDOW_OVERFLOW_IN_SYSTEM_PROMPT:
            return context_window_overflow_in_system_prompt()
