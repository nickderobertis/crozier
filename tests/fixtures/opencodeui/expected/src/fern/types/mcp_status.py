

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class McpStatus_Connected(UniversalBaseModel):
    status: typing.Literal["connected"] = "connected"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class McpStatus_Disabled(UniversalBaseModel):
    status: typing.Literal["disabled"] = "disabled"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class McpStatus_Failed(UniversalBaseModel):
    status: typing.Literal["failed"] = "failed"
    error: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class McpStatus_NeedsAuth(UniversalBaseModel):
    status: typing.Literal["needs_auth"] = "needs_auth"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class McpStatus_NeedsClientRegistration(UniversalBaseModel):
    status: typing.Literal["needs_client_registration"] = "needs_client_registration"
    error: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


McpStatus = typing_extensions.Annotated[
    typing.Union[
        McpStatus_Connected,
        McpStatus_Disabled,
        McpStatus_Failed,
        McpStatus_NeedsAuth,
        McpStatus_NeedsClientRegistration,
    ],
    pydantic.Field(discriminator="status"),
]
