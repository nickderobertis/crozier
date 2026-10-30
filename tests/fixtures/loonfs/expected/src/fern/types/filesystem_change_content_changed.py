

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_ref import ContentRef
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemChangeContentChanged(UniversalBaseModel):
    """
    A file received a new current revision from a put, a copy, an append, or a revision
    restore.
    """

    append_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The offset where the appended bytes begin, present when an append published the
    revision.
    
    It equals the base revision's `size_bytes`, so the new revision's bytes are the base
    revision's bytes followed by the bytes from this offset to `size_bytes`. It's
    present for every append, including one that starts a new content ID, and absent for
    a put, a copy, or a revision restore.
    """

    content_ref: ContentRef = pydantic.Field()
    """
    The immutable content that the revision published.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The file inode whose history advanced.
    """

    revision_no: RevisionNo = pydantic.Field()
    """
    The file's new revision number, which is higher than the number of every earlier
    revision.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
