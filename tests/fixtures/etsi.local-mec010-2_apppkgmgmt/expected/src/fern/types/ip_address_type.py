

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IpAddressType(enum.StrEnum):
    """
    Specifies the IP address type
    """

    IP_V6 = "IP_V6"
    IP_V4 = "IP_V4"

    def visit(self, ip_v6: typing.Callable[[], T_Result], ip_v4: typing.Callable[[], T_Result]) -> T_Result:
        if self is IpAddressType.IP_V6:
            return ip_v6()
        if self is IpAddressType.IP_V4:
            return ip_v4()
