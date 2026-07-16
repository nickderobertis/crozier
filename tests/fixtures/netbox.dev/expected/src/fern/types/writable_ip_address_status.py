

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableIpAddressStatus(str, enum.Enum):
    """
    The operational status of this IP
    """

    ACTIVE = "active"
    RESERVED = "reserved"
    DEPRECATED = "deprecated"
    DHCP = "dhcp"
    SLAAC = "slaac"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
        dhcp: typing.Callable[[], T_Result],
        slaac: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableIpAddressStatus.ACTIVE:
            return active()
        if self is WritableIpAddressStatus.RESERVED:
            return reserved()
        if self is WritableIpAddressStatus.DEPRECATED:
            return deprecated()
        if self is WritableIpAddressStatus.DHCP:
            return dhcp()
        if self is WritableIpAddressStatus.SLAAC:
            return slaac()
