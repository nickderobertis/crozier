

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits(enum.StrEnum):
    FLOAT = "float"
    POOLS = "pools"
    ISSUER = "issuer"
    BRIDGE = "bridge"
    CONTRACTS = "contracts"
    UNKNOWN = "unknown"

    def visit(
        self,
        float_: typing.Callable[[], T_Result],
        pools: typing.Callable[[], T_Result],
        issuer: typing.Callable[[], T_Result],
        bridge: typing.Callable[[], T_Result],
        contracts: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits.FLOAT:
            return float_()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits.POOLS:
            return pools()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits.ISSUER:
            return issuer()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits.BRIDGE:
            return bridge()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits.CONTRACTS:
            return contracts()
        if self is GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits.UNKNOWN:
            return unknown()
