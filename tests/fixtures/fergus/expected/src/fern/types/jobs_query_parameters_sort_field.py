

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobsQueryParametersSortField(enum.StrEnum):
    JOB_NO = "jobNo"
    CREATED_AT = "createdAt"
    LAST_MODIFIED = "lastModified"

    def visit(
        self,
        job_no: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        last_modified: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobsQueryParametersSortField.JOB_NO:
            return job_no()
        if self is JobsQueryParametersSortField.CREATED_AT:
            return created_at()
        if self is JobsQueryParametersSortField.LAST_MODIFIED:
            return last_modified()
