

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .published_file_details import PublishedFileDetails


class CPublishedFileGetDetailsResponse(UniversalBaseModel):
    publishedfiledetails: typing.Optional[typing.List[PublishedFileDetails]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
