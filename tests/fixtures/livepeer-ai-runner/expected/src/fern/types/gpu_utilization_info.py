

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GpuUtilizationInfo(UniversalBaseModel):
    """
    Model for GPU utilization statistics.
    """

    id: str
    name: str
    memory_total: int
    memory_free: int
    utilization_compute: int
    utilization_memory: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
