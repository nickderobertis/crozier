

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileSyncStatus(enum.StrEnum):
    """
    Outcome of a file sync reconciliation.
    """

    MR_CREATED = "mr_created"
    MR_EXISTS = "mr_exists"

    def visit(self, mr_created: typing.Callable[[], T_Result], mr_exists: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileSyncStatus.MR_CREATED:
            return mr_created()
        if self is FileSyncStatus.MR_EXISTS:
            return mr_exists()
