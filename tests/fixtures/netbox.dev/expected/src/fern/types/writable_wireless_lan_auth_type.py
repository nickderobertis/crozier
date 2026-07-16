

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableWirelessLanAuthType(enum.StrEnum):
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
        if self is WritableWirelessLanAuthType.OPEN:
            return open()
        if self is WritableWirelessLanAuthType.WEP:
            return wep()
        if self is WritableWirelessLanAuthType.WPA_PERSONAL:
            return wpa_personal()
        if self is WritableWirelessLanAuthType.WPA_ENTERPRISE:
            return wpa_enterprise()
