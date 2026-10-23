

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemCharLimitInputType(enum.StrEnum):
    TEXT = "text"
    EMAIL = "email"
    URL = "url"
    NUMBER = "number"
    PHONE = "phone"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyBlocksItemElementsItemCharLimitInputType.TEXT:
            return text()
        if self is SurveyBlocksItemElementsItemCharLimitInputType.EMAIL:
            return email()
        if self is SurveyBlocksItemElementsItemCharLimitInputType.URL:
            return url()
        if self is SurveyBlocksItemElementsItemCharLimitInputType.NUMBER:
            return number()
        if self is SurveyBlocksItemElementsItemCharLimitInputType.PHONE:
            return phone()
