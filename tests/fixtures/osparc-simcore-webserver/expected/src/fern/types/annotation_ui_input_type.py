

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnnotationUiInputType(enum.StrEnum):
    NOTE = "note"
    RECT = "rect"
    TEXT = "text"
    CONVERSATION = "conversation"

    def visit(
        self,
        note: typing.Callable[[], T_Result],
        rect: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
        conversation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AnnotationUiInputType.NOTE:
            return note()
        if self is AnnotationUiInputType.RECT:
            return rect()
        if self is AnnotationUiInputType.TEXT:
            return text()
        if self is AnnotationUiInputType.CONVERSATION:
            return conversation()
