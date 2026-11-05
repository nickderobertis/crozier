

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SoundTouchParametersAudioDirection(enum.StrEnum):
    """
    Media stream to be altered, incoming or outgoing
    """

    IN = "in"
    OUT = "out"

    def visit(self, in_: typing.Callable[[], T_Result], out: typing.Callable[[], T_Result]) -> T_Result:
        if self is SoundTouchParametersAudioDirection.IN:
            return in_()
        if self is SoundTouchParametersAudioDirection.OUT:
            return out()
