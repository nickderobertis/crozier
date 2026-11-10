

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class Sentiment(enum.StrEnum):
    POSITIVE = "POSITIVE"
    NEUTRAL = "NEUTRAL"
    NEGATIVE = "NEGATIVE"

    def visit(
        self,
        positive: typing.Callable[[], T_Result],
        neutral: typing.Callable[[], T_Result],
        negative: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Sentiment.POSITIVE:
            return positive()
        if self is Sentiment.NEUTRAL:
            return neutral()
        if self is Sentiment.NEGATIVE:
            return negative()
