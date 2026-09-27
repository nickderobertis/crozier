

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindZero(enum.StrEnum):
    LINEAR = "linear"

    def visit(self, linear: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindZero.LINEAR:
            return linear()
