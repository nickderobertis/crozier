

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnnotationUiOutputType(enum.StrEnum):
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
        if self is AnnotationUiOutputType.NOTE:
            return note()
        if self is AnnotationUiOutputType.RECT:
            return rect()
        if self is AnnotationUiOutputType.TEXT:
            return text()
        if self is AnnotationUiOutputType.CONVERSATION:
            return conversation()
