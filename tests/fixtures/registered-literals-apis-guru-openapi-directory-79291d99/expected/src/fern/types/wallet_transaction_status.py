

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WalletTransactionStatus(enum.StrEnum):
    """
    The status of the transaction.

    `AUTHORISING`: The transaction is being processed for validation and compliance.

    `INITIATED`: The transaction has been initiated and is currently being processed.

    `EXECUTED`: The transaction has been successfully executed and is considered complete. This is only applicable for debit transactions.

    `SETTLED`: The transaction has settled and funds are available for use. This is only applicable for credit transactions. A transaction will typically settle within seconds to several days, depending on which payment rail is used.

    `FAILED`: The transaction failed to process successfully. This is a terminal status.

    `BLOCKED`: The transaction has been blocked for violating compliance rules. This is a terminal status.
    """

    AUTHORISING = "AUTHORISING"
    INITIATED = "INITIATED"
    EXECUTED = "EXECUTED"
    SETTLED = "SETTLED"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"

    def visit(
        self,
        authorising: typing.Callable[[], T_Result],
        initiated: typing.Callable[[], T_Result],
        executed: typing.Callable[[], T_Result],
        settled: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WalletTransactionStatus.AUTHORISING:
            return authorising()
        if self is WalletTransactionStatus.INITIATED:
            return initiated()
        if self is WalletTransactionStatus.EXECUTED:
            return executed()
        if self is WalletTransactionStatus.SETTLED:
            return settled()
        if self is WalletTransactionStatus.BLOCKED:
            return blocked()
        if self is WalletTransactionStatus.FAILED:
            return failed()
