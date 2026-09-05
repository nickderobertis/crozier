

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPlaylistByIdRequestSort(enum.StrEnum):
    RECENT_ADDED_FIRST = "recent_added_first"
    OLDEST_ADDED_FIRST = "oldest_added_first"
    RECENT_PUBLISHED_FIRST = "recent_published_first"
    OLDEST_PUBLISHED_FIRST = "oldest_published_first"

    def visit(
        self,
        recent_added_first: typing.Callable[[], T_Result],
        oldest_added_first: typing.Callable[[], T_Result],
        recent_published_first: typing.Callable[[], T_Result],
        oldest_published_first: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetPlaylistByIdRequestSort.RECENT_ADDED_FIRST:
            return recent_added_first()
        if self is GetPlaylistByIdRequestSort.OLDEST_ADDED_FIRST:
            return oldest_added_first()
        if self is GetPlaylistByIdRequestSort.RECENT_PUBLISHED_FIRST:
            return recent_published_first()
        if self is GetPlaylistByIdRequestSort.OLDEST_PUBLISHED_FIRST:
            return oldest_published_first()
