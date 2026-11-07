

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListPronunciationsRequestStatus(enum.StrEnum):
    PENDING = "pending"
    READY = "ready"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListPronunciationsRequestStatus.PENDING:
            return pending()
        if self is ListPronunciationsRequestStatus.READY:
            return ready()
        if self is ListPronunciationsRequestStatus.FAILED:
            return failed()
