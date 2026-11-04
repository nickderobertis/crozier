

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .files_sharing_sharee import FilesSharingSharee
from .files_sharing_sharee_remote_all_of import FilesSharingShareeRemoteAllOf


class FilesSharingShareeRemote(FilesSharingSharee, FilesSharingShareeRemoteAllOf):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
