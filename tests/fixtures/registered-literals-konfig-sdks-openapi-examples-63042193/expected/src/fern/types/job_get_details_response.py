

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_get_details_response_contexts_item import JobGetDetailsResponseContextsItem
from .job_get_details_response_executor import JobGetDetailsResponseExecutor
from .job_get_details_response_latest_workflow import JobGetDetailsResponseLatestWorkflow
from .job_get_details_response_messages_item import JobGetDetailsResponseMessagesItem
from .job_get_details_response_organization import JobGetDetailsResponseOrganization
from .job_get_details_response_parallel_runs_item import JobGetDetailsResponseParallelRunsItem
from .job_get_details_response_pipeline import JobGetDetailsResponsePipeline
from .job_get_details_response_project import JobGetDetailsResponseProject
from .job_get_details_response_status import JobGetDetailsResponseStatus


class JobGetDetailsResponse(UniversalBaseModel):
    """
    Job Details
    """

    web_url: str = pydantic.Field()
    """
    URL of the job in CircleCI Web UI.
    """

    project: JobGetDetailsResponseProject = pydantic.Field()
    """
    Information about a project.
    """

    parallel_runs: typing.List[JobGetDetailsResponseParallelRunsItem] = pydantic.Field()
    """
    Info about parallels runs and their status.
    """

    started_at: dt.datetime = pydantic.Field()
    """
    The date and time the job started.
    """

    latest_workflow: JobGetDetailsResponseLatestWorkflow = pydantic.Field()
    """
    Info about the latest workflow the job was a part of.
    """

    name: str = pydantic.Field()
    """
    The name of the job.
    """

    executor: JobGetDetailsResponseExecutor = pydantic.Field()
    """
    Information about executor used for a job.
    """

    parallelism: int = pydantic.Field()
    """
    A number of parallel runs the job has.
    """

    status: JobGetDetailsResponseStatus = pydantic.Field()
    """
    The current status of the job.
    """

    number: int = pydantic.Field()
    """
    The number of the job.
    """

    pipeline: JobGetDetailsResponsePipeline = pydantic.Field()
    """
    Info about a pipeline the job is a part of.
    """

    duration: int = pydantic.Field()
    """
    Duration of a job in milliseconds.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The time when the job was created.
    """

    messages: typing.List[JobGetDetailsResponseMessagesItem] = pydantic.Field()
    """
    Messages from CircleCI execution platform.
    """

    contexts: typing.List[JobGetDetailsResponseContextsItem] = pydantic.Field()
    """
    List of contexts used by the job.
    """

    organization: JobGetDetailsResponseOrganization = pydantic.Field()
    """
    Information about an organization.
    """

    queued_at: dt.datetime = pydantic.Field()
    """
    The time when the job was placed in a queue.
    """

    stopped_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when the job stopped.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
