

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TableOptionsFormat(enum.StrEnum):
    MARKDOWN = "markdown"
    HTML = "html"

    def visit(self, markdown: typing.Callable[[], T_Result], html: typing.Callable[[], T_Result]) -> T_Result:
        if self is TableOptionsFormat.MARKDOWN:
            return markdown()
        if self is TableOptionsFormat.HTML:
            return html()
