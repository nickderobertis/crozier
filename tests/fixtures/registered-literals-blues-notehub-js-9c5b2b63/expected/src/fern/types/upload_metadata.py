

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .firmware import Firmware


class UploadMetadata(UniversalBaseModel):
    contains: typing.Optional[str] = None
    crc32: typing.Optional[int] = None
    created: typing.Optional[int] = None
    firmware: typing.Optional[Firmware] = None
    found: typing.Optional[str] = None
    length: typing.Optional[int] = None
    md5: typing.Optional[str] = None
    modified: typing.Optional[int] = None
    name: typing.Optional[str] = None
    notes: typing.Optional[str] = None
    source: typing.Optional[str] = None
    tags: typing.Optional[str] = None
    type: typing.Optional[str] = None
    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    User-specified version string provided at time of upload
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
