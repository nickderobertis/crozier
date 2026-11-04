

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .directory_listing_files_item import DirectoryListingFilesItem


class DirectoryListing(UniversalBaseModel):
    path: typing.Optional[str] = None
    files: typing.Optional[typing.List[DirectoryListingFilesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
