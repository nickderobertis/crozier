

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .feed_channels_response_item_count import FeedChannelsResponseItemCount
from .feed_channels_response_item_notify_frequency import FeedChannelsResponseItemNotifyFrequency


class FeedChannelsResponseItem(UniversalBaseModel):
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    name: str
    webhook_signature: typing_extensions.Annotated[
        str, FieldMetadata(alias="webhookSignature"), pydantic.Field(alias="webhookSignature")
    ]
    notify_frequency: typing_extensions.Annotated[
        FeedChannelsResponseItemNotifyFrequency,
        FieldMetadata(alias="notifyFrequency"),
        pydantic.Field(alias="notifyFrequency"),
    ]
    public_share_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publicShareId"), pydantic.Field(alias="publicShareId")
    ] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    count: typing_extensions.Annotated[
        FeedChannelsResponseItemCount, FieldMetadata(alias="_count"), pydantic.Field(alias="_count")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
