

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gpu_utilization_info import GpuUtilizationInfo


class HardwareStats(UniversalBaseModel):
    """
    Response model for real-time GPU statistics.
    """

    pipeline: str
    model_id: str
    gpu_stats: typing.Dict[str, GpuUtilizationInfo]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
