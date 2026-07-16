

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableWirelessLinkAuthCipher(str, enum.Enum):
    AUTO = "auto"
    TKIP = "tkip"
    AES = "aes"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        tkip: typing.Callable[[], T_Result],
        aes: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableWirelessLinkAuthCipher.AUTO:
            return auto()
        if self is WritableWirelessLinkAuthCipher.TKIP:
            return tkip()
        if self is WritableWirelessLinkAuthCipher.AES:
            return aes()
