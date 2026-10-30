

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .namespace_id import NamespaceId
from .run_no import RunNo


class GrepIndexStatusActive(UniversalBaseModel):
    """
    An index that follows the change feed and can be searched through its watermark.
    """

    built_through_seq: ChangeSeq = pydantic.Field()
    """
    The sequence of the commit at the index cursor.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the status describes.
    """

    next_event_index: int = pydantic.Field()
    """
    The offset of the next change event within `built_through_seq`. It's zero when the whole
    commit is indexed.
    """

    next_run_no: RunNo = pydantic.Field()
    """
    The next run number that the index allocates.
    """

    reorganize_pending: bool = pydantic.Field()
    """
    Whether a partitioned segment reorganization is in progress.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
