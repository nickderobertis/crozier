

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .actor_id import ActorId
from .change_seq import ChangeSeq
from .directory_binding import DirectoryBinding
from .inode_id import InodeId
from .inode_kind import InodeKind


class TrashEntry(UniversalBaseModel):
    """
    One recoverable deletion and the directory binding that it removed.
    """

    deleted_at_ms: int = pydantic.Field()
    """
    The time of the deletion, in Unix milliseconds.
    """

    deleted_binding: DirectoryBinding = pydantic.Field()
    """
    The directory binding that the deletion removed.
    """

    deleted_by: ActorId = pydantic.Field()
    """
    The actor responsible for the deletion.
    """

    deletion_seq: ChangeSeq = pydantic.Field()
    """
    The commit sequence that identifies this deletion.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The inode that the deletion hides.
    """

    inode_kind: InodeKind = pydantic.Field()
    """
    Whether the deleted root is a file or a directory. A newer server can return another kind.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
