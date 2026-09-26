

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RoomStatus(enum.StrEnum):
    WAITING = "waiting"
    PLAYING = "playing"
    FINISHED = "finished"

    def visit(
        self,
        waiting: typing.Callable[[], T_Result],
        playing: typing.Callable[[], T_Result],
        finished: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RoomStatus.WAITING:
            return waiting()
        if self is RoomStatus.PLAYING:
            return playing()
        if self is RoomStatus.FINISHED:
            return finished()
