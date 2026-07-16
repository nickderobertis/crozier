

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceCodeStatus(str, enum.Enum):
    """
    DeviceCode.Status enum.
    """

    UNKNOWN = "UNKNOWN"
    UNPAIRED = "UNPAIRED"
    PAIRED = "PAIRED"
    EXPIRED = "EXPIRED"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        unpaired: typing.Callable[[], T_Result],
        paired: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeviceCodeStatus.UNKNOWN:
            return unknown()
        if self is DeviceCodeStatus.UNPAIRED:
            return unpaired()
        if self is DeviceCodeStatus.PAIRED:
            return paired()
        if self is DeviceCodeStatus.EXPIRED:
            return expired()
