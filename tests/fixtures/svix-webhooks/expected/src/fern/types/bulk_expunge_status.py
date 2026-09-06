

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BulkExpungeStatus(enum.StrEnum):
    EXPUNGED = "expunged"
    NOT_FOUND = "not-found"

    def visit(self, expunged: typing.Callable[[], T_Result], not_found: typing.Callable[[], T_Result]) -> T_Result:
        if self is BulkExpungeStatus.EXPUNGED:
            return expunged()
        if self is BulkExpungeStatus.NOT_FOUND:
            return not_found()
