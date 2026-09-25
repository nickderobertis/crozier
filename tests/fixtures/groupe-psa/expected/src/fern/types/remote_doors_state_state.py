

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteDoorsStateState(enum.StrEnum):
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"

    def visit(self, unlocked: typing.Callable[[], T_Result], locked: typing.Callable[[], T_Result]) -> T_Result:
        if self is RemoteDoorsStateState.UNLOCKED:
            return unlocked()
        if self is RemoteDoorsStateState.LOCKED:
            return locked()
