

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChainNetwork(enum.StrEnum):
    MAINNET = "mainnet"
    TESTNET = "testnet"

    def visit(self, mainnet: typing.Callable[[], T_Result], testnet: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChainNetwork.MAINNET:
            return mainnet()
        if self is ChainNetwork.TESTNET:
            return testnet()
