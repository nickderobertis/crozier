

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_step_cpu_requested_frequency import Dbv0037JobStepCpuRequestedFrequency


class Dbv0037JobStepCpu(UniversalBaseModel):
    """
    CPU properties
    """

    requested_frequency: typing.Optional[Dbv0037JobStepCpuRequestedFrequency] = None
    governor: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    CPU governor
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
