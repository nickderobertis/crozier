

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extent_spatial import ExtentSpatial
from .extent_temporal import ExtentTemporal


class Extent(UniversalBaseModel):
    """
    The extent of the features in the collection. In the Core only spatial and temporal
    extents are specified. Extensions may add additional members to represent other
    extents, for example, thermal or pressure ranges.
    """

    spatial: typing.Optional[ExtentSpatial] = pydantic.Field(default=None)
    """
    The spatial extent of the features in the collection.
    """

    temporal: typing.Optional[ExtentTemporal] = pydantic.Field(default=None)
    """
    The temporal extent of the features in the collection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
