

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SoftwareStatementCertificationRequestStatus(enum.StrEnum):
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
        if self is SoftwareStatementCertificationRequestStatus.AWAITING_CERTIFICATION:
            return awaiting_certification()
        if self is SoftwareStatementCertificationRequestStatus.CERTIFIED:
            return certified()
        if self is SoftwareStatementCertificationRequestStatus.DEPRECATED:
            return deprecated()
        if self is SoftwareStatementCertificationRequestStatus.REJECTED:
            return rejected()
        if self is SoftwareStatementCertificationRequestStatus.SELF_CERTIFIED:
            return self_certified()
