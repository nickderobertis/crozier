

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Stove_Wood(UniversalBaseModel):
    burns: typing.Literal["wood"] = "wood"
    flue_cm: typing_extensions.Annotated[int, FieldMetadata(alias="flueCm"), pydantic.Field(alias="flueCm")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Stove_Pellet(UniversalBaseModel):
    burns: typing.Literal["pellet"] = "pellet"
    hopper_kg: typing_extensions.Annotated[float, FieldMetadata(alias="hopperKg"), pydantic.Field(alias="hopperKg")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Stove = typing_extensions.Annotated[typing.Union[Stove_Wood, Stove_Pellet], pydantic.Field(discriminator="burns")]
