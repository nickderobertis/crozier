

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppointmentAppointmentType(enum.StrEnum):
    """
    Kind of appointment the buyer is requesting.
    """

    SALES = "sales"
    SERVICE = "service"
    TEST_DRIVE = "test_drive"
    TRADE_IN = "trade_in"

    def visit(
        self,
        sales: typing.Callable[[], T_Result],
        service: typing.Callable[[], T_Result],
        test_drive: typing.Callable[[], T_Result],
        trade_in: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppointmentAppointmentType.SALES:
            return sales()
        if self is AppointmentAppointmentType.SERVICE:
            return service()
        if self is AppointmentAppointmentType.TEST_DRIVE:
            return test_drive()
        if self is AppointmentAppointmentType.TRADE_IN:
            return trade_in()
