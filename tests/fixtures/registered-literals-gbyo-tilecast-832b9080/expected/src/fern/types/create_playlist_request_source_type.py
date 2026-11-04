

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreatePlaylistRequestSourceType(enum.StrEnum):
    """
    static creates a manually ordered timeline; tag creates an initially empty tag-driven playlist
    """

    STATIC = "static"
    TAG = "tag"

    def visit(self, static: typing.Callable[[], T_Result], tag: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreatePlaylistRequestSourceType.STATIC:
            return static()
        if self is CreatePlaylistRequestSourceType.TAG:
            return tag()
