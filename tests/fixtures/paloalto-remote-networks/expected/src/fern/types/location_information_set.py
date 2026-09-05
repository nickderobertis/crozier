

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bandwidth_allocation_set import BandwidthAllocationSet
from .location_region_info_set import LocationRegionInfoSet


class LocationInformationSet(UniversalBaseModel):
    """
    information for a set of locations
    """

    bandwidth_allocations: typing.Optional[BandwidthAllocationSet] = None
    info_type: typing.Optional[str] = None
    location_region_info: typing.Optional[LocationRegionInfoSet] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
