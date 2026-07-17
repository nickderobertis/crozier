

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IpAddressRoleLabel(enum.StrEnum):
    LOOPBACK = "Loopback"
    SECONDARY = "Secondary"
    ANYCAST = "Anycast"
    VIP = "VIP"
    VRRP = "VRRP"
    HSRP = "HSRP"
    GLBP = "GLBP"
    CARP = "CARP"

    def visit(
        self,
        loopback: typing.Callable[[], T_Result],
        secondary: typing.Callable[[], T_Result],
        anycast: typing.Callable[[], T_Result],
        vip: typing.Callable[[], T_Result],
        vrrp: typing.Callable[[], T_Result],
        hsrp: typing.Callable[[], T_Result],
        glbp: typing.Callable[[], T_Result],
        carp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IpAddressRoleLabel.LOOPBACK:
            return loopback()
        if self is IpAddressRoleLabel.SECONDARY:
            return secondary()
        if self is IpAddressRoleLabel.ANYCAST:
            return anycast()
        if self is IpAddressRoleLabel.VIP:
            return vip()
        if self is IpAddressRoleLabel.VRRP:
            return vrrp()
        if self is IpAddressRoleLabel.HSRP:
            return hsrp()
        if self is IpAddressRoleLabel.GLBP:
            return glbp()
        if self is IpAddressRoleLabel.CARP:
            return carp()
