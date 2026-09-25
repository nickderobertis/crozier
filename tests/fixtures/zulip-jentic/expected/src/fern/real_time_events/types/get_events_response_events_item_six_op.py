

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemSixOp(enum.StrEnum):
    PEER_ADD = "peer_add"

    def visit(self, peer_add: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemSixOp.PEER_ADD:
            return peer_add()
