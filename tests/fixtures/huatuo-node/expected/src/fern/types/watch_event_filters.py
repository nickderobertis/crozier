

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WatchEventFilters(UniversalBaseModel):
    container_host_namespace: typing.Optional[str] = None
    container_hostname: typing.Optional[str] = None
    container_qos: typing.Optional[str] = None
    hostname: typing.Optional[str] = None
    region: typing.Optional[str] = None
    tracer_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
