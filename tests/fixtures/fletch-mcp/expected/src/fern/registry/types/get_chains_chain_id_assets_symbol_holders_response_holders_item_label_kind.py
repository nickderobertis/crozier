

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind(enum.StrEnum):
    POOL_MANAGER = "pool_manager"
    DEX_POOL = "dex_pool"
    ISSUER = "issuer"
    BRIDGE_GATEWAY = "bridge_gateway"
    LOCKER = "locker"
    CONTRACT = "contract"
    EXCHANGE = "exchange"
    EOA = "eoa"

    def visit(
        self,
        pool_manager: typing.Callable[[], T_Result],
        dex_pool: typing.Callable[[], T_Result],
        issuer: typing.Callable[[], T_Result],
        bridge_gateway: typing.Callable[[], T_Result],
        locker: typing.Callable[[], T_Result],
        contract: typing.Callable[[], T_Result],
        exchange: typing.Callable[[], T_Result],
        eoa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind.POOL_MANAGER:
            return pool_manager()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind.DEX_POOL:
            return dex_pool()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind.ISSUER:
            return issuer()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind.BRIDGE_GATEWAY:
            return bridge_gateway()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind.LOCKER:
            return locker()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind.CONTRACT:
            return contract()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind.EXCHANGE:
            return exchange()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind.EOA:
            return eoa()
