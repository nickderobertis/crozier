

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TimeOffRequestRequestType(enum.StrEnum):
    """
    The type of request
    """

    VACATION = "vacation"
    SICK = "sick"
    PERSONAL = "personal"
    JURY_DUTY = "jury_duty"
    VOLUNTEER = "volunteer"
    BEREAVEMENT = "bereavement"
    OTHER = "other"

    def visit(
        self,
        vacation: typing.Callable[[], T_Result],
        sick: typing.Callable[[], T_Result],
        personal: typing.Callable[[], T_Result],
        jury_duty: typing.Callable[[], T_Result],
        volunteer: typing.Callable[[], T_Result],
        bereavement: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TimeOffRequestRequestType.VACATION:
            return vacation()
        if self is TimeOffRequestRequestType.SICK:
            return sick()
        if self is TimeOffRequestRequestType.PERSONAL:
            return personal()
        if self is TimeOffRequestRequestType.JURY_DUTY:
            return jury_duty()
        if self is TimeOffRequestRequestType.VOLUNTEER:
            return volunteer()
        if self is TimeOffRequestRequestType.BEREAVEMENT:
            return bereavement()
        if self is TimeOffRequestRequestType.OTHER:
            return other()
