

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mutable_oa1three_legged_client_endpoints import MutableOa1ThreeLeggedClientEndpoints
from .mutable_oa2authorization_code_client_endpoints import MutableOa2AuthorizationCodeClientEndpoints
from .mutable_session_auth_client_endpoints import MutableSessionAuthClientEndpoints
from .owner import Owner
from .session_field import SessionField


class MutableAuthClient_Oa1TwoLegged(UniversalBaseModel):
    type: typing.Literal["OA1_TWO_LEGGED"] = "OA1_TWO_LEGGED"
    name: str
    owners: typing.List[Owner]
    preprocessor: typing.Optional[str] = None
    tenant: typing.Optional[str] = None
    consumer_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="consumerKey"), pydantic.Field(alias="consumerKey")
    ]
    consumer_secret: typing_extensions.Annotated[
        str, FieldMetadata(alias="consumerSecret"), pydantic.Field(alias="consumerSecret")
    ]
    nonce: str
    signature: str
    signature_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="signatureMethod"), pydantic.Field(alias="signatureMethod")
    ]
    verifier: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MutableAuthClient_Oa1ThreeLegged(UniversalBaseModel):
    type: typing.Literal["OA1_THREE_LEGGED"] = "OA1_THREE_LEGGED"
    name: str
    owners: typing.List[Owner]
    preprocessor: typing.Optional[str] = None
    tenant: typing.Optional[str] = None
    app_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="appName"), pydantic.Field(alias="appName")
    ] = None
    key: str
    secret: str
    nonce: typing.Optional[str] = None
    signature: typing.Optional[str] = None
    signature_method: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="signatureMethod"), pydantic.Field(alias="signatureMethod")
    ] = None
    endpoints: typing.Optional[MutableOa1ThreeLeggedClientEndpoints] = None
    redirect_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="redirectUri"), pydantic.Field(alias="redirectUri")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MutableAuthClient_Oa2AuthorizationCode(UniversalBaseModel):
    type: typing.Literal["OA2_AUTHORIZATION_CODE"] = "OA2_AUTHORIZATION_CODE"
    name: str
    owners: typing.List[Owner]
    preprocessor: typing.Optional[str] = None
    tenant: typing.Optional[str] = None
    client_id: typing_extensions.Annotated[str, FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId")]
    client_secret: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientSecret"), pydantic.Field(alias="clientSecret")
    ]
    redirect_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="redirectUri"), pydantic.Field(alias="redirectUri")
    ]
    refresh_with_scope: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="refreshWithScope"), pydantic.Field(alias="refreshWithScope")
    ] = None
    endpoints: MutableOa2AuthorizationCodeClientEndpoints
    predefined_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="predefinedScope"), pydantic.Field(alias="predefinedScope")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MutableAuthClient_SessionAuth(UniversalBaseModel):
    type: typing.Literal["SESSION_AUTH"] = "SESSION_AUTH"
    name: str
    owners: typing.List[Owner]
    preprocessor: typing.Optional[str] = None
    tenant: typing.Optional[str] = None
    fields: typing.List[SessionField]
    token_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tokenPath"), pydantic.Field(alias="tokenPath")
    ] = None
    expiration_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="expirationPath"), pydantic.Field(alias="expirationPath")
    ] = None
    endpoints: MutableSessionAuthClientEndpoints

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MutableAuthClient = typing_extensions.Annotated[
    typing.Union[
        MutableAuthClient_Oa1TwoLegged,
        MutableAuthClient_Oa1ThreeLegged,
        MutableAuthClient_Oa2AuthorizationCode,
        MutableAuthClient_SessionAuth,
    ],
    pydantic.Field(discriminator="type"),
]
