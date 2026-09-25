

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.event_type import EventType


class CreateWebhookResponse(UniversalBaseModel):
    id: typing.Optional[str] = None
    url: typing.Optional[str] = None
    event_types: typing_extensions.Annotated[
        typing.Optional[typing.List[EventType]], FieldMetadata(alias="eventTypes"), pydantic.Field(alias="eventTypes")
    ] = None
    is_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isEnabled"), pydantic.Field(alias="isEnabled")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
