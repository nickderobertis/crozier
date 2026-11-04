

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActActionResponseType(enum.StrEnum):
    START = "start"
    STATUS = "status"
    UPDATE = "update"
    APPROVE = "approve"
    STOP = "stop"
    PAY = "pay"
    END = "end"

    def visit(
        self,
        start: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        approve: typing.Callable[[], T_Result],
        stop: typing.Callable[[], T_Result],
        pay: typing.Callable[[], T_Result],
        end: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActActionResponseType.START:
            return start()
        if self is ActActionResponseType.STATUS:
            return status()
        if self is ActActionResponseType.UPDATE:
            return update()
        if self is ActActionResponseType.APPROVE:
            return approve()
        if self is ActActionResponseType.STOP:
            return stop()
        if self is ActActionResponseType.PAY:
            return pay()
        if self is ActActionResponseType.END:
            return end()
