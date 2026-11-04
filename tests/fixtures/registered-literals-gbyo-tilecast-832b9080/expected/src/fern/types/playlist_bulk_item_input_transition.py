

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaylistBulkItemInputTransition(enum.StrEnum):
    NONE = "none"
    FADE = "fade"
    CROSSFADE = "crossfade"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        fade: typing.Callable[[], T_Result],
        crossfade: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlaylistBulkItemInputTransition.NONE:
            return none()
        if self is PlaylistBulkItemInputTransition.FADE:
            return fade()
        if self is PlaylistBulkItemInputTransition.CROSSFADE:
            return crossfade()
