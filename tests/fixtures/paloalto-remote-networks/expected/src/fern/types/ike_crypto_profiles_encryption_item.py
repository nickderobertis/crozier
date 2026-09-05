

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IkeCryptoProfilesEncryptionItem(enum.StrEnum):
    DES = "des"
    THREE_DES = "3des"
    AES128CBC = "aes-128-cbc"
    AES192CBC = "aes-192-cbc"
    AES256CBC = "aes-256-cbc"
    AES128GCM = "aes-128-gcm"
    AES256GCM = "aes-256-gcm"

    def visit(
        self,
        des: typing.Callable[[], T_Result],
        three_des: typing.Callable[[], T_Result],
        aes128cbc: typing.Callable[[], T_Result],
        aes192cbc: typing.Callable[[], T_Result],
        aes256cbc: typing.Callable[[], T_Result],
        aes128gcm: typing.Callable[[], T_Result],
        aes256gcm: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IkeCryptoProfilesEncryptionItem.DES:
            return des()
        if self is IkeCryptoProfilesEncryptionItem.THREE_DES:
            return three_des()
        if self is IkeCryptoProfilesEncryptionItem.AES128CBC:
            return aes128cbc()
        if self is IkeCryptoProfilesEncryptionItem.AES192CBC:
            return aes192cbc()
        if self is IkeCryptoProfilesEncryptionItem.AES256CBC:
            return aes256cbc()
        if self is IkeCryptoProfilesEncryptionItem.AES128GCM:
            return aes128gcm()
        if self is IkeCryptoProfilesEncryptionItem.AES256GCM:
            return aes256gcm()
