

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPlaylistByIdRequestType(enum.StrEnum):
    EPISODE_LIST = "episode_list"
    PODCAST_LIST = "podcast_list"

    def visit(
        self, episode_list: typing.Callable[[], T_Result], podcast_list: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetPlaylistByIdRequestType.EPISODE_LIST:
            return episode_list()
        if self is GetPlaylistByIdRequestType.PODCAST_LIST:
            return podcast_list()
