

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsResponseChainsItemNetwork(enum.StrEnum):
    MAINNET = "mainnet"
    TESTNET = "testnet"

    def visit(self, mainnet: typing.Callable[[], T_Result], testnet: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetChainsResponseChainsItemNetwork.MAINNET:
            return mainnet()
        if self is GetChainsResponseChainsItemNetwork.TESTNET:
            return testnet()
