

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChartTileLayoutPosition(UniversalBaseModel):
    """
    Position of the tile in the dashboard's grid.  Numbering starts at 0, so a tile in the upper left of the dashboard will be at column 0, row 0.
    """

    col: int
    row: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
