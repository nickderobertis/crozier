

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .channel_permission_override_delete_request_selector_channel_type_channel_type import (
    ChannelPermissionOverrideDeleteRequestSelectorChannelTypeChannelType,
)


class ChannelPermissionOverrideDeleteRequestSelector_Workspace(UniversalBaseModel):
    scope: typing.Literal["workspace"] = "workspace"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChannelPermissionOverrideDeleteRequestSelector_Adapter(UniversalBaseModel):
    scope: typing.Literal["adapter"] = "adapter"
    adapter: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChannelPermissionOverrideDeleteRequestSelector_ChannelType(UniversalBaseModel):
    scope: typing.Literal["channel_type"] = "channel_type"
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


class ChannelPermissionOverrideDeleteRequestSelector_Channel(UniversalBaseModel):
    scope: typing.Literal["channel"] = "channel"
    adapter: str
    channel_external_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="channelExternalId"), pydantic.Field(alias="channelExternalId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChannelPermissionOverrideDeleteRequestSelector = typing_extensions.Annotated[
    typing.Union[
        ChannelPermissionOverrideDeleteRequestSelector_Workspace,
        ChannelPermissionOverrideDeleteRequestSelector_Adapter,
        ChannelPermissionOverrideDeleteRequestSelector_ChannelType,
        ChannelPermissionOverrideDeleteRequestSelector_Channel,
    ],
    pydantic.Field(discriminator="scope"),
]
