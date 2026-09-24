

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEnquiriesRequestFilterStatus(enum.StrEnum):
    TODO = "TODO"
    CONTACTED = "CONTACTED"
    JOBCREATED = "JOBCREATED"
    REJECTED = "REJECTED"

    def visit(
        self,
        todo: typing.Callable[[], T_Result],
        contacted: typing.Callable[[], T_Result],
        jobcreated: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetEnquiriesRequestFilterStatus.TODO:
            return todo()
        if self is GetEnquiriesRequestFilterStatus.CONTACTED:
            return contacted()
        if self is GetEnquiriesRequestFilterStatus.JOBCREATED:
            return jobcreated()
        if self is GetEnquiriesRequestFilterStatus.REJECTED:
            return rejected()
