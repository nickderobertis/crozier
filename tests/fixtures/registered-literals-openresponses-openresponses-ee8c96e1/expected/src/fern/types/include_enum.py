

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IncludeEnum(enum.StrEnum):
    """ """

    REASONING_ENCRYPTED_CONTENT = "reasoning.encrypted_content"
    MESSAGE_OUTPUT_TEXT_LOGPROBS = "message.output_text.logprobs"

    def visit(
        self,
        reasoning_encrypted_content: typing.Callable[[], T_Result],
        message_output_text_logprobs: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IncludeEnum.REASONING_ENCRYPTED_CONTENT:
            return reasoning_encrypted_content()
        if self is IncludeEnum.MESSAGE_OUTPUT_TEXT_LOGPROBS:
            return message_output_text_logprobs()
