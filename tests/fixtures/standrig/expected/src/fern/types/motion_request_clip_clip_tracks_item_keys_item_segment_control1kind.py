

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MotionRequestClipClipTracksItemKeysItemSegmentControl1Kind(enum.StrEnum):
    BEZIER = "bezier"

    def visit(self, bezier: typing.Callable[[], T_Result]) -> T_Result:
        if self is MotionRequestClipClipTracksItemKeysItemSegmentControl1Kind.BEZIER:
            return bezier()
