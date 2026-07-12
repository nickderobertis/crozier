

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ActivityAttendeeStatus(str, enum.Enum):
    ACCEPTED = "accepted"
    TENTATIVE = "tentative"
    DECLINED = "declined"

    def visit(
        self,
        accepted: typing.Callable[[], T_Result],
        tentative: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActivityAttendeeStatus.ACCEPTED:
            return accepted()
        if self is ActivityAttendeeStatus.TENTATIVE:
            return tentative()
        if self is ActivityAttendeeStatus.DECLINED:
            return declined()
