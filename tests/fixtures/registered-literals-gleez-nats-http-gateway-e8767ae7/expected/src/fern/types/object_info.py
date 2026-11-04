

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .object_info_link import ObjectInfoLink


class ObjectInfo(UniversalBaseModel):
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, str]] = None
    link: typing.Optional[ObjectInfoLink] = None
    max_chunk_size: typing.Optional[int] = None
    bucket: typing.Optional[str] = None
    nuid: typing.Optional[str] = None
    size: typing.Optional[int] = None
    mtime: typing.Optional[dt.datetime] = None
    chunks: typing.Optional[int] = None
    digest: typing.Optional[str] = None
    deleted: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
