

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Gadget_Lamp(UniversalBaseModel):
    kind: typing.Literal["LAMP"] = "LAMP"
    watts: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Gadget_Fan(UniversalBaseModel):
    kind: typing.Literal["FAN"] = "FAN"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Gadget_Dial(UniversalBaseModel):
    value: typing.Any
    kind: typing.Literal["DIAL"] = "DIAL"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class Gadget_Knob(UniversalBaseModel):
    value: typing.Any
    kind: typing.Literal["KNOB"] = "KNOB"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class Gadget_Slider(UniversalBaseModel):
    value: typing.Any
    kind: typing.Literal["SLIDER"] = "SLIDER"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


Gadget = typing_extensions.Annotated[
    typing.Union[Gadget_Lamp, Gadget_Fan, Gadget_Dial, Gadget_Knob, Gadget_Slider], pydantic.Field(discriminator="kind")
]
