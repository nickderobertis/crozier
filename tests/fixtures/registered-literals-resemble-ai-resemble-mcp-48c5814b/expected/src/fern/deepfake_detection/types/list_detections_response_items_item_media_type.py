

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListDetectionsResponseItemsItemMediaType(enum.StrEnum):
    AUDIO = "audio"
    VIDEO = "video"
    IMAGE = "image"

    def visit(
        self,
        audio: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListDetectionsResponseItemsItemMediaType.AUDIO:
            return audio()
        if self is ListDetectionsResponseItemsItemMediaType.VIDEO:
            return video()
        if self is ListDetectionsResponseItemsItemMediaType.IMAGE:
            return image()
