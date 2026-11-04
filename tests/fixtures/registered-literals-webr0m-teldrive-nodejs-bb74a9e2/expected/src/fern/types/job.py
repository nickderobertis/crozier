

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_attempt_error import JobAttemptError
from .job_state import JobState


class Job(UniversalBaseModel):
    id: str
    status: JobState
    type: str
    parent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    queue: str
    description: typing.Optional[str] = None
    message: typing.Optional[str] = None
    attempt: int
    max_attempts: typing_extensions.Annotated[
        int, FieldMetadata(alias="maxAttempts"), pydantic.Field(alias="maxAttempts")
    ]
    priority: int
    tags: typing.List[str]
    args: typing.Dict[str, typing.Any]
    output: typing.Optional[typing.Dict[str, typing.Any]] = None
    errors: typing.List[JobAttemptError]
    attempted_by: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="attemptedBy"), pydantic.Field(alias="attemptedBy")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    scheduled_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="scheduledAt"), pydantic.Field(alias="scheduledAt")
    ]
    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="completedAt"), pydantic.Field(alias="completedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
