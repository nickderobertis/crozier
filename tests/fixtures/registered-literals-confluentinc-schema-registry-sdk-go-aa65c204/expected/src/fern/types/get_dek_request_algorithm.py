

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDekRequestAlgorithm(enum.StrEnum):
    AES128GCM = "AES128_GCM"
    AES256GCM = "AES256_GCM"
    AES256SIV = "AES256_SIV"

    def visit(
        self,
        aes128gcm: typing.Callable[[], T_Result],
        aes256gcm: typing.Callable[[], T_Result],
        aes256siv: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDekRequestAlgorithm.AES128GCM:
            return aes128gcm()
        if self is GetDekRequestAlgorithm.AES256GCM:
            return aes256gcm()
        if self is GetDekRequestAlgorithm.AES256SIV:
            return aes256siv()
