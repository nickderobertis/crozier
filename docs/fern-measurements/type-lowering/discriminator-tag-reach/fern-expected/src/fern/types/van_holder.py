

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .person import Person
from .van_holder_type import VanHolderType


class VanHolder(Person):
    type: typing.Optional[VanHolderType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
