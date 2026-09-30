

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LessonSuccessorResponseLessonLessonKind(enum.StrEnum):
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
        if self is LessonSuccessorResponseLessonLessonKind.ALPHABET:
            return alphabet()
        if self is LessonSuccessorResponseLessonLessonKind.CUSTOM:
            return custom()
        if self is LessonSuccessorResponseLessonLessonKind.EXPLANATION:
            return explanation()
        if self is LessonSuccessorResponseLessonLessonKind.GRAMMAR:
            return grammar()
        if self is LessonSuccessorResponseLessonLessonKind.LISTENING:
            return listening()
        if self is LessonSuccessorResponseLessonLessonKind.PRACTICE:
            return practice()
        if self is LessonSuccessorResponseLessonLessonKind.QUIZ:
            return quiz()
        if self is LessonSuccessorResponseLessonLessonKind.READING:
            return reading()
        if self is LessonSuccessorResponseLessonLessonKind.REVIEW:
            return review()
        if self is LessonSuccessorResponseLessonLessonKind.TRANSLATION:
            return translation()
        if self is LessonSuccessorResponseLessonLessonKind.TUTORIAL:
            return tutorial()
        if self is LessonSuccessorResponseLessonLessonKind.VOCABULARY:
            return vocabulary()
