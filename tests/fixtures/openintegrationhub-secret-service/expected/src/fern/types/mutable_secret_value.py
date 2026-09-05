

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MutableSecretValue_Simple(UniversalBaseModel):
    type: typing.Literal["SIMPLE"] = "SIMPLE"
    username: str
    passphrase: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MutableSecretValue_Mixed(UniversalBaseModel):
    type: typing.Literal["MIXED"] = "MIXED"
    payload: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MutableSecretValue_ApiKey(UniversalBaseModel):
    type: typing.Literal["API_KEY"] = "API_KEY"
    key: str
    header_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="headerName"), pydantic.Field(alias="headerName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MutableSecretValue_SessionAuth(UniversalBaseModel):
    type: typing.Literal["SESSION_AUTH"] = "SESSION_AUTH"
    auth_client_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="authClientId"), pydantic.Field(alias="authClientId")
    ]
    access_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="accessToken"), pydantic.Field(alias="accessToken")
    ] = None
    input_fields: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="inputFields"), pydantic.Field(alias="inputFields")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MutableSecretValue_Oa1TwoLegged(UniversalBaseModel):
    type: typing.Literal["OA1_TWO_LEGGED"] = "OA1_TWO_LEGGED"
    expires_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MutableSecretValue_Oa1ThreeLegged(UniversalBaseModel):
    type: typing.Literal["OA1_THREE_LEGGED"] = "OA1_THREE_LEGGED"
    auth_client_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="authClientId"), pydantic.Field(alias="authClientId")
    ]
    access_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="accessToken"), pydantic.Field(alias="accessToken")
    ]
    access_token_secret: typing_extensions.Annotated[
        str, FieldMetadata(alias="accessTokenSecret"), pydantic.Field(alias="accessTokenSecret")
    ]
    scope: typing.Optional[str] = None
    expires: typing.Optional[str] = None
    external_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="externalId"), pydantic.Field(alias="externalId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MutableSecretValue_Oa2AuthorizationCode(UniversalBaseModel):
    type: typing.Literal["OA2_AUTHORIZATION_CODE"] = "OA2_AUTHORIZATION_CODE"
    auth_client_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="authClientId"), pydantic.Field(alias="authClientId")
    ]
    refresh_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="refreshToken"), pydantic.Field(alias="refreshToken")
    ] = None
    access_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="accessToken"), pydantic.Field(alias="accessToken")
    ]
    scope: typing.Optional[str] = None
    expires: dt.datetime
    external_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="externalId"), pydantic.Field(alias="externalId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MutableSecretValue = typing_extensions.Annotated[
    typing.Union[
        MutableSecretValue_Simple,
        MutableSecretValue_Mixed,
        MutableSecretValue_ApiKey,
        MutableSecretValue_SessionAuth,
        MutableSecretValue_Oa1TwoLegged,
        MutableSecretValue_Oa1ThreeLegged,
        MutableSecretValue_Oa2AuthorizationCode,
    ],
    pydantic.Field(discriminator="type"),
]
