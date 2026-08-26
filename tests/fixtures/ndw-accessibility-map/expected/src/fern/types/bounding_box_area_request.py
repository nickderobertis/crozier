

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .latitude import Latitude
from .longitude import Longitude


class BoundingBoxAreaRequest(UniversalBaseModel):
    min_latitude: typing_extensions.Annotated[
        Latitude, FieldMetadata(alias="minLatitude"), pydantic.Field(alias="minLatitude")
    ]
    max_latitude: typing_extensions.Annotated[
        Longitude, FieldMetadata(alias="maxLatitude"), pydantic.Field(alias="maxLatitude")
    ]
    min_longitude: typing_extensions.Annotated[
        Latitude, FieldMetadata(alias="minLongitude"), pydantic.Field(alias="minLongitude")
    ]
    max_longitude: typing_extensions.Annotated[
        Longitude, FieldMetadata(alias="maxLongitude"), pydantic.Field(alias="maxLongitude")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
