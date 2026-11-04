

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .in_ import In
from .o_auth_flows import OAuthFlows


class SecuritySchemeInput_ApiKey(UniversalBaseModel):
    type: typing.Literal["apiKey"] = "apiKey"
    description: typing.Optional[str] = None
    in_: typing_extensions.Annotated[In, FieldMetadata(alias="in"), pydantic.Field(alias="in")]
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SecuritySchemeInput_Http(UniversalBaseModel):
    type: typing.Literal["http"] = "http"
    bearer_format: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bearerFormat"), pydantic.Field(alias="bearerFormat")
    ] = None
    description: typing.Optional[str] = None
    scheme: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SecuritySchemeInput_Oauth2(UniversalBaseModel):
    type: typing.Literal["oauth2"] = "oauth2"
    description: typing.Optional[str] = None
    flows: OAuthFlows
    oauth2metadata_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oauth2MetadataUrl"), pydantic.Field(alias="oauth2MetadataUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SecuritySchemeInput_OpenIdConnect(UniversalBaseModel):
    type: typing.Literal["openIdConnect"] = "openIdConnect"
    description: typing.Optional[str] = None
    open_id_connect_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="openIdConnectUrl"), pydantic.Field(alias="openIdConnectUrl")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SecuritySchemeInput_MutualTls(UniversalBaseModel):
    type: typing.Literal["mutualTLS"] = "mutualTLS"
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SecuritySchemeInput = typing_extensions.Annotated[
    typing.Union[
        SecuritySchemeInput_ApiKey,
        SecuritySchemeInput_Http,
        SecuritySchemeInput_Oauth2,
        SecuritySchemeInput_OpenIdConnect,
        SecuritySchemeInput_MutualTls,
    ],
    pydantic.Field(discriminator="type"),
]
