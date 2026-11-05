

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RollbackPublicationRequestType(enum.StrEnum):
    PLAYLIST = "playlist"
    LAYOUT = "layout"
    CAMPAIGN = "campaign"

    def visit(
        self,
        playlist: typing.Callable[[], T_Result],
        layout: typing.Callable[[], T_Result],
        campaign: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RollbackPublicationRequestType.PLAYLIST:
            return playlist()
        if self is RollbackPublicationRequestType.LAYOUT:
            return layout()
        if self is RollbackPublicationRequestType.CAMPAIGN:
            return campaign()
