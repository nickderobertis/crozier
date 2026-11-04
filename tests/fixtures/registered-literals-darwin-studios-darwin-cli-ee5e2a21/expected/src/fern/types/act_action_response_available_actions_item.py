

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActActionResponseAvailableActionsItem(enum.StrEnum):
    STATUS = "status"
    UPDATE = "update"
    AUTHENTICATE = "authenticate"
    APPROVE = "approve"
    PAY = "pay"
    STOP = "stop"
    END = "end"

    def visit(
        self,
        status: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        authenticate: typing.Callable[[], T_Result],
        approve: typing.Callable[[], T_Result],
        pay: typing.Callable[[], T_Result],
        stop: typing.Callable[[], T_Result],
        end: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActActionResponseAvailableActionsItem.STATUS:
            return status()
        if self is ActActionResponseAvailableActionsItem.UPDATE:
            return update()
        if self is ActActionResponseAvailableActionsItem.AUTHENTICATE:
            return authenticate()
        if self is ActActionResponseAvailableActionsItem.APPROVE:
            return approve()
        if self is ActActionResponseAvailableActionsItem.PAY:
            return pay()
        if self is ActActionResponseAvailableActionsItem.STOP:
            return stop()
        if self is ActActionResponseAvailableActionsItem.END:
            return end()
