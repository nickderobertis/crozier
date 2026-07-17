

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WirelessLinkAuthTypeLabel(enum.StrEnum):
    OPEN = "Open"
    WEP = "WEP"
    WPA_PERSONAL_PSK = "WPA Personal (PSK)"
    WPA_ENTERPRISE = "WPA Enterprise"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        wep: typing.Callable[[], T_Result],
        wpa_personal_psk: typing.Callable[[], T_Result],
        wpa_enterprise: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WirelessLinkAuthTypeLabel.OPEN:
            return open()
        if self is WirelessLinkAuthTypeLabel.WEP:
            return wep()
        if self is WirelessLinkAuthTypeLabel.WPA_PERSONAL_PSK:
            return wpa_personal_psk()
        if self is WirelessLinkAuthTypeLabel.WPA_ENTERPRISE:
            return wpa_enterprise()
