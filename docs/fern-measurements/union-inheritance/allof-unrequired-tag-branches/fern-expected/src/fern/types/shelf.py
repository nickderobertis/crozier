

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .shelf_base import ShelfBase
from .shelf_type import ShelfType


class Shelf(ShelfBase):
    type: typing.Optional[ShelfType] = pydantic.Field(default=None)
    """
    Mounted on the wall.
    """

    brackets: typing.Optional[int] = None
    height: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
