

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflow_get_jobs_response_items_item_status import WorkflowGetJobsResponseItemsItemStatus
from .workflow_get_jobs_response_items_item_type import WorkflowGetJobsResponseItemsItemType


class WorkflowGetJobsResponseItemsItem(UniversalBaseModel):
    """
    Job
    """

    canceled_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the user.
    """

    dependencies: typing.List[str] = pydantic.Field()
    """
    A sequence of the unique job IDs for the jobs that this job depends upon in the workflow.
    """

    job_number: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of the job.
    """

    id: str = pydantic.Field()
    """
    The unique ID of the job.
    """

    started_at: dt.datetime = pydantic.Field()
    """
    The date and time the job started.
    """

    name: str = pydantic.Field()
    """
    The name of the job.
    """

    approved_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the user.
    """

    project_slug: str = pydantic.Field()
    """
    The project-slug for the job.
    """

    status: WorkflowGetJobsResponseItemsItemStatus = pydantic.Field()
    """
    The current status of the job.
    """

    type: WorkflowGetJobsResponseItemsItemType = pydantic.Field()
    """
    The type of job.
    """

    stopped_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the job stopped.
    """

    approval_request_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the job.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
