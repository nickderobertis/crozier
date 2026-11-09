

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChartTileLayoutSize(UniversalBaseModel):
    """
    Number of columns and rows the tile occupies.  A dashboard always has 6 columns, but has as many rows as needed to accommodate the given tiles.
    """

    cols: int
    rows: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
