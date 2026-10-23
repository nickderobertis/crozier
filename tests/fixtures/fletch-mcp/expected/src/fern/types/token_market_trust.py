

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenMarketTrust(enum.StrEnum):
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
        if self is TokenMarketTrust.VERIFIED:
            return verified()
        if self is TokenMarketTrust.LISTED:
            return listed()
        if self is TokenMarketTrust.COMMUNITY:
            return community()
        if self is TokenMarketTrust.LOOKALIKE:
            return lookalike()
        if self is TokenMarketTrust.UNKNOWN:
            return unknown()
