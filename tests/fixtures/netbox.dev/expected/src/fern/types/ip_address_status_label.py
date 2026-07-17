

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IpAddressStatusLabel(enum.StrEnum):
    ACTIVE = "Active"
    RESERVED = "Reserved"
    DEPRECATED = "Deprecated"
    DHCP = "DHCP"
    SLAAC = "SLAAC"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
        dhcp: typing.Callable[[], T_Result],
        slaac: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IpAddressStatusLabel.ACTIVE:
            return active()
        if self is IpAddressStatusLabel.RESERVED:
            return reserved()
        if self is IpAddressStatusLabel.DEPRECATED:
            return deprecated()
        if self is IpAddressStatusLabel.DHCP:
            return dhcp()
        if self is IpAddressStatusLabel.SLAAC:
            return slaac()
