

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemScheduledMessageIdOp(enum.StrEnum):
    REMOVE = "remove"

    def visit(self, remove: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemScheduledMessageIdOp.REMOVE:
            return remove()
