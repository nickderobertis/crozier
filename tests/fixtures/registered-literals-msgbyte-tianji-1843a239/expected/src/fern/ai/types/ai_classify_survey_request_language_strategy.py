

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AiClassifySurveyRequestLanguageStrategy(enum.StrEnum):
    DEFAULT = "default"
    USER = "user"

    def visit(self, default: typing.Callable[[], T_Result], user: typing.Callable[[], T_Result]) -> T_Result:
        if self is AiClassifySurveyRequestLanguageStrategy.DEFAULT:
            return default()
        if self is AiClassifySurveyRequestLanguageStrategy.USER:
            return user()
