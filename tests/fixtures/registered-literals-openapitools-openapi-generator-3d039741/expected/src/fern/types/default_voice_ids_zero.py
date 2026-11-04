

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DefaultVoiceIdsZero(enum.StrEnum):
    ALLOY = "alloy"
    ASH = "ash"

    def visit(self, alloy: typing.Callable[[], T_Result], ash: typing.Callable[[], T_Result]) -> T_Result:
        if self is DefaultVoiceIdsZero.ALLOY:
            return alloy()
        if self is DefaultVoiceIdsZero.ASH:
            return ash()
