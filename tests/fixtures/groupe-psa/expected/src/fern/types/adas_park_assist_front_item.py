

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdasParkAssistFrontItem(enum.StrEnum):
    FAULT = "Fault"
    DRIVER_INHIBITION = "DriverInhibition"
    ACTIVE = "Active"
    WAIT = "Wait"
    OUT_OF_SERVICE = "OutOfService"

    def visit(
        self,
        fault: typing.Callable[[], T_Result],
        driver_inhibition: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        wait: typing.Callable[[], T_Result],
        out_of_service: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdasParkAssistFrontItem.FAULT:
            return fault()
        if self is AdasParkAssistFrontItem.DRIVER_INHIBITION:
            return driver_inhibition()
        if self is AdasParkAssistFrontItem.ACTIVE:
            return active()
        if self is AdasParkAssistFrontItem.WAIT:
            return wait()
        if self is AdasParkAssistFrontItem.OUT_OF_SERVICE:
            return out_of_service()
