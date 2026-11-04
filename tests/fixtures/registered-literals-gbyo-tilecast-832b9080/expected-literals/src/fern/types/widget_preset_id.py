

import typing

WidgetPresetId = typing.Union[
    typing.Literal["leaderboard", "status_board", "queue_board", "schedule_departures", "opening_hours", "directory"],
    typing.Any,
]
