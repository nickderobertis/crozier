

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableWirelessLanAuthCipher(enum.StrEnum):
    AUTO = "auto"
    TKIP = "tkip"
    AES = "aes"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        tkip: typing.Callable[[], T_Result],
        aes: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableWirelessLanAuthCipher.AUTO:
            return auto()
        if self is WritableWirelessLanAuthCipher.TKIP:
            return tkip()
        if self is WritableWirelessLanAuthCipher.AES:
            return aes()
