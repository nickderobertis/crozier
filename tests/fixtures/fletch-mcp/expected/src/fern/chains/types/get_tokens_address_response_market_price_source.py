

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTokensAddressResponseMarketPriceSource(enum.StrEnum):
    DEX = "dex"

    def visit(self, dex: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTokensAddressResponseMarketPriceSource.DEX:
            return dex()
