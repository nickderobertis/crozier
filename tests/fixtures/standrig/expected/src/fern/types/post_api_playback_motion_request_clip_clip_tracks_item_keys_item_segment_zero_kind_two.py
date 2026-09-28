

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindTwo(enum.StrEnum):
    INVERSE_HOLD = "inverse-hold"

    def visit(self, inverse_hold: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindTwo.INVERSE_HOLD:
            return inverse_hold()
