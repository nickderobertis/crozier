

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .delete_directory_behavior import DeleteDirectoryBehavior
from .inode_id import InodeId


class FilesystemOperationDeletePath(UniversalBaseModel):
    """
    An operation that deletes the file or directory at one path.
    """

    behavior: typing.Optional[DeleteDirectoryBehavior] = pydantic.Field(default=None)
    """
    Whether the operation can recursively delete a non-empty directory.
    """

    expected_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The inode that the path must still resolve to before the delete.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path, which must resolve to a visible inode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
