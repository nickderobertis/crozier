

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileCategory(enum.StrEnum):
    ARCHIVE = "archive"
    AUDIO = "audio"
    DOCUMENT = "document"
    IMAGE = "image"
    VIDEO = "video"
    OTHER = "other"

    def visit(
        self,
        archive: typing.Callable[[], T_Result],
        audio: typing.Callable[[], T_Result],
        document: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileCategory.ARCHIVE:
            return archive()
        if self is FileCategory.AUDIO:
            return audio()
        if self is FileCategory.DOCUMENT:
            return document()
        if self is FileCategory.IMAGE:
            return image()
        if self is FileCategory.VIDEO:
            return video()
        if self is FileCategory.OTHER:
            return other()
