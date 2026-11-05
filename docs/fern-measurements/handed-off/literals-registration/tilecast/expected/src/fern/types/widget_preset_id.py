

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WidgetPresetId(enum.StrEnum):
    LEADERBOARD = "leaderboard"
    STATUS_BOARD = "status_board"
    QUEUE_BOARD = "queue_board"
    SCHEDULE_DEPARTURES = "schedule_departures"
    OPENING_HOURS = "opening_hours"
    DIRECTORY = "directory"

    def visit(
        self,
        leaderboard: typing.Callable[[], T_Result],
        status_board: typing.Callable[[], T_Result],
        queue_board: typing.Callable[[], T_Result],
        schedule_departures: typing.Callable[[], T_Result],
        opening_hours: typing.Callable[[], T_Result],
        directory: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WidgetPresetId.LEADERBOARD:
            return leaderboard()
        if self is WidgetPresetId.STATUS_BOARD:
            return status_board()
        if self is WidgetPresetId.QUEUE_BOARD:
            return queue_board()
        if self is WidgetPresetId.SCHEDULE_DEPARTURES:
            return schedule_departures()
        if self is WidgetPresetId.OPENING_HOURS:
            return opening_hours()
        if self is WidgetPresetId.DIRECTORY:
            return directory()
