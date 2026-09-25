

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbedAudioBlockGroupType(enum.StrEnum):
    EMBED_AUDIO = "EMBED_AUDIO"

    def visit(self, embed_audio: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmbedAudioBlockGroupType.EMBED_AUDIO:
            return embed_audio()
