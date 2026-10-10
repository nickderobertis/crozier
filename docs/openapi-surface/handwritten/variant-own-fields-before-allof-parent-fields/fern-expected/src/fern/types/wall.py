

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Wall_Gravity(UniversalBaseModel):
    build: typing.Literal["gravity"] = "gravity"
    base_m: typing_extensions.Annotated[float, FieldMetadata(alias="baseM"), pydantic.Field(alias="baseM")]
    inspector: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Wall_Embankment(UniversalBaseModel):
    build: typing.Literal["embankment"] = "embankment"
    inspector: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Wall = typing_extensions.Annotated[typing.Union[Wall_Gravity, Wall_Embankment], pydantic.Field(discriminator="build")]
