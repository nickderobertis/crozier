

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IpRangeStatusLabel(str, enum.Enum):
    ACTIVE = "Active"
    RESERVED = "Reserved"
    DEPRECATED = "Deprecated"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IpRangeStatusLabel.ACTIVE:
            return active()
        if self is IpRangeStatusLabel.RESERVED:
            return reserved()
        if self is IpRangeStatusLabel.DEPRECATED:
            return deprecated()
