

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PinResultEnum(enum.StrEnum):
    ERROR = "ERROR"
    OK = "OK"
    REJECTED = "REJECTED"
    WASBLOCKED = "WASBLOCKED"
    NOWBLOCKED = "NOWBLOCKED"
    TRANSPORT_PIN = "TRANSPORT_PIN"

    def visit(
        self,
        error: typing.Callable[[], T_Result],
        ok: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        wasblocked: typing.Callable[[], T_Result],
        nowblocked: typing.Callable[[], T_Result],
        transport_pin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PinResultEnum.ERROR:
            return error()
        if self is PinResultEnum.OK:
            return ok()
        if self is PinResultEnum.REJECTED:
            return rejected()
        if self is PinResultEnum.WASBLOCKED:
            return wasblocked()
        if self is PinResultEnum.NOWBLOCKED:
            return nowblocked()
        if self is PinResultEnum.TRANSPORT_PIN:
            return transport_pin()
