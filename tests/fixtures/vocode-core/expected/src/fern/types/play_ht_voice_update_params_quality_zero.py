

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlayHtVoiceUpdateParamsQualityZero(enum.StrEnum):
    FASTER = "faster"
    DRAFT = "draft"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    PREMIUM = "premium"

    def visit(
        self,
        faster: typing.Callable[[], T_Result],
        draft: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        premium: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlayHtVoiceUpdateParamsQualityZero.FASTER:
            return faster()
        if self is PlayHtVoiceUpdateParamsQualityZero.DRAFT:
            return draft()
        if self is PlayHtVoiceUpdateParamsQualityZero.LOW:
            return low()
        if self is PlayHtVoiceUpdateParamsQualityZero.MEDIUM:
            return medium()
        if self is PlayHtVoiceUpdateParamsQualityZero.HIGH:
            return high()
        if self is PlayHtVoiceUpdateParamsQualityZero.PREMIUM:
            return premium()
