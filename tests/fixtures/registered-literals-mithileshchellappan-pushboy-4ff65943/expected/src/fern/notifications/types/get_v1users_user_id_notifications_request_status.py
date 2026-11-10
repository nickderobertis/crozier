

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetV1UsersUserIdNotificationsRequestStatus(enum.StrEnum):
    QUEUED = "QUEUED"
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    DISPATCHED = "DISPATCHED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        dispatched: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetV1UsersUserIdNotificationsRequestStatus.QUEUED:
            return queued()
        if self is GetV1UsersUserIdNotificationsRequestStatus.SCHEDULED:
            return scheduled()
        if self is GetV1UsersUserIdNotificationsRequestStatus.IN_PROGRESS:
            return in_progress()
        if self is GetV1UsersUserIdNotificationsRequestStatus.DISPATCHED:
            return dispatched()
        if self is GetV1UsersUserIdNotificationsRequestStatus.COMPLETED:
            return completed()
        if self is GetV1UsersUserIdNotificationsRequestStatus.FAILED:
            return failed()
