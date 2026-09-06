

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AmendCertificateRequestRevokeReason(enum.StrEnum):
    """
    Specify a reason for revokation of the certificate.
    """

    UNSPECIFIED = "unspecified"
    KEYCOMPROMISE = "keycompromise"
    SUPERSEDED = "superseded"
    CESSATIONOFOPERATION = "cessationofoperation"
    PRIVILEGEWITHDRAWN = "privilegewithdrawn"

    def visit(
        self,
        unspecified: typing.Callable[[], T_Result],
        keycompromise: typing.Callable[[], T_Result],
        superseded: typing.Callable[[], T_Result],
        cessationofoperation: typing.Callable[[], T_Result],
        privilegewithdrawn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AmendCertificateRequestRevokeReason.UNSPECIFIED:
            return unspecified()
        if self is AmendCertificateRequestRevokeReason.KEYCOMPROMISE:
            return keycompromise()
        if self is AmendCertificateRequestRevokeReason.SUPERSEDED:
            return superseded()
        if self is AmendCertificateRequestRevokeReason.CESSATIONOFOPERATION:
            return cessationofoperation()
        if self is AmendCertificateRequestRevokeReason.PRIVILEGEWITHDRAWN:
            return privilegewithdrawn()
