

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .latitude import Latitude
from .longitude import Longitude


class Geocode(UniversalBaseModel):
    altitude: typing.Optional[float] = None
    captured_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="capturedAt"), pydantic.Field(alias="capturedAt")
    ]
    lat: Latitude
    lng: Longitude

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
