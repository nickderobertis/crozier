

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DefaultVoiceIdsOne(enum.StrEnum):
    ALLOY = "alloy"
    ECHO = "echo"

    def visit(self, alloy: typing.Callable[[], T_Result], echo: typing.Callable[[], T_Result]) -> T_Result:
        if self is DefaultVoiceIdsOne.ALLOY:
            return alloy()
        if self is DefaultVoiceIdsOne.ECHO:
            return echo()
