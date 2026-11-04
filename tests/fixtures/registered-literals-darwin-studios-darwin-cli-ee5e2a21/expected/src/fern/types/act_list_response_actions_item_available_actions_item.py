

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActListResponseActionsItemAvailableActionsItem(enum.StrEnum):
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
        if self is ActListResponseActionsItemAvailableActionsItem.STATUS:
            return status()
        if self is ActListResponseActionsItemAvailableActionsItem.UPDATE:
            return update()
        if self is ActListResponseActionsItemAvailableActionsItem.AUTHENTICATE:
            return authenticate()
        if self is ActListResponseActionsItemAvailableActionsItem.APPROVE:
            return approve()
        if self is ActListResponseActionsItemAvailableActionsItem.PAY:
            return pay()
        if self is ActListResponseActionsItemAvailableActionsItem.STOP:
            return stop()
        if self is ActListResponseActionsItemAvailableActionsItem.END:
            return end()
