

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocHead200ResponseState(enum.StrEnum):
    PENDING = "pending"
    READY = "ready"
    FAILED = "failed"
    DELETING = "deleting"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        deleting: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocHead200ResponseState.PENDING:
            return pending()
        if self is DocHead200ResponseState.READY:
            return ready()
        if self is DocHead200ResponseState.FAILED:
            return failed()
        if self is DocHead200ResponseState.DELETING:
            return deleting()
