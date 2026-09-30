

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LessonVisibilityHiddenLessonKindsItem(enum.StrEnum):
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
        if self is LessonVisibilityHiddenLessonKindsItem.ALPHABET:
            return alphabet()
        if self is LessonVisibilityHiddenLessonKindsItem.CUSTOM:
            return custom()
        if self is LessonVisibilityHiddenLessonKindsItem.EXPLANATION:
            return explanation()
        if self is LessonVisibilityHiddenLessonKindsItem.GRAMMAR:
            return grammar()
        if self is LessonVisibilityHiddenLessonKindsItem.LISTENING:
            return listening()
        if self is LessonVisibilityHiddenLessonKindsItem.PRACTICE:
            return practice()
        if self is LessonVisibilityHiddenLessonKindsItem.QUIZ:
            return quiz()
        if self is LessonVisibilityHiddenLessonKindsItem.READING:
            return reading()
        if self is LessonVisibilityHiddenLessonKindsItem.REVIEW:
            return review()
        if self is LessonVisibilityHiddenLessonKindsItem.TRANSLATION:
            return translation()
        if self is LessonVisibilityHiddenLessonKindsItem.TUTORIAL:
            return tutorial()
        if self is LessonVisibilityHiddenLessonKindsItem.VOCABULARY:
            return vocabulary()
