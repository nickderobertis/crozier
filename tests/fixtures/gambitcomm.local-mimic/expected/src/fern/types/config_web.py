

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigWeb(UniversalBaseModel):
    is_persistent_connections: typing.Optional[int] = None
    password: typing.Optional[str] = None
    port: typing.Optional[int] = None
    rule: typing.Optional[str] = None
    username: typing.Optional[str] = None
    wsdl: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
