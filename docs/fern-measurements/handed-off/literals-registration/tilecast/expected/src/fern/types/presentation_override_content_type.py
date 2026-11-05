

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PresentationOverrideContentType(enum.StrEnum):
    PLAYLIST = "playlist"
    LAYOUT = "layout"
    ASSET = "asset"

    def visit(
        self,
        playlist: typing.Callable[[], T_Result],
        layout: typing.Callable[[], T_Result],
        asset: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PresentationOverrideContentType.PLAYLIST:
            return playlist()
        if self is PresentationOverrideContentType.LAYOUT:
            return layout()
        if self is PresentationOverrideContentType.ASSET:
            return asset()
