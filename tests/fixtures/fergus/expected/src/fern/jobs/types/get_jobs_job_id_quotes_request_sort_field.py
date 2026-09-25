

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJobsJobIdQuotesRequestSortField(enum.StrEnum):
    ID = "id"
    VERSION_NUMBER = "versionNumber"

    def visit(self, id: typing.Callable[[], T_Result], version_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetJobsJobIdQuotesRequestSortField.ID:
            return id()
        if self is GetJobsJobIdQuotesRequestSortField.VERSION_NUMBER:
            return version_number()
