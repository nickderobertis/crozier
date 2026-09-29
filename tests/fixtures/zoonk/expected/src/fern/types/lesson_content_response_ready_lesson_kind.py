

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LessonContentResponseReadyLessonKind(enum.StrEnum):
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
        if self is LessonContentResponseReadyLessonKind.ALPHABET:
            return alphabet()
        if self is LessonContentResponseReadyLessonKind.CUSTOM:
            return custom()
        if self is LessonContentResponseReadyLessonKind.EXPLANATION:
            return explanation()
        if self is LessonContentResponseReadyLessonKind.GRAMMAR:
            return grammar()
        if self is LessonContentResponseReadyLessonKind.LISTENING:
            return listening()
        if self is LessonContentResponseReadyLessonKind.PRACTICE:
            return practice()
        if self is LessonContentResponseReadyLessonKind.QUIZ:
            return quiz()
        if self is LessonContentResponseReadyLessonKind.READING:
            return reading()
        if self is LessonContentResponseReadyLessonKind.REVIEW:
            return review()
        if self is LessonContentResponseReadyLessonKind.TRANSLATION:
            return translation()
        if self is LessonContentResponseReadyLessonKind.TUTORIAL:
            return tutorial()
        if self is LessonContentResponseReadyLessonKind.VOCABULARY:
            return vocabulary()
