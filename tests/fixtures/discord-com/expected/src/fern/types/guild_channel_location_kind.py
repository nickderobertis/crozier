

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GuildChannelLocationKind(enum.StrEnum):
    GC = "gc"

    def visit(self, gc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GuildChannelLocationKind.GC:
            return gc()
