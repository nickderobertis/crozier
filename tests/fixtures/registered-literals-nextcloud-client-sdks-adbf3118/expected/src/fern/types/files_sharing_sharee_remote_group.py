

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .files_sharing_sharee import FilesSharingSharee
from .files_sharing_sharee_remote_group_all_of import FilesSharingShareeRemoteGroupAllOf


class FilesSharingShareeRemoteGroup(FilesSharingSharee, FilesSharingShareeRemoteGroupAllOf):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
