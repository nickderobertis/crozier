

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .namespace_id import NamespaceId
from .trash_entry import TrashEntry


class ListTrashResponse(UniversalBaseModel):
    """
    One page of the namespace's recoverable deletions.
    """

    entries: typing.List[TrashEntry] = pydantic.Field()
    """
    The recoverable deletions, oldest first.
    """

    head_seq: ChangeSeq = pydantic.Field()
    """
    The head sequence that this page was evaluated at.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that was read.
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The cursor for the next page. It's present when another page follows.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
