

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .geometry import Geometry
from .properties_bin_grid_corners import PropertiesBinGridCorners


class AbstractFeature(UniversalBaseModel):
    geometry: typing.Optional[Geometry] = None
    properties: typing.Optional[PropertiesBinGridCorners] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
