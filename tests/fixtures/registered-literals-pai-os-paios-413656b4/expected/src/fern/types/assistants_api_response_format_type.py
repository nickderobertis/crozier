

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantsApiResponseFormatType(enum.StrEnum):
    """
    Must be one of `text` or `json_object`.
    """

    TEXT = "text"
    JSON_OBJECT = "json_object"

    def visit(self, text: typing.Callable[[], T_Result], json_object: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssistantsApiResponseFormatType.TEXT:
            return text()
        if self is AssistantsApiResponseFormatType.JSON_OBJECT:
            return json_object()
