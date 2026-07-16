

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RackStatusValue(enum.StrEnum):
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
        if self is RackStatusValue.RESERVED:
            return reserved()
        if self is RackStatusValue.AVAILABLE:
            return available()
        if self is RackStatusValue.PLANNED:
            return planned()
        if self is RackStatusValue.ACTIVE:
            return active()
        if self is RackStatusValue.DEPRECATED:
            return deprecated()
