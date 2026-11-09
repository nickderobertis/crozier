

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageErrorContentType(enum.StrEnum):
    PLAIN = "plain"
    MARKDOWN = "markdown"

    def visit(self, plain: typing.Callable[[], T_Result], markdown: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageErrorContentType.PLAIN:
            return plain()
        if self is MessageErrorContentType.MARKDOWN:
            return markdown()
