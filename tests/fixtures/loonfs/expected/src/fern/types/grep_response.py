

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .grep_match import GrepMatch
from .namespace_id import NamespaceId


class GrepResponse(UniversalBaseModel):
    """
    One page of content search results.
    """

    built_through_seq: ChangeSeq = pydantic.Field()
    """
    The last sequence that the index covers. The server searched the commits at or below this
    sequence through the index.
    """

    head_seq: ChangeSeq = pydantic.Field()
    """
    The namespace head sequence that the server used to evaluate this page.
    """

    matches: typing.List[GrepMatch] = pydantic.Field()
    """
    The matches, in ascending `(inode_id, byte_offset)` order.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that was searched.
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The cursor for the next page. It's present when another page follows.
    """

    tail_scanned: bool = pydantic.Field()
    """
    Whether the server scanned every revision after `built_through_seq`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
