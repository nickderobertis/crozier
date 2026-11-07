

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaylistItemInputTransition(enum.StrEnum):
    NONE = "none"
    FADE = "fade"
    CROSSFADE = "crossfade"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        fade: typing.Callable[[], T_Result],
        crossfade: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlaylistItemInputTransition.NONE:
            return none()
        if self is PlaylistItemInputTransition.FADE:
            return fade()
        if self is PlaylistItemInputTransition.CROSSFADE:
            return crossfade()
