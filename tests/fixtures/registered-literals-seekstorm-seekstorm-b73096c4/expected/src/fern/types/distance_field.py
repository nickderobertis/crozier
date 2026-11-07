

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .distance_unit import DistanceUnit
from .vec import Vec


class DistanceField(UniversalBaseModel):
    """
    DistanceField defines a field for proximity search.
    """

    field: str = pydantic.Field()
    """
    field name of a numeric facet field (currently onyl Point field type supported)
    """

    distance: str = pydantic.Field()
    """
    field name of the distance field we are deriving from the numeric facet field (Point type) and the base (Point type)
    """

    base: Vec = pydantic.Field()
    """
    base point (lat,lon) for distance calculation
    """

    unit: DistanceUnit = pydantic.Field()
    """
    distance unit for the distance field: kilometers or miles
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
