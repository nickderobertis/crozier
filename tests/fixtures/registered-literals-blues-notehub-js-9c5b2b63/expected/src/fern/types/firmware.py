

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Firmware(UniversalBaseModel):
    builder: typing.Optional[str] = None
    built: typing.Optional[str] = None
    firmware: typing.Optional[str] = None
    org: typing.Optional[str] = None
    product: typing.Optional[str] = None
    target: typing.Optional[str] = None
    ver_build: typing.Optional[int] = None
    ver_major: typing.Optional[int] = None
    ver_minor: typing.Optional[int] = None
    ver_patch: typing.Optional[int] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
