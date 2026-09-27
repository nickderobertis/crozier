

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiPlaybackControlRequestCommand(enum.StrEnum):
    PLAY = "play"
    PAUSE = "pause"
    RESET = "reset"
    DEMO_START = "demo-start"
    DEMO_STOP = "demo-stop"
    DEMO_POINTER = "demo-pointer"

    def visit(
        self,
        play: typing.Callable[[], T_Result],
        pause: typing.Callable[[], T_Result],
        reset: typing.Callable[[], T_Result],
        demo_start: typing.Callable[[], T_Result],
        demo_stop: typing.Callable[[], T_Result],
        demo_pointer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostApiPlaybackControlRequestCommand.PLAY:
            return play()
        if self is PostApiPlaybackControlRequestCommand.PAUSE:
            return pause()
        if self is PostApiPlaybackControlRequestCommand.RESET:
            return reset()
        if self is PostApiPlaybackControlRequestCommand.DEMO_START:
            return demo_start()
        if self is PostApiPlaybackControlRequestCommand.DEMO_STOP:
            return demo_stop()
        if self is PostApiPlaybackControlRequestCommand.DEMO_POINTER:
            return demo_pointer()
