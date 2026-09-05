

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorisationServerCertificationStatus(enum.StrEnum):
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
        if self is AuthorisationServerCertificationStatus.AWAITING_CERTIFICATION:
            return awaiting_certification()
        if self is AuthorisationServerCertificationStatus.CERTIFIED:
            return certified()
        if self is AuthorisationServerCertificationStatus.DEPRECATED:
            return deprecated()
        if self is AuthorisationServerCertificationStatus.REJECTED:
            return rejected()
        if self is AuthorisationServerCertificationStatus.SELF_CERTIFIED:
            return self_certified()
