

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataMetadataVerificationStatus(enum.StrEnum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    OUTDATED = "outdated"

    def visit(
        self,
        unverified: typing.Callable[[], T_Result],
        verified: typing.Callable[[], T_Result],
        outdated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataMetadataVerificationStatus.UNVERIFIED:
            return unverified()
        if self is DataMetadataVerificationStatus.VERIFIED:
            return verified()
        if self is DataMetadataVerificationStatus.OUTDATED:
            return outdated()
