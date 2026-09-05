

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaylistItemType(enum.StrEnum):
    """
    The type of this playlist item.
    If a playlist is **episode_list**, then an item could be either **episode** or **custom_audio**.
    If it's **podcast_list**, then an item can only be **podcast**.
    """

    EPISODE = "episode"
    CUSTOM_AUDIO = "custom_audio"
    PODCAST = "podcast"

    def visit(
        self,
        episode: typing.Callable[[], T_Result],
        custom_audio: typing.Callable[[], T_Result],
        podcast: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlaylistItemType.EPISODE:
            return episode()
        if self is PlaylistItemType.CUSTOM_AUDIO:
            return custom_audio()
        if self is PlaylistItemType.PODCAST:
            return podcast()
