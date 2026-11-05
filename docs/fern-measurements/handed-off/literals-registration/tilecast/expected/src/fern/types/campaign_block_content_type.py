

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CampaignBlockContentType(enum.StrEnum):
    PLAYLIST = "playlist"
    LAYOUT = "layout"

    def visit(self, playlist: typing.Callable[[], T_Result], layout: typing.Callable[[], T_Result]) -> T_Result:
        if self is CampaignBlockContentType.PLAYLIST:
            return playlist()
        if self is CampaignBlockContentType.LAYOUT:
            return layout()
