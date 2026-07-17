

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WirelessLanAuthCipherLabel(enum.StrEnum):
    AUTO = "Auto"
    TKIP = "TKIP"
    AES = "AES"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        tkip: typing.Callable[[], T_Result],
        aes: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WirelessLanAuthCipherLabel.AUTO:
            return auto()
        if self is WirelessLanAuthCipherLabel.TKIP:
            return tkip()
        if self is WirelessLanAuthCipherLabel.AES:
            return aes()
