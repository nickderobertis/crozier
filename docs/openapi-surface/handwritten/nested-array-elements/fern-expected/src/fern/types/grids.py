

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .blank_grid import BlankGrid
from .mixed_grid import MixedGrid


class Grids(UniversalBaseModel):
    mixed: typing.Optional[MixedGrid] = None
    blank: typing.Optional[BlankGrid] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
