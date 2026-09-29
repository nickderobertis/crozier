

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CourseContinuationReadyLessonKind(enum.StrEnum):
    ALPHABET = "alphabet"
    CUSTOM = "custom"
    EXPLANATION = "explanation"
    GRAMMAR = "grammar"
    LISTENING = "listening"
    PRACTICE = "practice"
    QUIZ = "quiz"
    READING = "reading"
    REVIEW = "review"
    TRANSLATION = "translation"
    TUTORIAL = "tutorial"
    VOCABULARY = "vocabulary"

    def visit(
        self,
        alphabet: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
        explanation: typing.Callable[[], T_Result],
        grammar: typing.Callable[[], T_Result],
        listening: typing.Callable[[], T_Result],
        practice: typing.Callable[[], T_Result],
        quiz: typing.Callable[[], T_Result],
        reading: typing.Callable[[], T_Result],
        review: typing.Callable[[], T_Result],
        translation: typing.Callable[[], T_Result],
        tutorial: typing.Callable[[], T_Result],
        vocabulary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CourseContinuationReadyLessonKind.ALPHABET:
            return alphabet()
        if self is CourseContinuationReadyLessonKind.CUSTOM:
            return custom()
        if self is CourseContinuationReadyLessonKind.EXPLANATION:
            return explanation()
        if self is CourseContinuationReadyLessonKind.GRAMMAR:
            return grammar()
        if self is CourseContinuationReadyLessonKind.LISTENING:
            return listening()
        if self is CourseContinuationReadyLessonKind.PRACTICE:
            return practice()
        if self is CourseContinuationReadyLessonKind.QUIZ:
            return quiz()
        if self is CourseContinuationReadyLessonKind.READING:
            return reading()
        if self is CourseContinuationReadyLessonKind.REVIEW:
            return review()
        if self is CourseContinuationReadyLessonKind.TRANSLATION:
            return translation()
        if self is CourseContinuationReadyLessonKind.TUTORIAL:
            return tutorial()
        if self is CourseContinuationReadyLessonKind.VOCABULARY:
            return vocabulary()
