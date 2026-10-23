

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTokensAddressResponseTrust(enum.StrEnum):
    VERIFIED = "verified"
    LISTED = "listed"
    LOOKALIKE = "lookalike"
    COMMUNITY = "community"
    UNKNOWN = "unknown"

    def visit(
        self,
        verified: typing.Callable[[], T_Result],
        listed: typing.Callable[[], T_Result],
        lookalike: typing.Callable[[], T_Result],
        community: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTokensAddressResponseTrust.VERIFIED:
            return verified()
        if self is GetTokensAddressResponseTrust.LISTED:
            return listed()
        if self is GetTokensAddressResponseTrust.LOOKALIKE:
            return lookalike()
        if self is GetTokensAddressResponseTrust.COMMUNITY:
            return community()
        if self is GetTokensAddressResponseTrust.UNKNOWN:
            return unknown()
