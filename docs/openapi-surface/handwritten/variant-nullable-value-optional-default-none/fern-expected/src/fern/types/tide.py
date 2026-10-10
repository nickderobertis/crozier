

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Tide_Gauge(UniversalBaseModel):
    source: typing.Literal["gauge"] = "gauge"
    height_cm: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="heightCm"), pydantic.Field(alias="heightCm")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Tide_Almanac(UniversalBaseModel):
    source: typing.Literal["almanac"] = "almanac"
    height_cm: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="heightCm"), pydantic.Field(alias="heightCm")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Tide = typing_extensions.Annotated[typing.Union[Tide_Gauge, Tide_Almanac], pydantic.Field(discriminator="source")]
