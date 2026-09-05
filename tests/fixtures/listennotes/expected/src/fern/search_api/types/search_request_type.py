

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchRequestType(enum.StrEnum):
    EPISODE = "episode"
    PODCAST = "podcast"
    CURATED = "curated"

    def visit(
        self,
        episode: typing.Callable[[], T_Result],
        podcast: typing.Callable[[], T_Result],
        curated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchRequestType.EPISODE:
            return episode()
        if self is SearchRequestType.PODCAST:
            return podcast()
        if self is SearchRequestType.CURATED:
            return curated()
