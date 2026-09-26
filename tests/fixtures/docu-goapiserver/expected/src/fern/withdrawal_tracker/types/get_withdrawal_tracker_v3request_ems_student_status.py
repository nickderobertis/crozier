

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWithdrawalTrackerV3RequestEmsStudentStatus(enum.StrEnum):
    ENROLLED = "Enrolled"
    REGISTRATION_PENDING = "Registration Pending"
    CONFIRMED_START_DATE = "Confirmed Start Date"
    WAITLIST = "Waitlist"
    MISSING_INFORMATION = "Missing Information"
    WITHDRAWN = "Withdrawn"
    UNKNOWN = "Unknown"
    EMPTY = "Empty"

    def visit(
        self,
        enrolled: typing.Callable[[], T_Result],
        registration_pending: typing.Callable[[], T_Result],
        confirmed_start_date: typing.Callable[[], T_Result],
        waitlist: typing.Callable[[], T_Result],
        missing_information: typing.Callable[[], T_Result],
        withdrawn: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWithdrawalTrackerV3RequestEmsStudentStatus.ENROLLED:
            return enrolled()
        if self is GetWithdrawalTrackerV3RequestEmsStudentStatus.REGISTRATION_PENDING:
            return registration_pending()
        if self is GetWithdrawalTrackerV3RequestEmsStudentStatus.CONFIRMED_START_DATE:
            return confirmed_start_date()
        if self is GetWithdrawalTrackerV3RequestEmsStudentStatus.WAITLIST:
            return waitlist()
        if self is GetWithdrawalTrackerV3RequestEmsStudentStatus.MISSING_INFORMATION:
            return missing_information()
        if self is GetWithdrawalTrackerV3RequestEmsStudentStatus.WITHDRAWN:
            return withdrawn()
        if self is GetWithdrawalTrackerV3RequestEmsStudentStatus.UNKNOWN:
            return unknown()
        if self is GetWithdrawalTrackerV3RequestEmsStudentStatus.EMPTY:
            return empty()
