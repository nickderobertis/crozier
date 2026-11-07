

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChainstateTokensRequestPartsItem(enum.StrEnum):
    NAME = "name"
    SYMBOL = "symbol"
    DECIMALS = "decimals"
    TOTAL_SUPPLY = "totalSupply"
    VERSION = "version"
    SOME = "some"
    ALL = "all"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        symbol: typing.Callable[[], T_Result],
        decimals: typing.Callable[[], T_Result],
        total_supply: typing.Callable[[], T_Result],
        version: typing.Callable[[], T_Result],
        some: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChainstateTokensRequestPartsItem.NAME:
            return name()
        if self is ChainstateTokensRequestPartsItem.SYMBOL:
            return symbol()
        if self is ChainstateTokensRequestPartsItem.DECIMALS:
            return decimals()
        if self is ChainstateTokensRequestPartsItem.TOTAL_SUPPLY:
            return total_supply()
        if self is ChainstateTokensRequestPartsItem.VERSION:
            return version()
        if self is ChainstateTokensRequestPartsItem.SOME:
            return some()
        if self is ChainstateTokensRequestPartsItem.ALL:
            return all_()
