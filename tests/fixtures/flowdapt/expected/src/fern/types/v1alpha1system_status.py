

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1alpha1system_status_os_info import V1Alpha1SystemStatusOsInfo
from .v1alpha1system_status_system_info import V1Alpha1SystemStatusSystemInfo


class V1Alpha1SystemStatus(UniversalBaseModel):
    version: str
    name: str
    system: V1Alpha1SystemStatusSystemInfo
    os: V1Alpha1SystemStatusOsInfo
    python: str
    hostname: str
    services: typing.Dict[str, typing.Any]
    database: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
