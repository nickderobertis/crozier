

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .file_revision import FileRevision
from .inode_id import InodeId
from .namespace_id import NamespaceId


class ListFileRevisionsResponse(UniversalBaseModel):
    """
    One page of a file's revisions.
    """

    head_seq: ChangeSeq = pydantic.Field()
    """
    The namespace head sequence that the read used.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The file inode whose revisions were returned.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that was read.
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    An opaque cursor for the next page, if more revisions are available.
    """

    revisions: typing.List[FileRevision] = pydantic.Field()
    """
    The retained revisions, in order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
