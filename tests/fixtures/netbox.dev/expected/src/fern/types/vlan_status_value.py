

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VlanStatusValue(str, enum.Enum):
    ACTIVE = "active"
    RESERVED = "reserved"
    DEPRECATED = "deprecated"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VlanStatusValue.ACTIVE:
            return active()
        if self is VlanStatusValue.RESERVED:
            return reserved()
        if self is VlanStatusValue.DEPRECATED:
            return deprecated()
