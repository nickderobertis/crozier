

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_status import JobStatus


class Job(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the job
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the job
    """

    queue_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="queueDate"),
        pydantic.Field(alias="queueDate", description="When the job was queued"),
    ] = None
    """
    When the job was queued
    """

    upload_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="uploadId"),
        pydantic.Field(alias="uploadId", description="Upload for which the job was scheduled"),
    ] = None
    """
    Upload for which the job was scheduled
    """

    user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="userId"),
        pydantic.Field(alias="userId", description="User who scheduled the job"),
    ] = None
    """
    User who scheduled the job
    """

    group_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="groupId"),
        pydantic.Field(alias="groupId", description="Group under which the job was scheduled"),
    ] = None
    """
    Group under which the job was scheduled
    """

    eta: typing.Optional[int] = pydantic.Field(default=None)
    """
    ETA of job to finish in seconds
    """

    status: typing.Optional[JobStatus] = pydantic.Field(default=None)
    """
    Denotes the current status of the job in the queue
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
