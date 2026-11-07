

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionAttachmentKind(enum.StrEnum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"

    def visit(
        self,
        image: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        audio: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActionAttachmentKind.IMAGE:
            return image()
        if self is ActionAttachmentKind.VIDEO:
            return video()
        if self is ActionAttachmentKind.AUDIO:
            return audio()
        if self is ActionAttachmentKind.FILE:
            return file()
