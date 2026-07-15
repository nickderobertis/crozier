

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigTftp(UniversalBaseModel):
    cache: typing.Optional[int] = None
    client: typing.Optional[str] = None
    dstfile: typing.Optional[str] = None
    mode: typing.Optional[str] = None
    port: typing.Optional[int] = None
    retries: typing.Optional[int] = None
    script: typing.Optional[str] = None
    server: typing.Optional[str] = None
    srcfile: typing.Optional[str] = None
    timeout: typing.Optional[int] = None
    trace: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
