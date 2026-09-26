

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_metadata_get200response_trapped import DocMetadataGet200ResponseTrapped


class DocMetadataGet200Response(UniversalBaseModel):
    title: typing.Optional[str] = None
    author: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    keywords: typing.Optional[str] = None
    producer: typing.Optional[str] = None
    creator: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    trapped: DocMetadataGet200ResponseTrapped
    custom: typing.Dict[str, str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
