

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IpAddressStatusValue(str, enum.Enum):
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
        if self is IpAddressStatusValue.ACTIVE:
            return active()
        if self is IpAddressStatusValue.RESERVED:
            return reserved()
        if self is IpAddressStatusValue.DEPRECATED:
            return deprecated()
        if self is IpAddressStatusValue.DHCP:
            return dhcp()
        if self is IpAddressStatusValue.SLAAC:
            return slaac()
