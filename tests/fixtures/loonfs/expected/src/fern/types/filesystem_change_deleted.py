

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .directory_binding import DirectoryBinding
from .inode_id import InodeId


class FilesystemChangeDeleted(UniversalBaseModel):
    """
    A file or directory subtree was deleted.
    """

    deleted_binding: DirectoryBinding = pydantic.Field()
    """
    The directory binding that the deletion removed.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The inode at the root of the deleted subtree.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
