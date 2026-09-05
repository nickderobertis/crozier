

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPodcastByIdRequestSort(enum.StrEnum):
    RECENT_FIRST = "recent_first"
    OLDEST_FIRST = "oldest_first"

    def visit(
        self, recent_first: typing.Callable[[], T_Result], oldest_first: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetPodcastByIdRequestSort.RECENT_FIRST:
            return recent_first()
        if self is GetPodcastByIdRequestSort.OLDEST_FIRST:
            return oldest_first()
