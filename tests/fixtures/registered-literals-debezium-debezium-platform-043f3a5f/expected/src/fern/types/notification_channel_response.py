

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_type import ChannelType
from .instant import Instant


class NotificationChannelResponse(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    type: typing.Optional[ChannelType] = None
    config: typing.Optional[typing.Dict[str, typing.Any]] = None
    enabled: typing.Optional[bool] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[Instant], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[Instant], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
