

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaylistResponseType(enum.StrEnum):
    """
    The type of this playlist, which should be either **episode_list** or **podcast_list**.
    """

    EPISODE_LIST = "episode_list"
    PODCAST_LIST = "podcast_list"

    def visit(
        self, episode_list: typing.Callable[[], T_Result], podcast_list: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PlaylistResponseType.EPISODE_LIST:
            return episode_list()
        if self is PlaylistResponseType.PODCAST_LIST:
            return podcast_list()
