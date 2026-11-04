

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReaderCheckoutStatusChangePayloadStatus(enum.StrEnum):
    """
    The current status of the transaction.
    """

    SUCCESSFUL = "successful"
    FAILED = "failed"

    def visit(self, successful: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReaderCheckoutStatusChangePayloadStatus.SUCCESSFUL:
            return successful()
        if self is ReaderCheckoutStatusChangePayloadStatus.FAILED:
            return failed()
