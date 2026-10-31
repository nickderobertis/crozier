

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .commit import Commit
from .namespace_id import NamespaceId


class ListChangesResponse(UniversalBaseModel):
    """
    The commits after a change feed cursor.
    """

    after_seq: ChangeSeq = pydantic.Field()
    """
    The exclusive cursor that this page starts after. It's the cursor that the caller supplied,
    or the endpoint's initial position.
    """

    changes: typing.List[Commit] = pydantic.Field()
    """
    The logical commits after `after_seq`, in ascending namespace sequence order.
    """

    head_seq: ChangeSeq = pydantic.Field()
    """
    The namespace head sequence that this page was read at.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace whose change feed was read.
    """

    next_after_seq: typing.Optional[ChangeSeq] = pydantic.Field(default=None)
    """
    The cursor for the next page, when another page remains. It's absent on the page that
    reaches `head_seq`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
