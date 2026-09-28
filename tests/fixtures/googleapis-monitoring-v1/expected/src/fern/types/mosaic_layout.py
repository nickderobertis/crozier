

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tile import Tile


class MosaicLayout(UniversalBaseModel):
    """
    A mosaic layout divides the available space into a grid of blocks, and overlays the grid with tiles. Unlike GridLayout, tiles may span multiple grid blocks and can be placed at arbitrary locations in the grid.
    """

    columns: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of columns in the mosaic grid. The number of columns must be between 1 and 12, inclusive.
    """

    tiles: typing.Optional[typing.List[Tile]] = pydantic.Field(default=None)
    """
    The tiles to display.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
