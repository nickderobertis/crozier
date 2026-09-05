

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBestPodcastsRequestSort(enum.StrEnum):
    RECENT_ADDED_FIRST = "recent_added_first"
    OLDEST_ADDED_FIRST = "oldest_added_first"
    RECENT_PUBLISHED_FIRST = "recent_published_first"
    OLDEST_PUBLISHED_FIRST = "oldest_published_first"
    LISTEN_SCORE = "listen_score"

    def visit(
        self,
        recent_added_first: typing.Callable[[], T_Result],
        oldest_added_first: typing.Callable[[], T_Result],
        recent_published_first: typing.Callable[[], T_Result],
        oldest_published_first: typing.Callable[[], T_Result],
        listen_score: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBestPodcastsRequestSort.RECENT_ADDED_FIRST:
            return recent_added_first()
        if self is GetBestPodcastsRequestSort.OLDEST_ADDED_FIRST:
            return oldest_added_first()
        if self is GetBestPodcastsRequestSort.RECENT_PUBLISHED_FIRST:
            return recent_published_first()
        if self is GetBestPodcastsRequestSort.OLDEST_PUBLISHED_FIRST:
            return oldest_published_first()
        if self is GetBestPodcastsRequestSort.LISTEN_SCORE:
            return listen_score()
