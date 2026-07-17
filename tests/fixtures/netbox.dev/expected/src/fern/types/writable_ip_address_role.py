

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableIpAddressRole(enum.StrEnum):
    """
    The functional role of this IP
    """

    LOOPBACK = "loopback"
    SECONDARY = "secondary"
    ANYCAST = "anycast"
    VIP = "vip"
    VRRP = "vrrp"
    HSRP = "hsrp"
    GLBP = "glbp"
    CARP = "carp"

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
        if self is WritableIpAddressRole.LOOPBACK:
            return loopback()
        if self is WritableIpAddressRole.SECONDARY:
            return secondary()
        if self is WritableIpAddressRole.ANYCAST:
            return anycast()
        if self is WritableIpAddressRole.VIP:
            return vip()
        if self is WritableIpAddressRole.VRRP:
            return vrrp()
        if self is WritableIpAddressRole.HSRP:
            return hsrp()
        if self is WritableIpAddressRole.GLBP:
            return glbp()
        if self is WritableIpAddressRole.CARP:
            return carp()
