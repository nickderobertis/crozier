

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .directory_listing_files_item_type import DirectoryListingFilesItemType


class DirectoryListingFilesItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    size: typing.Optional[int] = None
    type: typing.Optional[DirectoryListingFilesItemType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
