

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PinStatusEnum(enum.StrEnum):
    VERIFIED = "VERIFIED"
    TRANSPORT_PIN = "TRANSPORT_PIN"
    EMPTY_PIN = "EMPTY_PIN"
    BLOCKED = "BLOCKED"
    VERIFIABLE = "VERIFIABLE"

    def visit(
        self,
        verified: typing.Callable[[], T_Result],
        transport_pin: typing.Callable[[], T_Result],
        empty_pin: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
        verifiable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PinStatusEnum.VERIFIED:
            return verified()
        if self is PinStatusEnum.TRANSPORT_PIN:
            return transport_pin()
        if self is PinStatusEnum.EMPTY_PIN:
            return empty_pin()
        if self is PinStatusEnum.BLOCKED:
            return blocked()
        if self is PinStatusEnum.VERIFIABLE:
            return verifiable()
