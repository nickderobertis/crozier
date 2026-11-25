

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LockSensor_LevelUpstream(UniversalBaseModel):
    """
    A mapping naming one member twice, whose tag is unrequired.
    """

    sensor_id: typing.Literal["level_upstream"] = "level_upstream"
    depth: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LockSensor_LevelDownstream(UniversalBaseModel):
    """
    A mapping naming one member twice, whose tag is unrequired.
    """

    sensor_id: typing.Literal["level_downstream"] = "level_downstream"
    depth: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LockSensor_Flow(UniversalBaseModel):
    """
    A mapping naming one member twice, whose tag is unrequired.
    """

    sensor_id: typing.Literal["flow"] = "flow"
    rate: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LockSensor = typing_extensions.Annotated[
    typing.Union[LockSensor_LevelUpstream, LockSensor_LevelDownstream, LockSensor_Flow],
    pydantic.Field(discriminator="sensor_id"),
]
