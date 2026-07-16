

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .geofence_attributes import GeofenceAttributes


class Geofence(UniversalBaseModel):
    area: typing.Optional[str] = None
    attributes: typing.Optional[GeofenceAttributes] = None
    calendar_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="calendarId"), pydantic.Field(alias="calendarId")
    ] = None
    description: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
