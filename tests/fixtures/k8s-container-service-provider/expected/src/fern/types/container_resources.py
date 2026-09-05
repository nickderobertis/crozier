

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .container_cpu import ContainerCpu
from .container_memory import ContainerMemory


class ContainerResources(UniversalBaseModel):
    """
    CPU and memory resource constraints
    """

    cpu: ContainerCpu
    memory: ContainerMemory

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
