

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PresentationNetworkSecurity(enum.StrEnum):
    """
    WPA2/WPA3 Personal PSK or WPA2-Enterprise PEAP/MSCHAPv2.
    """

    WPA_PSK = "wpa_psk"
    WPA_EAP_PEAP_MSCHAPV2 = "wpa_eap_peap_mschapv2"

    def visit(
        self, wpa_psk: typing.Callable[[], T_Result], wpa_eap_peap_mschapv2: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PresentationNetworkSecurity.WPA_PSK:
            return wpa_psk()
        if self is PresentationNetworkSecurity.WPA_EAP_PEAP_MSCHAPV2:
            return wpa_eap_peap_mschapv2()
