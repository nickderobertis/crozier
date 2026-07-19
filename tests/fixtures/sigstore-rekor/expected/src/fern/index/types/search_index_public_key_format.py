

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchIndexPublicKeyFormat(enum.StrEnum):
    PGP = "pgp"
    X509 = "x509"
    MINISIGN = "minisign"
    SSH = "ssh"
    TUF = "tuf"

    def visit(
        self,
        pgp: typing.Callable[[], T_Result],
        x509: typing.Callable[[], T_Result],
        minisign: typing.Callable[[], T_Result],
        ssh: typing.Callable[[], T_Result],
        tuf: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchIndexPublicKeyFormat.PGP:
            return pgp()
        if self is SearchIndexPublicKeyFormat.X509:
            return x509()
        if self is SearchIndexPublicKeyFormat.MINISIGN:
            return minisign()
        if self is SearchIndexPublicKeyFormat.SSH:
            return ssh()
        if self is SearchIndexPublicKeyFormat.TUF:
            return tuf()
