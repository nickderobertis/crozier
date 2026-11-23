

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Pet(UniversalBaseModel):
    name: typing.Optional[str] = None
    age: typing.Optional[int] = None
    species: typing.Optional[str] = None
    breed: typing.Optional[str] = None
    size: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
