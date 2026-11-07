

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .instance_out import InstanceOut


class DashboardOut(UniversalBaseModel):
    clusters: int
    workers_online: int
    gpus_total: int
    vram_used_mb: int
    vram_total_mb: int
    instances_running: int
    instances: typing.List[InstanceOut]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
