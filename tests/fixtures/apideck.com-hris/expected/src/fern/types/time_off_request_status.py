

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TimeOffRequestStatus(enum.StrEnum):
    """
    The status of the time off request.
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
        if self is TimeOffRequestStatus.REQUESTED:
            return requested()
        if self is TimeOffRequestStatus.APPROVED:
            return approved()
        if self is TimeOffRequestStatus.DECLINED:
            return declined()
        if self is TimeOffRequestStatus.CANCELLED:
            return cancelled()
        if self is TimeOffRequestStatus.DELETED:
            return deleted()
        if self is TimeOffRequestStatus.OTHER:
            return other()
