

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SoftwareStatementCertificateOrKeyType(enum.StrEnum):
    RTSTRANSPORT = "rtstransport"
    RTSSIGNING = "rtssigning"
    SIGKEY = "sigkey"
    ENCKEY = "enckey"
    BRCAC = "brcac"
    BRCAC_EXT = "brcac_ext"
    BRCAC2022 = "brcac_2022"

    def visit(
        self,
        rtstransport: typing.Callable[[], T_Result],
        rtssigning: typing.Callable[[], T_Result],
        sigkey: typing.Callable[[], T_Result],
        enckey: typing.Callable[[], T_Result],
        brcac: typing.Callable[[], T_Result],
        brcac_ext: typing.Callable[[], T_Result],
        brcac2022: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SoftwareStatementCertificateOrKeyType.RTSTRANSPORT:
            return rtstransport()
        if self is SoftwareStatementCertificateOrKeyType.RTSSIGNING:
            return rtssigning()
        if self is SoftwareStatementCertificateOrKeyType.SIGKEY:
            return sigkey()
        if self is SoftwareStatementCertificateOrKeyType.ENCKEY:
            return enckey()
        if self is SoftwareStatementCertificateOrKeyType.BRCAC:
            return brcac()
        if self is SoftwareStatementCertificateOrKeyType.BRCAC_EXT:
            return brcac_ext()
        if self is SoftwareStatementCertificateOrKeyType.BRCAC2022:
            return brcac2022()
