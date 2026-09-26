

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderListResponseAllItemModelsValueModalitiesInputItem(enum.StrEnum):
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
        if self is ProviderListResponseAllItemModelsValueModalitiesInputItem.TEXT:
            return text()
        if self is ProviderListResponseAllItemModelsValueModalitiesInputItem.AUDIO:
            return audio()
        if self is ProviderListResponseAllItemModelsValueModalitiesInputItem.IMAGE:
            return image()
        if self is ProviderListResponseAllItemModelsValueModalitiesInputItem.VIDEO:
            return video()
        if self is ProviderListResponseAllItemModelsValueModalitiesInputItem.PDF:
            return pdf()
