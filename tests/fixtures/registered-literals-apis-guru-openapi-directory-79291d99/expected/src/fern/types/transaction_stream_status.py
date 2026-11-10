

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionStreamStatus(enum.StrEnum):
    """
    The current status of the transaction stream.

    `MATURE`: A `MATURE` recurring stream should have at least 3 transactions and happen on a regular cadence (For Annual recurring stream, we will mark it `MATURE` after 2 instances).

    `EARLY_DETECTION`: When a recurring transaction first appears in the transaction history and before it fulfills the requirement of a mature stream, the status will be `EARLY_DETECTION`.

    `TOMBSTONED`: A stream that was previously in the `EARLY_DETECTION` status will move to the `TOMBSTONED` status when no further transactions were found at the next expected date.

    `UNKNOWN`: A stream is assigned an `UNKNOWN` status when none of the other statuses are applicable.
    """

    UNKNOWN = "UNKNOWN"
    MATURE = "MATURE"
    EARLY_DETECTION = "EARLY_DETECTION"
    TOMBSTONED = "TOMBSTONED"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        mature: typing.Callable[[], T_Result],
        early_detection: typing.Callable[[], T_Result],
        tombstoned: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionStreamStatus.UNKNOWN:
            return unknown()
        if self is TransactionStreamStatus.MATURE:
            return mature()
        if self is TransactionStreamStatus.EARLY_DETECTION:
            return early_detection()
        if self is TransactionStreamStatus.TOMBSTONED:
            return tombstoned()
