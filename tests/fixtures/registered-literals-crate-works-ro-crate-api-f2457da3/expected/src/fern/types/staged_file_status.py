

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StagedFileStatus(enum.StrEnum):
    """
    `pending` - staged in presigned mode and the bytes have not (yet) been observed; `received` - the bytes are held. Finalise remains the authoritative verification point.
    """

    PENDING = "pending"
    RECEIVED = "received"

    def visit(self, pending: typing.Callable[[], T_Result], received: typing.Callable[[], T_Result]) -> T_Result:
        if self is StagedFileStatus.PENDING:
            return pending()
        if self is StagedFileStatus.RECEIVED:
            return received()
