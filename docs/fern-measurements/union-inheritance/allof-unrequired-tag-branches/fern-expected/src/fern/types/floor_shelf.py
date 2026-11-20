

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .floor_shelf_type import FloorShelfType


class FloorShelf(UniversalBaseModel):
    type: typing.Optional[FloorShelfType] = pydantic.Field(default=None)
    """
    Standing on the floor.
    """

    height: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
