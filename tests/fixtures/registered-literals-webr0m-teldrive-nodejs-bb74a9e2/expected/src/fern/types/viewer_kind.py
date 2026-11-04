

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewerKind(enum.StrEnum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    PDF = "pdf"
    EBOOK = "ebook"
    TEXT = "text"

    def visit(
        self,
        image: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        audio: typing.Callable[[], T_Result],
        pdf: typing.Callable[[], T_Result],
        ebook: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ViewerKind.IMAGE:
            return image()
        if self is ViewerKind.VIDEO:
            return video()
        if self is ViewerKind.AUDIO:
            return audio()
        if self is ViewerKind.PDF:
            return pdf()
        if self is ViewerKind.EBOOK:
            return ebook()
        if self is ViewerKind.TEXT:
            return text()
