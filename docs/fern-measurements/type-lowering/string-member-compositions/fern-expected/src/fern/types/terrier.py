

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .animal import Animal
from .terrier_size import TerrierSize


class Terrier(Animal):
    digs: typing.Optional[bool] = None
    size: typing.Optional[TerrierSize] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
