

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyDeleteResponsePayloadItemsItemType(enum.StrEnum):
    TEXT = "text"
    SELECT = "select"
    EMAIL = "email"
    IMAGE_URL = "imageUrl"
    HIDDEN = "hidden"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        select: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        image_url: typing.Callable[[], T_Result],
        hidden: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyDeleteResponsePayloadItemsItemType.TEXT:
            return text()
        if self is SurveyDeleteResponsePayloadItemsItemType.SELECT:
            return select()
        if self is SurveyDeleteResponsePayloadItemsItemType.EMAIL:
            return email()
        if self is SurveyDeleteResponsePayloadItemsItemType.IMAGE_URL:
            return image_url()
        if self is SurveyDeleteResponsePayloadItemsItemType.HIDDEN:
            return hidden()
