

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bounding_box import BoundingBox


class MunicipalityProperties(UniversalBaseModel):
    """
    Municipality GeoJSON properties
    """

    name: str = pydantic.Field()
    """
    Municipality name
    """

    search_distance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="searchDistance"),
        pydantic.Field(alias="searchDistance", description="Search distance in metres"),
    ]
    """
    Search distance in metres
    """

    bounds: BoundingBox
    date_last_check: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="dateLastCheck"),
        pydantic.Field(alias="dateLastCheck", description="The last validated date."),
    ]
    """
    The last validated date.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
