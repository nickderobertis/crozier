

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableIpRangeStatus(str, enum.Enum):
    """
    Operational status of this range
    """

    ACTIVE = "active"
    RESERVED = "reserved"
    DEPRECATED = "deprecated"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableIpRangeStatus.ACTIVE:
            return active()
        if self is WritableIpRangeStatus.RESERVED:
            return reserved()
        if self is WritableIpRangeStatus.DEPRECATED:
            return deprecated()
