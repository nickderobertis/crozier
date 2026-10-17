

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thread_storage_channel_values import ThreadStorageChannelValues
from .thread_storage_checkpoints import ThreadStorageCheckpoints
from .thread_storage_pending_writes import ThreadStoragePendingWrites


class ThreadStorage(UniversalBaseModel):
    """
    Bytes a thread occupies in the checkpointer, as stored.
    """

    thread_id: str
    total_bytes: int = pydantic.Field()
    """
    Sum of the three sections below.
    """

    checkpoints: ThreadStorageCheckpoints = pydantic.Field()
    """
    Checkpoint rows: serialized checkpoint plus metadata.
    """

    channel_values: ThreadStorageChannelValues = pydantic.Field()
    """
    Stored channel values, one row per channel version.
    """

    pending_writes: ThreadStoragePendingWrites = pydantic.Field()
    """
    Task writes not yet folded into a checkpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
