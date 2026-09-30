

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CoursePromptGenerationResponsePendingCourseFormat(enum.StrEnum):
    CODING = "coding"
    CORE = "core"
    EXAM = "exam"
    INSTRUMENT = "instrument"
    LANGUAGE = "language"
    PERSONALIZED = "personalized"
    PRACTICAL = "practical"
    QUESTION = "question"

    def visit(
        self,
        coding: typing.Callable[[], T_Result],
        core: typing.Callable[[], T_Result],
        exam: typing.Callable[[], T_Result],
        instrument: typing.Callable[[], T_Result],
        language: typing.Callable[[], T_Result],
        personalized: typing.Callable[[], T_Result],
        practical: typing.Callable[[], T_Result],
        question: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CoursePromptGenerationResponsePendingCourseFormat.CODING:
            return coding()
        if self is CoursePromptGenerationResponsePendingCourseFormat.CORE:
            return core()
        if self is CoursePromptGenerationResponsePendingCourseFormat.EXAM:
            return exam()
        if self is CoursePromptGenerationResponsePendingCourseFormat.INSTRUMENT:
            return instrument()
        if self is CoursePromptGenerationResponsePendingCourseFormat.LANGUAGE:
            return language()
        if self is CoursePromptGenerationResponsePendingCourseFormat.PERSONALIZED:
            return personalized()
        if self is CoursePromptGenerationResponsePendingCourseFormat.PRACTICAL:
            return practical()
        if self is CoursePromptGenerationResponsePendingCourseFormat.QUESTION:
            return question()
