

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CourseContinuationPendingLessonKind(enum.StrEnum):
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
        if self is CourseContinuationPendingLessonKind.ALPHABET:
            return alphabet()
        if self is CourseContinuationPendingLessonKind.CUSTOM:
            return custom()
        if self is CourseContinuationPendingLessonKind.EXPLANATION:
            return explanation()
        if self is CourseContinuationPendingLessonKind.GRAMMAR:
            return grammar()
        if self is CourseContinuationPendingLessonKind.LISTENING:
            return listening()
        if self is CourseContinuationPendingLessonKind.PRACTICE:
            return practice()
        if self is CourseContinuationPendingLessonKind.QUIZ:
            return quiz()
        if self is CourseContinuationPendingLessonKind.READING:
            return reading()
        if self is CourseContinuationPendingLessonKind.REVIEW:
            return review()
        if self is CourseContinuationPendingLessonKind.TRANSLATION:
            return translation()
        if self is CourseContinuationPendingLessonKind.TUTORIAL:
            return tutorial()
        if self is CourseContinuationPendingLessonKind.VOCABULARY:
            return vocabulary()
