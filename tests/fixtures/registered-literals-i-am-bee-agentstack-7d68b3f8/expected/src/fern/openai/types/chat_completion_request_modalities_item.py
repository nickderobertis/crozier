

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionRequestModalitiesItem(enum.StrEnum):
    TEXT = "text"
    AUDIO = "audio"

    def visit(self, text: typing.Callable[[], T_Result], audio: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatCompletionRequestModalitiesItem.TEXT:
            return text()
        if self is ChatCompletionRequestModalitiesItem.AUDIO:
            return audio()
