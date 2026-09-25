

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbedBlockGroupType(enum.StrEnum):
    EMBED = "EMBED"

    def visit(self, embed: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmbedBlockGroupType.EMBED:
            return embed()
