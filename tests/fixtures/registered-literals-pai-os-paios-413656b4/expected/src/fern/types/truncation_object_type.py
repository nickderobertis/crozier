

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TruncationObjectType(enum.StrEnum):
    """
    The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.
    """

    AUTO = "auto"
    LAST_MESSAGES = "last_messages"

    def visit(self, auto: typing.Callable[[], T_Result], last_messages: typing.Callable[[], T_Result]) -> T_Result:
        if self is TruncationObjectType.AUTO:
            return auto()
        if self is TruncationObjectType.LAST_MESSAGES:
            return last_messages()
