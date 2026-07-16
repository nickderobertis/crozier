

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WirelessLanAuthCipherValue(str, enum.Enum):
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
