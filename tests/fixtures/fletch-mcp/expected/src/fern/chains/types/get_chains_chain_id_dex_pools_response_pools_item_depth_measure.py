

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdDexPoolsResponsePoolsItemDepthMeasure(enum.StrEnum):
    QUOTE_HOLDINGS = "quote_holdings"
    BOUNDED_ONE_PERCENT_QUOTE = "bounded_one_percent_quote"
    UNAVAILABLE = "unavailable"

    def visit(
        self,
        quote_holdings: typing.Callable[[], T_Result],
        bounded_one_percent_quote: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdDexPoolsResponsePoolsItemDepthMeasure.QUOTE_HOLDINGS:
            return quote_holdings()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemDepthMeasure.BOUNDED_ONE_PERCENT_QUOTE:
            return bounded_one_percent_quote()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemDepthMeasure.UNAVAILABLE:
            return unavailable()
