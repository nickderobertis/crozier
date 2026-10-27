

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SendChannelMessageRequestBodyContentType(enum.StrEnum):
    TEXT = "text"
    HTML = "html"

    def visit(self, text: typing.Callable[[], T_Result], html: typing.Callable[[], T_Result]) -> T_Result:
        if self is SendChannelMessageRequestBodyContentType.TEXT:
            return text()
        if self is SendChannelMessageRequestBodyContentType.HTML:
            return html()
