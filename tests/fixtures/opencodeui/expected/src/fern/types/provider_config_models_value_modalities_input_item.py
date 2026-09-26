

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderConfigModelsValueModalitiesInputItem(enum.StrEnum):
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
        if self is ProviderConfigModelsValueModalitiesInputItem.TEXT:
            return text()
        if self is ProviderConfigModelsValueModalitiesInputItem.AUDIO:
            return audio()
        if self is ProviderConfigModelsValueModalitiesInputItem.IMAGE:
            return image()
        if self is ProviderConfigModelsValueModalitiesInputItem.VIDEO:
            return video()
        if self is ProviderConfigModelsValueModalitiesInputItem.PDF:
            return pdf()
