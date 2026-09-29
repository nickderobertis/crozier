

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LocationPoint(UniversalBaseModel):
    """
    GeoProperty. Geojson reference to the item. Point
    """

    bbox: typing.Optional[typing.List[float]] = None
    coordinates: typing.List[float]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
