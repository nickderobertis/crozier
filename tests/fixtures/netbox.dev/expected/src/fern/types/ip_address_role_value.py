

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IpAddressRoleValue(str, enum.Enum):
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
        if self is IpAddressRoleValue.LOOPBACK:
            return loopback()
        if self is IpAddressRoleValue.SECONDARY:
            return secondary()
        if self is IpAddressRoleValue.ANYCAST:
            return anycast()
        if self is IpAddressRoleValue.VIP:
            return vip()
        if self is IpAddressRoleValue.VRRP:
            return vrrp()
        if self is IpAddressRoleValue.HSRP:
            return hsrp()
        if self is IpAddressRoleValue.GLBP:
            return glbp()
        if self is IpAddressRoleValue.CARP:
            return carp()
