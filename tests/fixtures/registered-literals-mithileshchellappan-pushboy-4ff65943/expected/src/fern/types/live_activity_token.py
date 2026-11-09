

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .live_activity_token_type import LiveActivityTokenType
from .platform import Platform


class LiveActivityToken(UniversalBaseModel):
    id: typing_extensions.Annotated[str, FieldMetadata(alias="ID"), pydantic.Field(alias="ID")]
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="UserID"), pydantic.Field(alias="UserID")]
    platform: typing_extensions.Annotated[Platform, FieldMetadata(alias="Platform"), pydantic.Field(alias="Platform")]
    token_type: typing_extensions.Annotated[
        LiveActivityTokenType, FieldMetadata(alias="TokenType"), pydantic.Field(alias="TokenType")
    ]
    token: typing_extensions.Annotated[str, FieldMetadata(alias="Token"), pydantic.Field(alias="Token")]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="CreatedAt"), pydantic.Field(alias="CreatedAt")]
    last_seen_at: typing_extensions.Annotated[
        str, FieldMetadata(alias="LastSeenAt"), pydantic.Field(alias="LastSeenAt")
    ]
    expires_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ExpiresAt"), pydantic.Field(alias="ExpiresAt")
    ] = None
    invalidated_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="InvalidatedAt"), pydantic.Field(alias="InvalidatedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
