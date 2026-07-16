

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WirelessLinkAuthTypeValue(enum.StrEnum):
    OPEN = "open"
    WEP = "wep"
    WPA_PERSONAL = "wpa-personal"
    WPA_ENTERPRISE = "wpa-enterprise"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        wep: typing.Callable[[], T_Result],
        wpa_personal: typing.Callable[[], T_Result],
        wpa_enterprise: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WirelessLinkAuthTypeValue.OPEN:
            return open()
        if self is WirelessLinkAuthTypeValue.WEP:
            return wep()
        if self is WirelessLinkAuthTypeValue.WPA_PERSONAL:
            return wpa_personal()
        if self is WirelessLinkAuthTypeValue.WPA_ENTERPRISE:
            return wpa_enterprise()
