

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BusinessAppointmentSettingsAlignmentTime(enum.StrEnum):
    """
    Time units of a service duration for bookings.
    """

    SERVICE_DURATION = "SERVICE_DURATION"
    QUARTER_HOURLY = "QUARTER_HOURLY"
    HALF_HOURLY = "HALF_HOURLY"
    HOURLY = "HOURLY"

    def visit(
        self,
        service_duration: typing.Callable[[], T_Result],
        quarter_hourly: typing.Callable[[], T_Result],
        half_hourly: typing.Callable[[], T_Result],
        hourly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BusinessAppointmentSettingsAlignmentTime.SERVICE_DURATION:
            return service_duration()
        if self is BusinessAppointmentSettingsAlignmentTime.QUARTER_HOURLY:
            return quarter_hourly()
        if self is BusinessAppointmentSettingsAlignmentTime.HALF_HOURLY:
            return half_hourly()
        if self is BusinessAppointmentSettingsAlignmentTime.HOURLY:
            return hourly()
