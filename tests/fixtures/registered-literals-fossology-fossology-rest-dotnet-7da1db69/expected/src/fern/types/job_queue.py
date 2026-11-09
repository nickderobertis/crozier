

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_queue_download import JobQueueDownload


class JobQueue(UniversalBaseModel):
    """
    Structure of jobs queue
    """

    job_queue_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="jobQueueId"),
        pydantic.Field(alias="jobQueueId", description="Job queue id"),
    ] = None
    """
    Job queue id
    """

    job_queue_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jobQueueType"),
        pydantic.Field(alias="jobQueueType", description="Job queue type (generally agent name)"),
    ] = None
    """
    Job queue type (generally agent name)
    """

    start_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="startTime"),
        pydantic.Field(alias="startTime", description="Job queue start time"),
    ] = None
    """
    Job queue start time
    """

    end_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endTime"),
        pydantic.Field(alias="endTime", description="Job queue end time"),
    ] = None
    """
    Job queue end time
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Job queue completion status
    """

    items_processed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemsProcessed"),
        pydantic.Field(alias="itemsProcessed", description="Number of items processed"),
    ] = None
    """
    Number of items processed
    """

    log: typing.Optional[str] = pydantic.Field(default=None)
    """
    Location of log file if exists
    """

    dependencies: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    List of dependent job queue ids
    """

    items_per_sec: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="itemsPerSec"),
        pydantic.Field(alias="itemsPerSec", description="Number of items processed per second"),
    ] = None
    """
    Number of items processed per second
    """

    can_do_actions: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="canDoActions"),
        pydantic.Field(alias="canDoActions", description="Job can accept new actions like pause and cancel"),
    ] = None
    """
    Job can accept new actions like pause and cancel
    """

    is_in_progress: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isInProgress"),
        pydantic.Field(alias="isInProgress", description="Checks if the job queue is still in progress"),
    ] = None
    """
    Checks if the job queue is still in progress
    """

    is_ready: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isReady"),
        pydantic.Field(alias="isReady", description="Is the job ready"),
    ] = None
    """
    Is the job ready
    """

    download: typing.Optional[JobQueueDownload] = pydantic.Field(default=None)
    """
    Report download information
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
