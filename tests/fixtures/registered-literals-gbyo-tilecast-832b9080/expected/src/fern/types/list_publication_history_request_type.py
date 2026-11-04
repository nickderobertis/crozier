

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListPublicationHistoryRequestType(enum.StrEnum):
    PLAYLIST = "playlist"
    LAYOUT = "layout"
    CAMPAIGN = "campaign"

    def visit(
        self,
        playlist: typing.Callable[[], T_Result],
        layout: typing.Callable[[], T_Result],
        campaign: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListPublicationHistoryRequestType.PLAYLIST:
            return playlist()
        if self is ListPublicationHistoryRequestType.LAYOUT:
            return layout()
        if self is ListPublicationHistoryRequestType.CAMPAIGN:
            return campaign()
