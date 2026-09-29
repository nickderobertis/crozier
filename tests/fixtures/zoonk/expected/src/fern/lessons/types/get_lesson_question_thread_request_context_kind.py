

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetLessonQuestionThreadRequestContextKind(enum.StrEnum):
    """
    Filter by context kind; use lesson for the completion conversation
    """

    LESSON = "lesson"
    STEP = "step"
    ANSWER = "answer"

    def visit(
        self,
        lesson: typing.Callable[[], T_Result],
        step: typing.Callable[[], T_Result],
        answer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetLessonQuestionThreadRequestContextKind.LESSON:
            return lesson()
        if self is GetLessonQuestionThreadRequestContextKind.STEP:
            return step()
        if self is GetLessonQuestionThreadRequestContextKind.ANSWER:
            return answer()
