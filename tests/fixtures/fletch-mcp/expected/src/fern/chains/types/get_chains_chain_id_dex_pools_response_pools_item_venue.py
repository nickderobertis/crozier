

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdDexPoolsResponsePoolsItemVenue(enum.StrEnum):
    UNISWAP_V4 = "uniswap_v4"
    UNISWAP_V3 = "uniswap_v3"

    def visit(self, uniswap_v4: typing.Callable[[], T_Result], uniswap_v3: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetChainsChainIdDexPoolsResponsePoolsItemVenue.UNISWAP_V4:
            return uniswap_v4()
        if self is GetChainsChainIdDexPoolsResponsePoolsItemVenue.UNISWAP_V3:
            return uniswap_v3()
