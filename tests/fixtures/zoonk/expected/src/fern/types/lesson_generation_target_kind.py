

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LessonGenerationTargetKind(enum.StrEnum):
    LESSON = "lesson"
    SOURCE_LESSON = "sourceLesson"

    def visit(self, lesson: typing.Callable[[], T_Result], source_lesson: typing.Callable[[], T_Result]) -> T_Result:
        if self is LessonGenerationTargetKind.LESSON:
            return lesson()
        if self is LessonGenerationTargetKind.SOURCE_LESSON:
            return source_lesson()
