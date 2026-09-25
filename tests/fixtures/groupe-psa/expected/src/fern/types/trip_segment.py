

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .trip_segment_propulsion import TripSegmentPropulsion


class TripSegment(UniversalBaseModel):
    """
    Part of the trip crossed for a type of propulsion.
    """

    propulsion: typing.Optional[TripSegmentPropulsion] = pydantic.Field(default=None)
    """
    Propulsion during this trip segment.
    """

    percent: typing.Optional[float] = pydantic.Field(default=None)
    """
    Trip segment pecentage. _Unit: %_
    """

    distance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Distance driven during this trip segment. _Unit: Km_
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
