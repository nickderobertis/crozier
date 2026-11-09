

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_queue import JobQueue


class ShowJob(UniversalBaseModel):
    """
    History of all the jobs and the job queue info
    """

    job_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId", description="Job ID")
    ] = None
    """
    Job ID
    """

    job_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jobName"),
        pydantic.Field(alias="jobName", description="Job name (generally upload name)"),
    ] = None
    """
    Job name (generally upload name)
    """

    job_queue: typing_extensions.Annotated[
        typing.Optional[typing.List[JobQueue]],
        FieldMetadata(alias="jobQueue"),
        pydantic.Field(alias="jobQueue", description="Jobs queued for the current job"),
    ] = None
    """
    Jobs queued for the current job
    """

    upload_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="uploadId"),
        pydantic.Field(alias="uploadId", description="Upload ID to which the job belongs to."),
    ] = None
    """
    Upload ID to which the job belongs to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
