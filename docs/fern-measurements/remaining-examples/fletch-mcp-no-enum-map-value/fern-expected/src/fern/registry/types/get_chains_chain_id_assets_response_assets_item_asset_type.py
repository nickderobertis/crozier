

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdAssetsResponseAssetsItemAssetType(enum.StrEnum):
    STOCK_TOKEN = "stock_token"
    STABLECOIN = "stablecoin"
    WRAPPED_NATIVE = "wrapped_native"
    BRIDGED = "bridged"

    def visit(
        self,
        stock_token: typing.Callable[[], T_Result],
        stablecoin: typing.Callable[[], T_Result],
        wrapped_native: typing.Callable[[], T_Result],
        bridged: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdAssetsResponseAssetsItemAssetType.STOCK_TOKEN:
            return stock_token()
        if self is GetChainsChainIdAssetsResponseAssetsItemAssetType.STABLECOIN:
            return stablecoin()
        if self is GetChainsChainIdAssetsResponseAssetsItemAssetType.WRAPPED_NATIVE:
            return wrapped_native()
        if self is GetChainsChainIdAssetsResponseAssetsItemAssetType.BRIDGED:
            return bridged()
