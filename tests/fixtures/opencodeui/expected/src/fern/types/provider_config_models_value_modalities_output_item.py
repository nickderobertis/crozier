

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderConfigModelsValueModalitiesOutputItem(enum.StrEnum):
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
        if self is ProviderConfigModelsValueModalitiesOutputItem.TEXT:
            return text()
        if self is ProviderConfigModelsValueModalitiesOutputItem.AUDIO:
            return audio()
        if self is ProviderConfigModelsValueModalitiesOutputItem.IMAGE:
            return image()
        if self is ProviderConfigModelsValueModalitiesOutputItem.VIDEO:
            return video()
        if self is ProviderConfigModelsValueModalitiesOutputItem.PDF:
            return pdf()
