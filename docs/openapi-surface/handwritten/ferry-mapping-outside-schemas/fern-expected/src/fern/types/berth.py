

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Berth_Vehicle(UniversalBaseModel):
    value: typing.Any
    category: typing.Literal["vehicle"] = "vehicle"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class Berth_Cabin(UniversalBaseModel):
    value: typing.Any
    category: typing.Literal["cabin"] = "cabin"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class Berth_Deck(UniversalBaseModel):
    value: typing.Any
    category: typing.Literal["deck"] = "deck"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


Berth = typing_extensions.Annotated[
    typing.Union[Berth_Vehicle, Berth_Cabin, Berth_Deck], pydantic.Field(discriminator="category")
]
