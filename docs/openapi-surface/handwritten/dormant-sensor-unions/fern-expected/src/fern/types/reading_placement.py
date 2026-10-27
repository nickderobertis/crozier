

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reading_placement_band import ReadingPlacementBand


class ReadingPlacement(UniversalBaseModel):
    band: typing.Optional[ReadingPlacementBand] = pydantic.Field(default=None)
    """
    How far the sensor reaches.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
