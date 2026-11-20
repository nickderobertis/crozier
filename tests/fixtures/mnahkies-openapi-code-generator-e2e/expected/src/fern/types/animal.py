

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Animal_Cat(UniversalBaseModel):
    type: typing.Literal["cat"] = "cat"
    name: typing.Optional[str] = None
    lives: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Animal_Dog(UniversalBaseModel):
    type: typing.Literal["dog"] = "dog"
    name: typing.Optional[str] = None
    sticks: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Animal = typing_extensions.Annotated[typing.Union[Animal_Cat, Animal_Dog], pydantic.Field(discriminator="type")]
