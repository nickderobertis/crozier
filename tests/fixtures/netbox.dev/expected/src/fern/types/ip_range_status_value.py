

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IpRangeStatusValue(str, enum.Enum):
    ACTIVE = "active"
    RESERVED = "reserved"
    DEPRECATED = "deprecated"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IpRangeStatusValue.ACTIVE:
            return active()
        if self is IpRangeStatusValue.RESERVED:
            return reserved()
        if self is IpRangeStatusValue.DEPRECATED:
            return deprecated()
