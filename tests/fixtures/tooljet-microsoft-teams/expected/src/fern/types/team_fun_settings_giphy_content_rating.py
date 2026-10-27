

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TeamFunSettingsGiphyContentRating(enum.StrEnum):
    MODERATE = "moderate"
    STRICT = "strict"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

    def visit(
        self,
        moderate: typing.Callable[[], T_Result],
        strict: typing.Callable[[], T_Result],
        unknown_future_value: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TeamFunSettingsGiphyContentRating.MODERATE:
            return moderate()
        if self is TeamFunSettingsGiphyContentRating.STRICT:
            return strict()
        if self is TeamFunSettingsGiphyContentRating.UNKNOWN_FUTURE_VALUE:
            return unknown_future_value()
