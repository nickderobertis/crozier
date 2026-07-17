

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WirelessLinkAuthCipherLabel(enum.StrEnum):
    AUTO = "Auto"
    TKIP = "TKIP"
    AES = "AES"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        tkip: typing.Callable[[], T_Result],
        aes: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WirelessLinkAuthCipherLabel.AUTO:
            return auto()
        if self is WirelessLinkAuthCipherLabel.TKIP:
            return tkip()
        if self is WirelessLinkAuthCipherLabel.AES:
            return aes()
