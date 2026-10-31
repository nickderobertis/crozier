

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJobsRequestStatus(enum.StrEnum):
    ALL = "all"
    PENDING = "pending"
    INTERVIEW = "interview"
    DECLINED = "declined"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        interview: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetJobsRequestStatus.ALL:
            return all_()
        if self is GetJobsRequestStatus.PENDING:
            return pending()
        if self is GetJobsRequestStatus.INTERVIEW:
            return interview()
        if self is GetJobsRequestStatus.DECLINED:
            return declined()
