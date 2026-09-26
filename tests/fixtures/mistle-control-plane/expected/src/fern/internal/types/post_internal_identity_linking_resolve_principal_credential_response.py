

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalIdentityLinkingResolvePrincipalCredentialResponse_Value(UniversalBaseModel):
    kind: typing.Literal["value"] = "value"
    value: str
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostInternalIdentityLinkingResolvePrincipalCredentialResponse_AwsSession(UniversalBaseModel):
    kind: typing.Literal["aws_session"] = "aws_session"
    access_key_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="accessKeyId"), pydantic.Field(alias="accessKeyId")
    ]
    secret_access_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="secretAccessKey"), pydantic.Field(alias="secretAccessKey")
    ]
    session_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="sessionToken"), pydantic.Field(alias="sessionToken")
    ]
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostInternalIdentityLinkingResolvePrincipalCredentialResponse = typing_extensions.Annotated[
    typing.Union[
        PostInternalIdentityLinkingResolvePrincipalCredentialResponse_Value,
        PostInternalIdentityLinkingResolvePrincipalCredentialResponse_AwsSession,
    ],
    pydantic.Field(discriminator="kind"),
]
