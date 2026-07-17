

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WirelessLanAuthCipherValue(enum.StrEnum):
    AUTO = "auto"
    TKIP = "tkip"
    AES = "aes"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        tkip: typing.Callable[[], T_Result],
        aes: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WirelessLanAuthCipherValue.AUTO:
            return auto()
        if self is WirelessLanAuthCipherValue.TKIP:
            return tkip()
        if self is WirelessLanAuthCipherValue.AES:
            return aes()
