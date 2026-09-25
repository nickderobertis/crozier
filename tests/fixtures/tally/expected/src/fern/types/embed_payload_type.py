

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbedPayloadType(enum.StrEnum):
    RICH = "rich"
    VIDEO = "video"
    PHOTO = "photo"
    LINK = "link"
    PDF = "pdf"
    GIST = "gist"
    IMAGE = "image/*"
    AUDIO = "audio/*"

    def visit(
        self,
        rich: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        photo: typing.Callable[[], T_Result],
        link: typing.Callable[[], T_Result],
        pdf: typing.Callable[[], T_Result],
        gist: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        audio: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmbedPayloadType.RICH:
            return rich()
        if self is EmbedPayloadType.VIDEO:
            return video()
        if self is EmbedPayloadType.PHOTO:
            return photo()
        if self is EmbedPayloadType.LINK:
            return link()
        if self is EmbedPayloadType.PDF:
            return pdf()
        if self is EmbedPayloadType.GIST:
            return gist()
        if self is EmbedPayloadType.IMAGE:
            return image()
        if self is EmbedPayloadType.AUDIO:
            return audio()
