

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TimeOffRequestsFilterTimeOffRequestStatus(str, enum.Enum):
    """
    Time off request status to filter on
    """

    REQUESTED = "requested"
    APPROVED = "approved"
    DECLINED = "declined"
    CANCELLED = "cancelled"
    DELETED = "deleted"
    OTHER = "other"

    def visit(
        self,
        requested: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TimeOffRequestsFilterTimeOffRequestStatus.REQUESTED:
            return requested()
        if self is TimeOffRequestsFilterTimeOffRequestStatus.APPROVED:
            return approved()
        if self is TimeOffRequestsFilterTimeOffRequestStatus.DECLINED:
            return declined()
        if self is TimeOffRequestsFilterTimeOffRequestStatus.CANCELLED:
            return cancelled()
        if self is TimeOffRequestsFilterTimeOffRequestStatus.DELETED:
            return deleted()
        if self is TimeOffRequestsFilterTimeOffRequestStatus.OTHER:
            return other()
