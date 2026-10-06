

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_api_usage_response_cpu import GetApiUsageResponseCpu
from .get_api_usage_response_gpu_item import GetApiUsageResponseGpuItem
from .get_api_usage_response_kernel import GetApiUsageResponseKernel
from .get_api_usage_response_memory import GetApiUsageResponseMemory
from .get_api_usage_response_server import GetApiUsageResponseServer


class GetApiUsageResponse(UniversalBaseModel):
    cpu: GetApiUsageResponseCpu
    gpu: typing.Optional[typing.List[GetApiUsageResponseGpuItem]] = None
    kernel: typing.Optional[GetApiUsageResponseKernel] = None
    memory: GetApiUsageResponseMemory
    server: typing.Optional[GetApiUsageResponseServer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
