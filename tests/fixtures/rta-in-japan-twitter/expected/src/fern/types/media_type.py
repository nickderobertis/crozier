

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MediaType(enum.StrEnum):
    ANIMATED_GIF = "animated_gif"
    PHOTO = "photo"
    VIDEO = "video"

    def visit(
        self,
        animated_gif: typing.Callable[[], T_Result],
        photo: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MediaType.ANIMATED_GIF:
            return animated_gif()
        if self is MediaType.PHOTO:
            return photo()
        if self is MediaType.VIDEO:
            return video()
