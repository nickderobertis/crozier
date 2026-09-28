

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableRunDispatchStatus(enum.StrEnum):
    """
    Current dispatch lifecycle state.
    """

    PENDING = "pending"
    DISPATCHING = "dispatching"
    COMPLETE = "complete"
    CANCELED = "canceled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        dispatching: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2TableRunDispatchStatus.PENDING:
            return pending()
        if self is V2TableRunDispatchStatus.DISPATCHING:
            return dispatching()
        if self is V2TableRunDispatchStatus.COMPLETE:
            return complete()
        if self is V2TableRunDispatchStatus.CANCELED:
            return canceled()
