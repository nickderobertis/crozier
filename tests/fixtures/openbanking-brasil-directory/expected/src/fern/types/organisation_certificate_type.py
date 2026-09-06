

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganisationCertificateType(enum.StrEnum):
    QWAC = "qwac"
    QSEAL = "qseal"
    RTSWAC = "rtswac"
    RTSSEAL = "rtsseal"
    BRSEAL = "brseal"
    BRSEAL_EXT = "brseal_ext"
    RTSTRANSPORT_RS = "rtstransport_rs"

    def visit(
        self,
        qwac: typing.Callable[[], T_Result],
        qseal: typing.Callable[[], T_Result],
        rtswac: typing.Callable[[], T_Result],
        rtsseal: typing.Callable[[], T_Result],
        brseal: typing.Callable[[], T_Result],
        brseal_ext: typing.Callable[[], T_Result],
        rtstransport_rs: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrganisationCertificateType.QWAC:
            return qwac()
        if self is OrganisationCertificateType.QSEAL:
            return qseal()
        if self is OrganisationCertificateType.RTSWAC:
            return rtswac()
        if self is OrganisationCertificateType.RTSSEAL:
            return rtsseal()
        if self is OrganisationCertificateType.BRSEAL:
            return brseal()
        if self is OrganisationCertificateType.BRSEAL_EXT:
            return brseal_ext()
        if self is OrganisationCertificateType.RTSTRANSPORT_RS:
            return rtstransport_rs()
