

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .feed_update_channel_info_response_notify_frequency import FeedUpdateChannelInfoResponseNotifyFrequency


class FeedUpdateChannelInfoResponse(UniversalBaseModel):
    notification_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="notificationIds"), pydantic.Field(alias="notificationIds")
    ]
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    name: str
    webhook_signature: typing_extensions.Annotated[
        str, FieldMetadata(alias="webhookSignature"), pydantic.Field(alias="webhookSignature")
    ]
    notify_frequency: typing_extensions.Annotated[
        FeedUpdateChannelInfoResponseNotifyFrequency,
        FieldMetadata(alias="notifyFrequency"),
        pydantic.Field(alias="notifyFrequency"),
    ]
    public_share_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publicShareId"), pydantic.Field(alias="publicShareId")
    ] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
