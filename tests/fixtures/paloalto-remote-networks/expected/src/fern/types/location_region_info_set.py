

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .location_region_info import LocationRegionInfo


class LocationRegionInfoSet(UniversalBaseModel):
    regions_info: typing.Optional[typing.List[LocationRegionInfo]] = pydantic.Field(default=None)
    """
    regions mapped info
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
