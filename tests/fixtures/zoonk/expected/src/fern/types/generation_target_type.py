

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GenerationTargetType(enum.StrEnum):
    """
    Resource type to generate
    """

    COURSE_PROMPT = "coursePrompt"
    CHAPTER = "chapter"
    LESSON = "lesson"

    def visit(
        self,
        course_prompt: typing.Callable[[], T_Result],
        chapter: typing.Callable[[], T_Result],
        lesson: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GenerationTargetType.COURSE_PROMPT:
            return course_prompt()
        if self is GenerationTargetType.CHAPTER:
            return chapter()
        if self is GenerationTargetType.LESSON:
            return lesson()
