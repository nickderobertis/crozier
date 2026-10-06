

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AiCompletionRequestLanguage(enum.StrEnum):
    MARKDOWN = "markdown"
    PYTHON = "python"
    SQL = "sql"

    def visit(
        self,
        markdown: typing.Callable[[], T_Result],
        python: typing.Callable[[], T_Result],
        sql: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AiCompletionRequestLanguage.MARKDOWN:
            return markdown()
        if self is AiCompletionRequestLanguage.PYTHON:
            return python()
        if self is AiCompletionRequestLanguage.SQL:
            return sql()
