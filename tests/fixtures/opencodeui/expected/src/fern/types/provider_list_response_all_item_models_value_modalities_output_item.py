

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderListResponseAllItemModelsValueModalitiesOutputItem(enum.StrEnum):
    TEXT = "text"
    AUDIO = "audio"
    IMAGE = "image"
    VIDEO = "video"
    PDF = "pdf"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        audio: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        pdf: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderListResponseAllItemModelsValueModalitiesOutputItem.TEXT:
            return text()
        if self is ProviderListResponseAllItemModelsValueModalitiesOutputItem.AUDIO:
            return audio()
        if self is ProviderListResponseAllItemModelsValueModalitiesOutputItem.IMAGE:
            return image()
        if self is ProviderListResponseAllItemModelsValueModalitiesOutputItem.VIDEO:
            return video()
        if self is ProviderListResponseAllItemModelsValueModalitiesOutputItem.PDF:
            return pdf()
