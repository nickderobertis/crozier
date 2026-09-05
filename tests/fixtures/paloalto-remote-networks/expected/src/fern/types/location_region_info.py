

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .location import Location


class LocationRegionInfo(UniversalBaseModel):
    compute_location: str = pydantic.Field()
    """
    aggregate compute region
    """

    edge_location: str = pydantic.Field()
    """
    edge location for given lat/long/ip
    """

    location: Location

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
