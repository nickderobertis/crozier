

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEthernetSettingsResponse(UniversalBaseModel):
    enable: typing.Optional[bool] = None
    static_ip: typing.Optional[bool] = None
    ip: typing.Optional[str] = None
    netmask: typing.Optional[str] = None
    gateway: typing.Optional[str] = None
    dns: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
