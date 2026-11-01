

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CertificateRenewalStatusOutcome(enum.StrEnum):
    """
    Whether a successful cycle renewed certificates or found no certificates due.
    """

    UNCHANGED = "unchanged"
    RENEWED = "renewed"

    def visit(self, unchanged: typing.Callable[[], T_Result], renewed: typing.Callable[[], T_Result]) -> T_Result:
        if self is CertificateRenewalStatusOutcome.UNCHANGED:
            return unchanged()
        if self is CertificateRenewalStatusOutcome.RENEWED:
            return renewed()
