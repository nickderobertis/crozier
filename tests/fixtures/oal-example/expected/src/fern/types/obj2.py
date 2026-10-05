

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .obj1 import Obj1


class Obj2(Obj1):
    age: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
