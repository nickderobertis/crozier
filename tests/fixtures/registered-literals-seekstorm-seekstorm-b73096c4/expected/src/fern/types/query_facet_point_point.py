

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .distance_unit import DistanceUnit
from .range_type import RangeType
from .vec import Vec


class QueryFacetPointPoint(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type Point (distance between base of type Point and facet field of type Point)
    """

    field: str = pydantic.Field()
    """
    field name
    """

    range_type: RangeType = pydantic.Field()
    """
    range type (CountWithinRange,CountBelowRange,CountAboveRange)
    """

    ranges: typing.List[typing.List[typing.Any]] = pydantic.Field()
    """
    range label, range start
    """

    base: Vec = pydantic.Field()
    """
    base point (latitude/lat, longitude/lon)
    """

    unit: DistanceUnit = pydantic.Field()
    """
    distance unit (kilometers/miles)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
