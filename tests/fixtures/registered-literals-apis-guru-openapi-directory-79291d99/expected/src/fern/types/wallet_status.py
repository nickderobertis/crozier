

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WalletStatus(enum.StrEnum):
    """
    The status of the wallet.

    `UNKNOWN`: The wallet status is unknown.

    `ACTIVE`: The wallet is active and ready to send money to and receive money from.

    `CLOSED`: The wallet is closed. Any transactions made to or from this wallet will error.
    """

    UNKNOWN = "UNKNOWN"
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WalletStatus.UNKNOWN:
            return unknown()
        if self is WalletStatus.ACTIVE:
            return active()
        if self is WalletStatus.CLOSED:
            return closed()
