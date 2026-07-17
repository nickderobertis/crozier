

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FilterType(enum.StrEnum):
    """
    Definition of filter type: per FLOW or PACKET
    """

    FLOW = "FLOW"
    PACKET = "PACKET"

    def visit(self, flow: typing.Callable[[], T_Result], packet: typing.Callable[[], T_Result]) -> T_Result:
        if self is FilterType.FLOW:
            return flow()
        if self is FilterType.PACKET:
            return packet()
