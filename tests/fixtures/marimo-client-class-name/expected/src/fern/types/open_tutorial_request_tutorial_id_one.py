

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenTutorialRequestTutorialIdOne(enum.StrEnum):
    MARKDOWN_FORMAT = "markdown-format"

    def visit(self, markdown_format: typing.Callable[[], T_Result]) -> T_Result:
        if self is OpenTutorialRequestTutorialIdOne.MARKDOWN_FORMAT:
            return markdown_format()
