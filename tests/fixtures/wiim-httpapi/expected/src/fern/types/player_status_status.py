

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlayerStatusStatus(enum.StrEnum):
    """
    Playback status stop: no audio selected play: playing
    audio load/loading: loading/buffering audio pause: audio
    paused
    """

    PLAY = "play"
    PAUSE = "pause"
    STOP = "stop"
    BUFFERING = "buffering"

    def visit(
        self,
        play: typing.Callable[[], T_Result],
        pause: typing.Callable[[], T_Result],
        stop: typing.Callable[[], T_Result],
        buffering: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlayerStatusStatus.PLAY:
            return play()
        if self is PlayerStatusStatus.PAUSE:
            return pause()
        if self is PlayerStatusStatus.STOP:
            return stop()
        if self is PlayerStatusStatus.BUFFERING:
            return buffering()
