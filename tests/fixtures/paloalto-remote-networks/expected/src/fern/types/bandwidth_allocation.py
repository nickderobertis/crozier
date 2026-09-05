

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .location import Location


class BandwidthAllocation(UniversalBaseModel):
    bandwidth: str = pydantic.Field()
    """
    bandwidth to allocate in Mbps
    """

    compute_location: typing.Optional[str] = pydantic.Field(default=None)
    """
    aggregate compute region
    """

    edge_location: typing.Optional[str] = pydantic.Field(default=None)
    """
    edge location for given lat/long/ip
    """

    ipsec_node_list: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ipsec node list
    """

    location: Location

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
