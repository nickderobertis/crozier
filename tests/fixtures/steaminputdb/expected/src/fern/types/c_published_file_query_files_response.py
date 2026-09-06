

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .published_file_details import PublishedFileDetails


class CPublishedFileQueryFilesResponse(UniversalBaseModel):
    next_cursor: typing.Optional[str] = None
    publishedfiledetails: typing.Optional[typing.List[PublishedFileDetails]] = None
    total: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
