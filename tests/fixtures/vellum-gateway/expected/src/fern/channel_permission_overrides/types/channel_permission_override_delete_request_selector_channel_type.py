

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .channel_permission_override_delete_request_selector_channel_type_channel_type import (
    ChannelPermissionOverrideDeleteRequestSelectorChannelTypeChannelType,
)


class ChannelPermissionOverrideDeleteRequestSelectorChannelType(UniversalBaseModel):
    adapter: str
    channel_type: typing_extensions.Annotated[
        ChannelPermissionOverrideDeleteRequestSelectorChannelTypeChannelType,
        FieldMetadata(alias="channelType"),
        pydantic.Field(alias="channelType"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
