

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowDirection(enum.StrEnum):
    """
    Enum for the flow direction
    """

    UNKNOWN = "unknown"
    UPSTREAM = "upstream"
    DOWNSTREAM = "downstream"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        upstream: typing.Callable[[], T_Result],
        downstream: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FlowDirection.UNKNOWN:
            return unknown()
        if self is FlowDirection.UPSTREAM:
            return upstream()
        if self is FlowDirection.DOWNSTREAM:
            return downstream()
