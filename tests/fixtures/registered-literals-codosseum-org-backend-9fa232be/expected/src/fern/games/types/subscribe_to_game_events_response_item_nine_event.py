

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemNineEvent(enum.StrEnum):
    SYNC = "sync"

    def visit(self, sync: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemNineEvent.SYNC:
            return sync()
