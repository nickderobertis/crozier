

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ComparePublicationsRequestType(enum.StrEnum):
    PLAYLIST = "playlist"
    LAYOUT = "layout"
    CAMPAIGN = "campaign"

    def visit(
        self,
        playlist: typing.Callable[[], T_Result],
        layout: typing.Callable[[], T_Result],
        campaign: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ComparePublicationsRequestType.PLAYLIST:
            return playlist()
        if self is ComparePublicationsRequestType.LAYOUT:
            return layout()
        if self is ComparePublicationsRequestType.CAMPAIGN:
            return campaign()
