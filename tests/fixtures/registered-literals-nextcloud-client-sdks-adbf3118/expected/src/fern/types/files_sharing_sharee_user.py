

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .files_sharing_sharee import FilesSharingSharee
from .files_sharing_sharee_user_all_of import FilesSharingShareeUserAllOf


class FilesSharingShareeUser(FilesSharingSharee, FilesSharingShareeUserAllOf):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
