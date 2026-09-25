

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemSevenOp(enum.StrEnum):
    PEER_REMOVE = "peer_remove"

    def visit(self, peer_remove: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemSevenOp.PEER_REMOVE:
            return peer_remove()
