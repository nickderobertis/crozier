

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AiInlineCompletionRequestLanguage(enum.StrEnum):
    MARKDOWN = "markdown"
    PYTHON = "python"
    SQL = "sql"

    def visit(
        self,
        markdown: typing.Callable[[], T_Result],
        python: typing.Callable[[], T_Result],
        sql: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AiInlineCompletionRequestLanguage.MARKDOWN:
            return markdown()
        if self is AiInlineCompletionRequestLanguage.PYTHON:
            return python()
        if self is AiInlineCompletionRequestLanguage.SQL:
            return sql()
