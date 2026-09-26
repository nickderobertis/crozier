

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .components_schemas_channel_properties_from_one_of3content_type import (
    ComponentsSchemasChannelPropertiesFromOneOf3ContentType,
)
from .components_schemas_channel_properties_from_one_of3headers import (
    ComponentsSchemasChannelPropertiesFromOneOf3Headers,
)


class ChannelTo_App(UniversalBaseModel):
    type: typing.Literal["app"] = "app"
    user: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChannelTo_Phone(UniversalBaseModel):
    type: typing.Literal["phone"] = "phone"
    dtmf_answer: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dtmfAnswer"), pydantic.Field(alias="dtmfAnswer")
    ] = None
    number: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChannelTo_Sip(UniversalBaseModel):
    type: typing.Literal["sip"] = "sip"
    uri: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChannelTo_Websocket(UniversalBaseModel):
    type: typing.Literal["websocket"] = "websocket"
    content_type: typing_extensions.Annotated[
        ComponentsSchemasChannelPropertiesFromOneOf3ContentType,
        FieldMetadata(alias="content-type"),
        pydantic.Field(alias="content-type"),
    ]
    headers: typing.Optional[ComponentsSchemasChannelPropertiesFromOneOf3Headers] = None
    uri: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChannelTo_Vbc(UniversalBaseModel):
    type: typing.Literal["vbc"] = "vbc"
    extension: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChannelTo = typing_extensions.Annotated[
    typing.Union[ChannelTo_App, ChannelTo_Phone, ChannelTo_Sip, ChannelTo_Websocket, ChannelTo_Vbc],
    pydantic.Field(discriminator="type"),
]
