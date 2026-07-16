

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RackStatusLabel(str, enum.Enum):
    RESERVED = "Reserved"
    AVAILABLE = "Available"
    PLANNED = "Planned"
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"

    def visit(
        self,
        reserved: typing.Callable[[], T_Result],
        available: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RackStatusLabel.RESERVED:
            return reserved()
        if self is RackStatusLabel.AVAILABLE:
            return available()
        if self is RackStatusLabel.PLANNED:
            return planned()
        if self is RackStatusLabel.ACTIVE:
            return active()
        if self is RackStatusLabel.DEPRECATED:
            return deprecated()
