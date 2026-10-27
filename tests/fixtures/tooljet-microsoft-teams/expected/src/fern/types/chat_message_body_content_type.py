

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatMessageBodyContentType(enum.StrEnum):
    TEXT = "text"
    HTML = "html"

    def visit(self, text: typing.Callable[[], T_Result], html: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatMessageBodyContentType.TEXT:
            return text()
        if self is ChatMessageBodyContentType.HTML:
            return html()
