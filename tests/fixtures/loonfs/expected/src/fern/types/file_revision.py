

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .actor_id import ActorId
from .change_seq import ChangeSeq
from .commit_id import CommitId
from .content_ref import ContentRef
from .inode_id import InodeId
from .revision_no import RevisionNo


class FileRevision(UniversalBaseModel):
    """
    One immutable revision of a file.
    """

    commit_id: CommitId = pydantic.Field()
    """
    The ID of the commit that created this revision.
    """

    committed_at_ms: int = pydantic.Field()
    """
    The time the revision was committed, in Unix milliseconds. Commit order comes from
    `committed_seq`, not from this time.
    """

    committed_by: ActorId = pydantic.Field()
    """
    The actor responsible for this revision, as the application supplied it.
    """

    committed_seq: ChangeSeq = pydantic.Field()
    """
    The namespace sequence of the commit that created this revision.
    """

    content_ref: ContentRef = pydantic.Field()
    """
    The content stored for this revision.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The file inode that this revision belongs to.
    """

    revision_no: RevisionNo = pydantic.Field()
    """
    The revision number within the file inode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
