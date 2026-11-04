

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SensorReadingChecksItem_Threshold(UniversalBaseModel):
    kind: typing.Literal["threshold"] = "threshold"
    limit: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SensorReadingChecksItem_Trend(UniversalBaseModel):
    kind: typing.Literal["trend"] = "trend"
    hours: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SensorReadingChecksItem = typing_extensions.Annotated[
    typing.Union[SensorReadingChecksItem_Threshold, SensorReadingChecksItem_Trend], pydantic.Field(discriminator="kind")
]
