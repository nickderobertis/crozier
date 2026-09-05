

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1Alpha1SystemStatusSystemInfo(UniversalBaseModel):
    time: str
    cpu_pct: float
    memory: int
    disk_pct: float
    network_io_sent: int
    network_io_recv: int
    threads: int
    fds: int
    pid: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
