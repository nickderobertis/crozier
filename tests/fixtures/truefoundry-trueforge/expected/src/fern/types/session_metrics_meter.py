

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metrics_unit import MetricsUnit
from .session_metrics_meter_name import SessionMetricsMeterName


class SessionMetricsMeter(UniversalBaseModel):
    aggregate_value: float
    description: str
    name: SessionMetricsMeterName
    unit: MetricsUnit

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
