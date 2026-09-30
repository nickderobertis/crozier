

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResolveCoursePromptResponseUnsupportedIntent(enum.StrEnum):
    AMBIGUOUS = "ambiguous"
    LEARN = "learn"
    QUESTION = "question"

    def visit(
        self,
        ambiguous: typing.Callable[[], T_Result],
        learn: typing.Callable[[], T_Result],
        question: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResolveCoursePromptResponseUnsupportedIntent.AMBIGUOUS:
            return ambiguous()
        if self is ResolveCoursePromptResponseUnsupportedIntent.LEARN:
            return learn()
        if self is ResolveCoursePromptResponseUnsupportedIntent.QUESTION:
            return question()
