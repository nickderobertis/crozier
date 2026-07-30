

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AtsEventType(enum.StrEnum):
    ATS_JOB_CREATED = "ats.job.created"
    ATS_JOB_UPDATED = "ats.job.updated"
    ATS_JOB_DELETED = "ats.job.deleted"
    ATS_APPLICANT_CREATED = "ats.applicant.created"
    ATS_APPLICANT_UPDATED = "ats.applicant.updated"
    ATS_APPLICANT_DELETED = "ats.applicant.deleted"

    def visit(
        self,
        ats_job_created: typing.Callable[[], T_Result],
        ats_job_updated: typing.Callable[[], T_Result],
        ats_job_deleted: typing.Callable[[], T_Result],
        ats_applicant_created: typing.Callable[[], T_Result],
        ats_applicant_updated: typing.Callable[[], T_Result],
        ats_applicant_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AtsEventType.ATS_JOB_CREATED:
            return ats_job_created()
        if self is AtsEventType.ATS_JOB_UPDATED:
            return ats_job_updated()
        if self is AtsEventType.ATS_JOB_DELETED:
            return ats_job_deleted()
        if self is AtsEventType.ATS_APPLICANT_CREATED:
            return ats_applicant_created()
        if self is AtsEventType.ATS_APPLICANT_UPDATED:
            return ats_applicant_updated()
        if self is AtsEventType.ATS_APPLICANT_DELETED:
            return ats_applicant_deleted()
