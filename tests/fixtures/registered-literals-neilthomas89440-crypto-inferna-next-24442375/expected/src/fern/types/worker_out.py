

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gpu_out import GpuOut
from .instance_out import InstanceOut


class WorkerOut(UniversalBaseModel):
    id: str
    cluster_id: str
    name: str
    hostname: str
    state: str
    version: typing.Optional[str] = None
    os: typing.Optional[str] = None
    cpu_cores: typing.Optional[int] = None
    memory_mb: typing.Optional[int] = None
    last_seen_at: typing.Optional[dt.datetime] = None
    gpus: typing.Optional[typing.List[GpuOut]] = None
    instances: typing.Optional[typing.List[InstanceOut]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
