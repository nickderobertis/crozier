

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notification_payload import NotificationPayload
from .publish_job_status import PublishJobStatus


class PublishJob(UniversalBaseModel):
    id: typing_extensions.Annotated[str, FieldMetadata(alias="ID"), pydantic.Field(alias="ID")]
    topic_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="TopicID"), pydantic.Field(alias="TopicID")
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="UserID"), pydantic.Field(alias="UserID")
    ] = None
    payload: typing_extensions.Annotated[
        typing.Optional[NotificationPayload], FieldMetadata(alias="Payload"), pydantic.Field(alias="Payload")
    ] = None
    status: typing_extensions.Annotated[PublishJobStatus, FieldMetadata(alias="Status"), pydantic.Field(alias="Status")]
    total_count: typing_extensions.Annotated[int, FieldMetadata(alias="TotalCount"), pydantic.Field(alias="TotalCount")]
    success_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="SuccessCount"), pydantic.Field(alias="SuccessCount")
    ]
    failure_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="FailureCount"), pydantic.Field(alias="FailureCount")
    ]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="CreatedAt"), pydantic.Field(alias="CreatedAt")]
    completed_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="CompletedAt"), pydantic.Field(alias="CompletedAt")
    ] = None
    scheduled_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ScheduledAt"), pydantic.Field(alias="ScheduledAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
