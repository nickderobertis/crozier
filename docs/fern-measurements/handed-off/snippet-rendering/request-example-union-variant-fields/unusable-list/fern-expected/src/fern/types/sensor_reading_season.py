

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .autumn_season_phase import AutumnSeasonPhase
from .spring_season_phase import SpringSeasonPhase


class SensorReadingSeason_Spring(UniversalBaseModel):
    kind: typing.Literal["spring"] = "spring"
    phase: SpringSeasonPhase

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SensorReadingSeason_Autumn(UniversalBaseModel):
    kind: typing.Literal["autumn"] = "autumn"
    phase: AutumnSeasonPhase

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SensorReadingSeason = typing_extensions.Annotated[
    typing.Union[SensorReadingSeason_Spring, SensorReadingSeason_Autumn], pydantic.Field(discriminator="kind")
]
