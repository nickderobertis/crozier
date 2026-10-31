

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .inode_id import InodeId
from .namespace_id import NamespaceId
from .path_entry import PathEntry


class ListInodeChildrenResponse(UniversalBaseModel):
    """
    One page of a directory's children, addressed by the parent inode, with the namespace head that
    the read used.
    """

    entries: typing.List[PathEntry] = pydantic.Field()
    """
    The directory entries, in canonical name key order.
    """

    head_seq: ChangeSeq = pydantic.Field()
    """
    The namespace head sequence that this listing was read at.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that was read.
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The cursor for the next page, if more entries remain.
    """

    parent_inode_id: InodeId = pydantic.Field()
    """
    The directory inode whose children were returned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
