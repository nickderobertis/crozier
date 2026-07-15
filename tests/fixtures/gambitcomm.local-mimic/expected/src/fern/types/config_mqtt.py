

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigMqtt(UniversalBaseModel):
    broker: typing.Optional[str] = None
    clientid: typing.Optional[str] = None
    filename: typing.Optional[str] = None
    is_tls: typing.Optional[str] = None
    password: typing.Optional[str] = None
    port: typing.Optional[int] = None
    tls_conf_filename: typing.Optional[str] = None
    username: typing.Optional[str] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
