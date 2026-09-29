

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResolveCoursePromptResponseUnsupportedCourseFormat(enum.StrEnum):
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
        if self is ResolveCoursePromptResponseUnsupportedCourseFormat.CODING:
            return coding()
        if self is ResolveCoursePromptResponseUnsupportedCourseFormat.CORE:
            return core()
        if self is ResolveCoursePromptResponseUnsupportedCourseFormat.EXAM:
            return exam()
        if self is ResolveCoursePromptResponseUnsupportedCourseFormat.INSTRUMENT:
            return instrument()
        if self is ResolveCoursePromptResponseUnsupportedCourseFormat.LANGUAGE:
            return language()
        if self is ResolveCoursePromptResponseUnsupportedCourseFormat.PERSONALIZED:
            return personalized()
        if self is ResolveCoursePromptResponseUnsupportedCourseFormat.PRACTICAL:
            return practical()
        if self is ResolveCoursePromptResponseUnsupportedCourseFormat.QUESTION:
            return question()
