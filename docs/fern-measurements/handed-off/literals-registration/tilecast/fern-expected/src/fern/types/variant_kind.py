

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VariantKind(enum.StrEnum):
    ORIGINAL = "original"
    PLAYBACK = "playback"
    THUMBNAIL = "thumbnail"
    POSTER = "poster"

    def visit(
        self,
        original: typing.Callable[[], T_Result],
        playback: typing.Callable[[], T_Result],
        thumbnail: typing.Callable[[], T_Result],
        poster: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VariantKind.ORIGINAL:
            return original()
        if self is VariantKind.PLAYBACK:
            return playback()
        if self is VariantKind.THUMBNAIL:
            return thumbnail()
        if self is VariantKind.POSTER:
            return poster()
