

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SoftwareStatementCertificationStatus(enum.StrEnum):
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
        if self is SoftwareStatementCertificationStatus.AWAITING_CERTIFICATION:
            return awaiting_certification()
        if self is SoftwareStatementCertificationStatus.CERTIFIED:
            return certified()
        if self is SoftwareStatementCertificationStatus.DEPRECATED:
            return deprecated()
        if self is SoftwareStatementCertificationStatus.REJECTED:
            return rejected()
        if self is SoftwareStatementCertificationStatus.SELF_CERTIFIED:
            return self_certified()
