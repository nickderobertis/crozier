

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlayHtVoiceQuality(enum.StrEnum):
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
        if self is PlayHtVoiceQuality.FASTER:
            return faster()
        if self is PlayHtVoiceQuality.DRAFT:
            return draft()
        if self is PlayHtVoiceQuality.LOW:
            return low()
        if self is PlayHtVoiceQuality.MEDIUM:
            return medium()
        if self is PlayHtVoiceQuality.HIGH:
            return high()
        if self is PlayHtVoiceQuality.PREMIUM:
            return premium()
