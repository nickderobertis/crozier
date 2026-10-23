

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTokensAddressResponseReadingRobinhoodAppMatch(enum.StrEnum):
    TICKER_ONLY = "ticker_only"
    NONE = "none"

    def visit(self, ticker_only: typing.Callable[[], T_Result], none: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTokensAddressResponseReadingRobinhoodAppMatch.TICKER_ONLY:
            return ticker_only()
        if self is GetTokensAddressResponseReadingRobinhoodAppMatch.NONE:
            return none()
