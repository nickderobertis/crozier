

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorisationServerCertificationRequestStatus(enum.StrEnum):
    """
    Is this certification current or expired
    """

    AWAITING_CERTIFICATION = "Awaiting Certification"
    CERTIFIED = "Certified"
    DEPRECATED = "Deprecated"
    REJECTED = "Rejected"
    SELF_CERTIFIED = "Self-Certified"

    def visit(
        self,
        awaiting_certification: typing.Callable[[], T_Result],
        certified: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        self_certified: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthorisationServerCertificationRequestStatus.AWAITING_CERTIFICATION:
            return awaiting_certification()
        if self is AuthorisationServerCertificationRequestStatus.CERTIFIED:
            return certified()
        if self is AuthorisationServerCertificationRequestStatus.DEPRECATED:
            return deprecated()
        if self is AuthorisationServerCertificationRequestStatus.REJECTED:
            return rejected()
        if self is AuthorisationServerCertificationRequestStatus.SELF_CERTIFIED:
            return self_certified()
