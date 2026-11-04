

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_sharee_lookup_all_of_extra import FilesSharingShareeLookupAllOfExtra
from .files_sharing_sharee_lookup_all_of_value import FilesSharingShareeLookupAllOfValue


class FilesSharingShareeLookupAllOf(UniversalBaseModel):
    extra: FilesSharingShareeLookupAllOfExtra
    value: FilesSharingShareeLookupAllOfValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
