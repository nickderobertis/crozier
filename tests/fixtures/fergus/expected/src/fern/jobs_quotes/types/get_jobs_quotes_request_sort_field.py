

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJobsQuotesRequestSortField(enum.StrEnum):
    ID = "id"
    CREATED_AT = "createdAt"
    LAST_MODIFIED = "lastModified"

    def visit(
        self,
        id: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        last_modified: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetJobsQuotesRequestSortField.ID:
            return id()
        if self is GetJobsQuotesRequestSortField.CREATED_AT:
            return created_at()
        if self is GetJobsQuotesRequestSortField.LAST_MODIFIED:
            return last_modified()
