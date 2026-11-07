

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubmitContentDraftRequestType(enum.StrEnum):
    PLAYLIST = "playlist"
    LAYOUT = "layout"
    CAMPAIGN = "campaign"

    def visit(
        self,
        playlist: typing.Callable[[], T_Result],
        layout: typing.Callable[[], T_Result],
        campaign: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubmitContentDraftRequestType.PLAYLIST:
            return playlist()
        if self is SubmitContentDraftRequestType.LAYOUT:
            return layout()
        if self is SubmitContentDraftRequestType.CAMPAIGN:
            return campaign()
