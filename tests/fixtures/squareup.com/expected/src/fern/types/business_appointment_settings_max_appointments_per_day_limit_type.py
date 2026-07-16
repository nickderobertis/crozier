

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BusinessAppointmentSettingsMaxAppointmentsPerDayLimitType(str, enum.Enum):
    """
    Types of daily appointment limits.
    """

    PER_TEAM_MEMBER = "PER_TEAM_MEMBER"
    PER_LOCATION = "PER_LOCATION"

    def visit(
        self, per_team_member: typing.Callable[[], T_Result], per_location: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is BusinessAppointmentSettingsMaxAppointmentsPerDayLimitType.PER_TEAM_MEMBER:
            return per_team_member()
        if self is BusinessAppointmentSettingsMaxAppointmentsPerDayLimitType.PER_LOCATION:
            return per_location()
