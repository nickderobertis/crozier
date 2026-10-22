

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BitcoinNetwork(enum.StrEnum):
    MAINNET = "Mainnet"
    TESTNET = "Testnet"
    TESTNET4 = "Testnet4"
    SIGNET = "Signet"
    SIGNET_CUSTOM = "SignetCustom"
    REGTEST = "Regtest"

    def visit(
        self,
        mainnet: typing.Callable[[], T_Result],
        testnet: typing.Callable[[], T_Result],
        testnet4: typing.Callable[[], T_Result],
        signet: typing.Callable[[], T_Result],
        signet_custom: typing.Callable[[], T_Result],
        regtest: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BitcoinNetwork.MAINNET:
            return mainnet()
        if self is BitcoinNetwork.TESTNET:
            return testnet()
        if self is BitcoinNetwork.TESTNET4:
            return testnet4()
        if self is BitcoinNetwork.SIGNET:
            return signet()
        if self is BitcoinNetwork.SIGNET_CUSTOM:
            return signet_custom()
        if self is BitcoinNetwork.REGTEST:
            return regtest()
