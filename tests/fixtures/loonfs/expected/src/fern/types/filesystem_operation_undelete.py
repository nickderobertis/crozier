

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .change_seq import ChangeSeq
from .display_name import DisplayName
from .inode_id import InodeId


class FilesystemOperationUndelete(UniversalBaseModel):
    """
    An operation that restores the deletion that `inode_id` and `deletion_seq` identify.

    To choose the destination, set `destination_path`, or set `destination_parent_inode_id` and
    `destination_display_name`. If you set neither, the undelete uses the parent and name
    recorded with the deletion.
    """

    deletion_seq: ChangeSeq = pydantic.Field()
    """
    The deletion sequence that the caller observed. It prevents the undelete from cancelling
    a newer deletion of the inode.
    """

    destination_display_name: typing.Optional[DisplayName] = pydantic.Field(default=None)
    """
    The inode's name in `destination_parent_inode_id`.
    """

    destination_parent_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The directory to restore the inode into. It requires `destination_display_name`.
    """

    destination_path: typing.Optional[AbsolutePath] = pydantic.Field(default=None)
    """
    The absolute path to restore the inode to. It can't be combined with
    `destination_parent_inode_id`.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The deleted inode to make reachable again.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
