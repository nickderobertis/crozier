

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CoursePromptGenerationResponsePendingCompletionKind(enum.StrEnum):
    COURSE = "course"
    INTRODUCTION_LESSON = "introductionLesson"

    def visit(
        self, course: typing.Callable[[], T_Result], introduction_lesson: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CoursePromptGenerationResponsePendingCompletionKind.COURSE:
            return course()
        if self is CoursePromptGenerationResponsePendingCompletionKind.INTRODUCTION_LESSON:
            return introduction_lesson()
