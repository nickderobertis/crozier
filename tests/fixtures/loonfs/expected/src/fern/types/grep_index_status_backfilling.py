

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .inode_id import InodeId
from .namespace_id import NamespaceId
from .pin_id import PinId
from .run_no import RunNo


class GrepIndexStatusBackfilling(UniversalBaseModel):
    """
    An index that is running its initial scan of a pinned checkpoint and can't be searched yet.
    """

    captured_seq: ChangeSeq = pydantic.Field()
    """
    The namespace sequence that completes the backfill when the index reaches it.
    """

    checkpoint_id: PinId = pydantic.Field()
    """
    The checkpoint that pins the state being scanned.
    """

    cursor_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The inode that the scan resumes after. It's absent before the first page.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the status describes.
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
