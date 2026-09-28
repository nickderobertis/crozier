

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_from_websocket_content_type import ChannelFromWebsocketContentType
from .channel_from_websocket_headers import ChannelFromWebsocketHeaders


class ChannelFrom_App(UniversalBaseModel):
    type: typing.Literal["app"] = "app"
    user: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChannelFrom_Phone(UniversalBaseModel):
    type: typing.Literal["phone"] = "phone"
    number: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChannelFrom_Sip(UniversalBaseModel):
    type: typing.Literal["sip"] = "sip"
    uri: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChannelFrom_Websocket(UniversalBaseModel):
    type: typing.Literal["websocket"] = "websocket"
    content_type: typing_extensions.Annotated[
        ChannelFromWebsocketContentType, FieldMetadata(alias="content-type"), pydantic.Field(alias="content-type")
    ]
    headers: typing.Optional[ChannelFromWebsocketHeaders] = None
    uri: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChannelFrom_Vbc(UniversalBaseModel):
    type: typing.Literal["vbc"] = "vbc"
    extension: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChannelFrom = typing_extensions.Annotated[
    typing.Union[ChannelFrom_App, ChannelFrom_Phone, ChannelFrom_Sip, ChannelFrom_Websocket, ChannelFrom_Vbc],
    pydantic.Field(discriminator="type"),
]
