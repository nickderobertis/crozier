

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableWirelessLanStatus(str, enum.Enum):
    ACTIVE = "active"
    RESERVED = "reserved"
    DISABLED = "disabled"
    DEPRECATED = "deprecated"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableWirelessLanStatus.ACTIVE:
            return active()
        if self is WritableWirelessLanStatus.RESERVED:
            return reserved()
        if self is WritableWirelessLanStatus.DISABLED:
            return disabled()
        if self is WritableWirelessLanStatus.DEPRECATED:
            return deprecated()
