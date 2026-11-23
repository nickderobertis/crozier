

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Signal_Flag(UniversalBaseModel):
    """
    Every signal, discriminated by `type` over typed one-value enums.
    """

    type: typing.Literal["flag"] = "flag"
    colour: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Signal_Lamp(UniversalBaseModel):
    """
    Every signal, discriminated by `type` over typed one-value enums.
    """

    type: typing.Literal["lamp"] = "lamp"
    flashes: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Signal = typing_extensions.Annotated[typing.Union[Signal_Flag, Signal_Lamp], pydantic.Field(discriminator="type")]
