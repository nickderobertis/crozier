

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .code import Code
from .created_at import CreatedAt
from .created_by import CreatedBy
from .deleted import Deleted
from .department import Department
from .description import Description
from .id import Id
from .job_blocks_item import JobBlocksItem
from .job_branch import JobBranch
from .job_employment_terms import JobEmploymentTerms
from .job_hiring_managers_item import JobHiringManagersItem
from .job_salary import JobSalary
from .job_status import JobStatus
from .job_visibility import JobVisibility
from .language import Language
from .owner_id import OwnerId
from .published_at import PublishedAt
from .record_url import RecordUrl
from .tags import Tags
from .title import Title
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class Job(UniversalBaseModel):
    addresses: typing.Optional[typing.List[Address]] = None
    available_to_employees: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Specifies whether an employee of the organization can apply for the job.
    """

    blocks: typing.Optional[typing.List[JobBlocksItem]] = None
    branch: typing.Optional[JobBranch] = pydantic.Field(default=None)
    """
    Details of the branch for which the job is created.
    """

    closing: typing.Optional[str] = None
    closing_date: typing.Optional[dt.date] = None
    closing_html: typing.Optional[str] = pydantic.Field(default=None)
    """
    The closing section of the job description in HTML format
    """

    code: typing.Optional[Code] = None
    confidential: typing.Optional[bool] = None
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    deleted: typing.Optional[Deleted] = None
    department: typing.Optional[Department] = None
    description: typing.Optional[Description] = None
    description_html: typing.Optional[str] = pydantic.Field(default=None)
    """
    The job description in HTML format
    """

    employment_terms: typing.Optional[JobEmploymentTerms] = None
    experience: typing.Optional[str] = pydantic.Field(default=None)
    """
    Level of experience required for the job role.
    """

    followers: typing.Optional[typing.List[str]] = None
    hiring_managers: typing.Optional[typing.List[JobHiringManagersItem]] = None
    id: typing.Optional[Id] = None
    job_portal_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the job portal
    """

    language: typing.Optional[Language] = None
    owner_id: typing.Optional[OwnerId] = None
    published_at: typing.Optional[PublishedAt] = None
    record_url: typing.Optional[RecordUrl] = None
    recruiters: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The recruiter is generally someone who is tasked to help the hiring manager find and screen qualified applicant
    """

    remote: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Specifies whether the posting is for a remote job.
    """

    requisition_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A job's Requisition ID (Req ID) allows your organization to identify and track a job based on alphanumeric naming conventions unique to your company's internal processes.
    """

    salary: typing.Optional[JobSalary] = None
    sequence: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sequence in relation to other jobs.
    """

    slug: typing.Optional[str] = None
    status: typing.Optional[JobStatus] = None
    tags: typing.Optional[Tags] = None
    title: typing.Optional[Title] = None
    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the job description
    """

    visibility: typing.Optional[JobVisibility] = pydantic.Field(default=None)
    """
    The visibility of the job
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
