

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GeoCoordinates(UniversalBaseModel):
    """
    Structure with the address geocoordinates. Optional for `delivery` orders, required for `pickup-in-point` orders.
    """

    latitude: str = pydantic.Field()
    """
    Double value with the latitude coordinates of the address. Required only if the geoCoordinates field is defined. 
    
    Example format: `-25.4158764`.
    """

    longitude: str = pydantic.Field()
    """
    Double value with the longitude coordinates of the address. Required only if the geoCoordinates field is defined. Example format: `-49.342759`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
