

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LessonResourceKind(enum.StrEnum):
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
        if self is LessonResourceKind.ALPHABET:
            return alphabet()
        if self is LessonResourceKind.CUSTOM:
            return custom()
        if self is LessonResourceKind.EXPLANATION:
            return explanation()
        if self is LessonResourceKind.GRAMMAR:
            return grammar()
        if self is LessonResourceKind.LISTENING:
            return listening()
        if self is LessonResourceKind.PRACTICE:
            return practice()
        if self is LessonResourceKind.QUIZ:
            return quiz()
        if self is LessonResourceKind.READING:
            return reading()
        if self is LessonResourceKind.REVIEW:
            return review()
        if self is LessonResourceKind.TRANSLATION:
            return translation()
        if self is LessonResourceKind.TUTORIAL:
            return tutorial()
        if self is LessonResourceKind.VOCABULARY:
            return vocabulary()
