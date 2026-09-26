

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalIntegrationCredentialsResolveResponseAwsSession(UniversalBaseModel):
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
