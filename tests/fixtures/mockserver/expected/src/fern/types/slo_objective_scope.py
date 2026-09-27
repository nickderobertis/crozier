

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SloObjectiveScope(enum.StrEnum):
    """
    which recorded traffic to evaluate; v1 records only FORWARD (proxied/forwarded upstream) samples
    """

    FORWARD = "FORWARD"
    INBOUND = "INBOUND"

    def visit(self, forward: typing.Callable[[], T_Result], inbound: typing.Callable[[], T_Result]) -> T_Result:
        if self is SloObjectiveScope.FORWARD:
            return forward()
        if self is SloObjectiveScope.INBOUND:
            return inbound()
