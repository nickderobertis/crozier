

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ignores_ignore_response import IgnoresIgnoreResponse


class UserUserToUserContext(UniversalBaseModel):
    global_ignore_end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="globalIgnoreEndDate"),
        pydantic.Field(alias="globalIgnoreEndDate"),
    ] = None
    ignore_status: typing_extensions.Annotated[
        typing.Optional[IgnoresIgnoreResponse],
        FieldMetadata(alias="ignoreStatus"),
        pydantic.Field(alias="ignoreStatus"),
    ] = None
    is_following: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isFollowing"), pydantic.Field(alias="isFollowing")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
