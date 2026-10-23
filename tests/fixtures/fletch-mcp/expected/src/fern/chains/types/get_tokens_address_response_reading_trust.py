

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTokensAddressResponseReadingTrust(enum.StrEnum):
    VERIFIED = "verified"
    LISTED = "listed"
    COMMUNITY = "community"
    LOOKALIKE = "lookalike"
    UNKNOWN = "unknown"

    def visit(
        self,
        verified: typing.Callable[[], T_Result],
        listed: typing.Callable[[], T_Result],
        community: typing.Callable[[], T_Result],
        lookalike: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTokensAddressResponseReadingTrust.VERIFIED:
            return verified()
        if self is GetTokensAddressResponseReadingTrust.LISTED:
            return listed()
        if self is GetTokensAddressResponseReadingTrust.COMMUNITY:
            return community()
        if self is GetTokensAddressResponseReadingTrust.LOOKALIKE:
            return lookalike()
        if self is GetTokensAddressResponseReadingTrust.UNKNOWN:
            return unknown()
