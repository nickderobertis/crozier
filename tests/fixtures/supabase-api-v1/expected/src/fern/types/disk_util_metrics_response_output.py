

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .disk_util_metrics_response_output_metrics import DiskUtilMetricsResponseOutputMetrics


class DiskUtilMetricsResponseOutput(UniversalBaseModel):
    timestamp: str
    metrics: DiskUtilMetricsResponseOutputMetrics

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
