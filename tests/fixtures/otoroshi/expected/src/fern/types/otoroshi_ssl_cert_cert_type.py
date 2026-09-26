

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtoroshiSslCertCertType(enum.StrEnum):
    """
    the kind of certificate
    """

    CLIENT = "client"
    CA = "ca"
    LETS_ENCRYPT = "letsEncrypt"
    KEYPAIR = "keypair"
    SELF_SIGNED = "selfSigned"
    CERTIFICATE = "certificate"

    def visit(
        self,
        client: typing.Callable[[], T_Result],
        ca: typing.Callable[[], T_Result],
        lets_encrypt: typing.Callable[[], T_Result],
        keypair: typing.Callable[[], T_Result],
        self_signed: typing.Callable[[], T_Result],
        certificate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OtoroshiSslCertCertType.CLIENT:
            return client()
        if self is OtoroshiSslCertCertType.CA:
            return ca()
        if self is OtoroshiSslCertCertType.LETS_ENCRYPT:
            return lets_encrypt()
        if self is OtoroshiSslCertCertType.KEYPAIR:
            return keypair()
        if self is OtoroshiSslCertCertType.SELF_SIGNED:
            return self_signed()
        if self is OtoroshiSslCertCertType.CERTIFICATE:
            return certificate()
