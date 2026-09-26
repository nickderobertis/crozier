

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .event_session_error_properties_error import EventSessionErrorPropertiesError


class EventSessionErrorProperties(UniversalBaseModel):
    session_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")
    ] = None
    error: typing.Optional[EventSessionErrorPropertiesError] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
