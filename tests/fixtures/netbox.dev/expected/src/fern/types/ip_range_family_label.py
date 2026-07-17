

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IpRangeFamilyLabel(enum.StrEnum):
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"

    def visit(self, i_pv4: typing.Callable[[], T_Result], i_pv6: typing.Callable[[], T_Result]) -> T_Result:
        if self is IpRangeFamilyLabel.I_PV4:
            return i_pv4()
        if self is IpRangeFamilyLabel.I_PV6:
            return i_pv6()
