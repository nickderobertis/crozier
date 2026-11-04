

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_sharee_remote_all_of_value import FilesSharingShareeRemoteAllOfValue


class FilesSharingShareeRemoteGroupAllOf(UniversalBaseModel):
    guid: str
    name: str
    value: FilesSharingShareeRemoteAllOfValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
