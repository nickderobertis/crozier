

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteDekVersionRequestAlgorithm(enum.StrEnum):
    AES128GCM = "AES128_GCM"
    AES256GCM = "AES256_GCM"
    AES256SIV = "AES256_SIV"

    def visit(
        self,
        aes128gcm: typing.Callable[[], T_Result],
        aes256gcm: typing.Callable[[], T_Result],
        aes256siv: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeleteDekVersionRequestAlgorithm.AES128GCM:
            return aes128gcm()
        if self is DeleteDekVersionRequestAlgorithm.AES256GCM:
            return aes256gcm()
        if self is DeleteDekVersionRequestAlgorithm.AES256SIV:
            return aes256siv()
