

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListIntelligencesResponseItemsItemMediaType(enum.StrEnum):
    """
    Type of media analyzed
    """

    AUDIO = "audio"
    VIDEO = "video"
    IMAGE = "image"

    def visit(
        self,
        audio: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListIntelligencesResponseItemsItemMediaType.AUDIO:
            return audio()
        if self is ListIntelligencesResponseItemsItemMediaType.VIDEO:
            return video()
        if self is ListIntelligencesResponseItemsItemMediaType.IMAGE:
            return image()
