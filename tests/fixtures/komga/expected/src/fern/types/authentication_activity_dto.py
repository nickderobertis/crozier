

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthenticationActivityDto(UniversalBaseModel):
    api_key_comment: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiKeyComment"), pydantic.Field(alias="apiKeyComment")
    ] = None
    api_key_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiKeyId"), pydantic.Field(alias="apiKeyId")
    ] = None
    date_time: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="dateTime"), pydantic.Field(alias="dateTime")
    ]
    email: typing.Optional[str] = None
    error: typing.Optional[str] = None
    ip: typing.Optional[str] = None
    source: typing.Optional[str] = None
    success: bool
    user_agent: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userAgent"), pydantic.Field(alias="userAgent")
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
