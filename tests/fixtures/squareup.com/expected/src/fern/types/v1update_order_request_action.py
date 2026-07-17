

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1UpdateOrderRequestAction(enum.StrEnum):
    """ """

    COMPLETE = "COMPLETE"
    CANCEL = "CANCEL"
    REFUND = "REFUND"

    def visit(
        self,
        complete: typing.Callable[[], T_Result],
        cancel: typing.Callable[[], T_Result],
        refund: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1UpdateOrderRequestAction.COMPLETE:
            return complete()
        if self is V1UpdateOrderRequestAction.CANCEL:
            return cancel()
        if self is V1UpdateOrderRequestAction.REFUND:
            return refund()
