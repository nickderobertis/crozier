

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VerificationStatus(enum.StrEnum):
    """
    The verification status. One of the following:

    `"VERIFIED"`: The information was successfully verified.

    `"UNVERIFIED"`: The verification has not yet been performed.

    `"NEEDS_INFO"`: The verification was attempted but could not be completed due to missing information.

    "`UNABLE_TO_VERIFY`": The verification was performed and the information could not be verified.

    `"UNKNOWN"`: The verification status is unknown.
    """

    VERIFIED = "VERIFIED"
    UNVERIFIED = "UNVERIFIED"
    NEEDS_INFO = "NEEDS_INFO"
    UNABLE_TO_VERIFY = "UNABLE_TO_VERIFY"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        verified: typing.Callable[[], T_Result],
        unverified: typing.Callable[[], T_Result],
        needs_info: typing.Callable[[], T_Result],
        unable_to_verify: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VerificationStatus.VERIFIED:
            return verified()
        if self is VerificationStatus.UNVERIFIED:
            return unverified()
        if self is VerificationStatus.NEEDS_INFO:
            return needs_info()
        if self is VerificationStatus.UNABLE_TO_VERIFY:
            return unable_to_verify()
        if self is VerificationStatus.UNKNOWN:
            return unknown()
