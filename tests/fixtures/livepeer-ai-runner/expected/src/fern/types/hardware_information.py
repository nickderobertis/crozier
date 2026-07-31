

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gpu_compute_info import GpuComputeInfo


class HardwareInformation(UniversalBaseModel):
    """
    Response model for GPU information.
    """

    pipeline: str
    model_id: str
    gpu_info: typing.Dict[str, GpuComputeInfo]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
