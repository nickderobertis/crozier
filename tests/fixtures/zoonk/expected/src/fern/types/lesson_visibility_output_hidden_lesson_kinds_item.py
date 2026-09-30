

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LessonVisibilityOutputHiddenLessonKindsItem(enum.StrEnum):
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
        if self is LessonVisibilityOutputHiddenLessonKindsItem.ALPHABET:
            return alphabet()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.CUSTOM:
            return custom()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.EXPLANATION:
            return explanation()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.GRAMMAR:
            return grammar()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.LISTENING:
            return listening()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.PRACTICE:
            return practice()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.QUIZ:
            return quiz()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.READING:
            return reading()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.REVIEW:
            return review()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.TRANSLATION:
            return translation()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.TUTORIAL:
            return tutorial()
        if self is LessonVisibilityOutputHiddenLessonKindsItem.VOCABULARY:
            return vocabulary()
