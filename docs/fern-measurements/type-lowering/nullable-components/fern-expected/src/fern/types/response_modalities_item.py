

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseModalitiesItem(enum.StrEnum):
    TEXT = "text"
    AUDIO = "audio"

    def visit(self, text: typing.Callable[[], T_Result], audio: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseModalitiesItem.TEXT:
            return text()
        if self is ResponseModalitiesItem.AUDIO:
            return audio()
