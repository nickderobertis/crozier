

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdasParkAssistRearItem(enum.StrEnum):
    FAULT = "Fault"
    DRIVER_INHIBITION = "DriverInhibition"
    TRAILER_INHIBITION = "TrailerInhibition"
    ACTIVE = "Active"
    WAIT = "Wait"
    OUT_OF_SERVICE = "OutOfService"

    def visit(
        self,
        fault: typing.Callable[[], T_Result],
        driver_inhibition: typing.Callable[[], T_Result],
        trailer_inhibition: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        wait: typing.Callable[[], T_Result],
        out_of_service: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdasParkAssistRearItem.FAULT:
            return fault()
        if self is AdasParkAssistRearItem.DRIVER_INHIBITION:
            return driver_inhibition()
        if self is AdasParkAssistRearItem.TRAILER_INHIBITION:
            return trailer_inhibition()
        if self is AdasParkAssistRearItem.ACTIVE:
            return active()
        if self is AdasParkAssistRearItem.WAIT:
            return wait()
        if self is AdasParkAssistRearItem.OUT_OF_SERVICE:
            return out_of_service()
