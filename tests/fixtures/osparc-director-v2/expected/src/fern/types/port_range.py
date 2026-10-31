

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .port_range_lower import PortRangeLower
from .port_range_upper import PortRangeUpper


class PortRange(UniversalBaseModel):
    """
    `lower` and `upper` are included
    """

    lower: PortRangeLower
    upper: PortRangeUpper

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
