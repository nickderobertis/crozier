

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .uuid_ import Uuid


class SessionSummary(UniversalBaseModel):
    id: Uuid
    current: bool
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    last_used_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastUsedAt"), pydantic.Field(alias="lastUsedAt")
    ] = None
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]
    revoked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="revokedAt"), pydantic.Field(alias="revokedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
