

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchAudioRequestCategory(enum.StrEnum):
    MUSIC = "music"
    PODCAST = "podcast"
    AUDIOBOOK = "audiobook"
    NEWS = "news"

    def visit(
        self,
        music: typing.Callable[[], T_Result],
        podcast: typing.Callable[[], T_Result],
        audiobook: typing.Callable[[], T_Result],
        news: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchAudioRequestCategory.MUSIC:
            return music()
        if self is SearchAudioRequestCategory.PODCAST:
            return podcast()
        if self is SearchAudioRequestCategory.AUDIOBOOK:
            return audiobook()
        if self is SearchAudioRequestCategory.NEWS:
            return news()
