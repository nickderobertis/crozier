

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert_operator import AlertOperator
from .bench_alert_levels_target import BenchAlertLevelsTarget


class BenchAlertLevels(UniversalBaseModel):
    operator: AlertOperator
    levels: typing.List[str]
    target: BenchAlertLevelsTarget

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
