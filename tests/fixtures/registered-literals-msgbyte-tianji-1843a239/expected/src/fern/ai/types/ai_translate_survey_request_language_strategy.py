

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AiTranslateSurveyRequestLanguageStrategy(enum.StrEnum):
    DEFAULT = "default"
    USER = "user"

    def visit(self, default: typing.Callable[[], T_Result], user: typing.Callable[[], T_Result]) -> T_Result:
        if self is AiTranslateSurveyRequestLanguageStrategy.DEFAULT:
            return default()
        if self is AiTranslateSurveyRequestLanguageStrategy.USER:
            return user()
