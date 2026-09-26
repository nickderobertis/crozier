

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbedVideoBlockGroupType(enum.StrEnum):
    EMBED_VIDEO = "EMBED_VIDEO"

    def visit(self, embed_video: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmbedVideoBlockGroupType.EMBED_VIDEO:
            return embed_video()
