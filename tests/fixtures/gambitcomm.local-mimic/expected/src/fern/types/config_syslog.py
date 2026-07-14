

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigSyslog(UniversalBaseModel):
    client: typing.Optional[str] = None
    hostname: typing.Optional[str] = None
    localport: typing.Optional[int] = None
    separator: typing.Optional[str] = None
    sequence: typing.Optional[int] = None
    server: typing.Optional[str] = None
    serverport: typing.Optional[int] = None
    timestamp: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
