

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableRackStatus(enum.StrEnum):
    RESERVED = "reserved"
    AVAILABLE = "available"
    PLANNED = "planned"
    ACTIVE = "active"
    DEPRECATED = "deprecated"

    def visit(
        self,
        reserved: typing.Callable[[], T_Result],
        available: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableRackStatus.RESERVED:
            return reserved()
        if self is WritableRackStatus.AVAILABLE:
            return available()
        if self is WritableRackStatus.PLANNED:
            return planned()
        if self is WritableRackStatus.ACTIVE:
            return active()
        if self is WritableRackStatus.DEPRECATED:
            return deprecated()
