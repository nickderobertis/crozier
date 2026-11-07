

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ControlCastingDeviceRequestCommand(enum.StrEnum):
    PLAY = "play"
    PAUSE = "pause"
    STOP = "stop"

    def visit(
        self,
        play: typing.Callable[[], T_Result],
        pause: typing.Callable[[], T_Result],
        stop: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ControlCastingDeviceRequestCommand.PLAY:
            return play()
        if self is ControlCastingDeviceRequestCommand.PAUSE:
            return pause()
        if self is ControlCastingDeviceRequestCommand.STOP:
            return stop()
