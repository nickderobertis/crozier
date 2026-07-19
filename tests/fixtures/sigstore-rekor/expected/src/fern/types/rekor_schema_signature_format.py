

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RekorSchemaSignatureFormat(enum.StrEnum):
    """
    Specifies the format of the signature
    """

    PGP = "pgp"
    MINISIGN = "minisign"
    X509 = "x509"
    SSH = "ssh"

    def visit(
        self,
        pgp: typing.Callable[[], T_Result],
        minisign: typing.Callable[[], T_Result],
        x509: typing.Callable[[], T_Result],
        ssh: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RekorSchemaSignatureFormat.PGP:
            return pgp()
        if self is RekorSchemaSignatureFormat.MINISIGN:
            return minisign()
        if self is RekorSchemaSignatureFormat.X509:
            return x509()
        if self is RekorSchemaSignatureFormat.SSH:
            return ssh()
