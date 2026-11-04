

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecordsGetPredictionsResponseOneItemStatus(enum.StrEnum):
    READY = "ready"
    PENDING = "pending"
    ERRORED = "errored"

    def visit(
        self,
        ready: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        errored: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RecordsGetPredictionsResponseOneItemStatus.READY:
            return ready()
        if self is RecordsGetPredictionsResponseOneItemStatus.PENDING:
            return pending()
        if self is RecordsGetPredictionsResponseOneItemStatus.ERRORED:
            return errored()
