

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .patch_me_tokens_response_type import PatchMeTokensResponseType


class PatchMeTokensResponse(UniversalBaseModel):
    token: str
    id: str
    type: PatchMeTokensResponseType
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    used_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="usedAt"), pydantic.Field(alias="usedAt")
    ] = None
    user_agent: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userAgent"), pydantic.Field(alias="userAgent")
    ] = None
    me: bool
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
