

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DisclosureContentType(enum.StrEnum):
    PLAIN = "plain"
    MARKDOWN = "markdown"

    def visit(self, plain: typing.Callable[[], T_Result], markdown: typing.Callable[[], T_Result]) -> T_Result:
        if self is DisclosureContentType.PLAIN:
            return plain()
        if self is DisclosureContentType.MARKDOWN:
            return markdown()
