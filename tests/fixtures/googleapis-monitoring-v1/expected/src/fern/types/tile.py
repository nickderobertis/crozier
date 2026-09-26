

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .widget import Widget


class Tile(UniversalBaseModel):
    """
    A single tile in the mosaic. The placement and size of the tile are configurable.
    """

    height: typing.Optional[int] = pydantic.Field(default=None)
    """
    The height of the tile, measured in grid blocks. Tiles must have a minimum height of 1.
    """

    widget: typing.Optional[Widget] = pydantic.Field(default=None)
    """
    The informational widget contained in the tile. For example an XyChart.
    """

    width: typing.Optional[int] = pydantic.Field(default=None)
    """
    The width of the tile, measured in grid blocks. Tiles must have a minimum width of 1.
    """

    x_pos: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="xPos"),
        pydantic.Field(
            alias="xPos",
            description="The zero-indexed position of the tile in grid blocks relative to the left edge of the grid. Tiles must be contained within the specified number of columns. x_pos cannot be negative.",
        ),
    ] = None
    """
    The zero-indexed position of the tile in grid blocks relative to the left edge of the grid. Tiles must be contained within the specified number of columns. x_pos cannot be negative.
    """

    y_pos: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="yPos"),
        pydantic.Field(
            alias="yPos",
            description="The zero-indexed position of the tile in grid blocks relative to the top edge of the grid. y_pos cannot be negative.",
        ),
    ] = None
    """
    The zero-indexed position of the tile in grid blocks relative to the top edge of the grid. y_pos cannot be negative.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
