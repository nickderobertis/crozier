

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UeContextTransferStatus(enum.StrEnum):
    TRANSFERRED = "TRANSFERRED"
    NOT_TRANSFERRED = "NOT_TRANSFERRED"

    def visit(
        self, transferred: typing.Callable[[], T_Result], not_transferred: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is UeContextTransferStatus.TRANSFERRED:
            return transferred()
        if self is UeContextTransferStatus.NOT_TRANSFERRED:
            return not_transferred()
