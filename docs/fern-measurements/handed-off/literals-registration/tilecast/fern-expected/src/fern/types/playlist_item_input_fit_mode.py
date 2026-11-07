

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaylistItemInputFitMode(enum.StrEnum):
    CONTAIN = "contain"
    COVER = "cover"
    STRETCH = "stretch"

    def visit(
        self,
        contain: typing.Callable[[], T_Result],
        cover: typing.Callable[[], T_Result],
        stretch: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlaylistItemInputFitMode.CONTAIN:
            return contain()
        if self is PlaylistItemInputFitMode.COVER:
            return cover()
        if self is PlaylistItemInputFitMode.STRETCH:
            return stretch()
