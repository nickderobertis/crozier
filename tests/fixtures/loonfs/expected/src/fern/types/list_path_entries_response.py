

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .change_seq import ChangeSeq
from .namespace_id import NamespaceId
from .path_entry import PathEntry


class ListPathEntriesResponse(UniversalBaseModel):
    """
    One page of a directory's entries, with the namespace head that the read used.
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

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path of the listed directory.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
