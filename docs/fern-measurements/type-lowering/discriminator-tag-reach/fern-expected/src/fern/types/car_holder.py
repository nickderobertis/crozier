

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .car_holder_type import CarHolderType
from .person import Person


class CarHolder(Person):
    type: typing.Optional[CarHolderType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
