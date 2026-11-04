

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert_operator import AlertOperator


class SensorReadingAlertsItem_Bench(UniversalBaseModel):
    target: typing.Literal["bench"] = "bench"
    operator: AlertOperator
    levels: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SensorReadingAlertsItem_Vent(UniversalBaseModel):
    target: typing.Literal["vent"] = "vent"
    operator: AlertOperator
    levels: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SensorReadingAlertsItem = typing_extensions.Annotated[
    typing.Union[SensorReadingAlertsItem_Bench, SensorReadingAlertsItem_Vent], pydantic.Field(discriminator="target")
]
