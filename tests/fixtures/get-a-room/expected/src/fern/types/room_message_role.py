

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RoomMessageRole(enum.StrEnum):
    CREATOR = "creator"
    GUEST = "guest"

    def visit(self, creator: typing.Callable[[], T_Result], guest: typing.Callable[[], T_Result]) -> T_Result:
        if self is RoomMessageRole.CREATOR:
            return creator()
        if self is RoomMessageRole.GUEST:
            return guest()
