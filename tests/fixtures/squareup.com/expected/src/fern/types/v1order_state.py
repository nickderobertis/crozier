

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1OrderState(enum.StrEnum):
    """ """

    PENDING = "PENDING"
    OPEN = "OPEN"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    REFUNDED = "REFUNDED"
    REJECTED = "REJECTED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        open: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1OrderState.PENDING:
            return pending()
        if self is V1OrderState.OPEN:
            return open()
        if self is V1OrderState.COMPLETED:
            return completed()
        if self is V1OrderState.CANCELED:
            return canceled()
        if self is V1OrderState.REFUNDED:
            return refunded()
        if self is V1OrderState.REJECTED:
            return rejected()
