

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Box(UniversalBaseModel):
    """
    Axis-aligned bounding box in normalized page coordinates.

    Every value is a fraction of the page's width (`xmin`/`xmax`) or height
    (`ymin`/`ymax`) in `[0, 1]`, with at most 8 decimal places. To convert to
    pixels, multiply by the dimensions of whatever raster of the page you are
    drawing on. Coordinates are clamped and rounded at construction so the
    in-process value always equals the serialized one.
    """

    xmin: float = pydantic.Field()
    """
    Left edge as a fraction of the page width, in `[0, 1]`.
    """

    ymin: float = pydantic.Field()
    """
    Top edge as a fraction of the page height, in `[0, 1]`.
    """

    xmax: float = pydantic.Field()
    """
    Right edge as a fraction of the page width, in `[0, 1]`.
    """

    ymax: float = pydantic.Field()
    """
    Bottom edge as a fraction of the page height, in `[0, 1]`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
