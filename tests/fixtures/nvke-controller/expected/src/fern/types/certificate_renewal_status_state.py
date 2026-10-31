

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CertificateRenewalStatusState(enum.StrEnum):
    """
    The lifecycle state of the most recent certificate-renewal cycle.
    """

    ACCEPTED = "accepted"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(
        self,
        accepted: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CertificateRenewalStatusState.ACCEPTED:
            return accepted()
        if self is CertificateRenewalStatusState.SUCCEEDED:
            return succeeded()
        if self is CertificateRenewalStatusState.FAILED:
            return failed()
