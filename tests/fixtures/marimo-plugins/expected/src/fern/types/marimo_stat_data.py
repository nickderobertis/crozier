

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_stat_data_direction import MarimoStatDataDirection
from .marimo_stat_data_target_direction import MarimoStatDataTargetDirection
from .marimo_stat_data_value import MarimoStatDataValue


class MarimoStatData(UniversalBaseModel):
    value: typing.Optional[MarimoStatDataValue] = None
    label: typing.Optional[str] = None
    caption: typing.Optional[str] = None
    bordered: typing.Optional[bool] = None
    direction: typing.Optional[MarimoStatDataDirection] = None
    target_direction: typing.Optional[MarimoStatDataTargetDirection] = None
    slot: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
