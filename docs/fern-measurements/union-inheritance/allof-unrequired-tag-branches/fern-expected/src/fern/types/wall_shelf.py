

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wall_shelf_type import WallShelfType


class WallShelf(UniversalBaseModel):
    type: typing.Optional[WallShelfType] = pydantic.Field(default=None)
    """
    Mounted on the wall.
    """

    brackets: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
