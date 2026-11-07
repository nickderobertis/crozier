

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .stream_progress_completed_ranges_item import StreamProgressCompletedRangesItem
from .stream_progress_status import StreamProgressStatus
from .stream_progress_total_range import StreamProgressTotalRange


class StreamProgress(UniversalBaseModel):
    """
    Per-stream progress snapshot.
    """

    status: StreamProgressStatus = pydantic.Field()
    """
    Current state, derived from stream_status events.
    """

    state_count: int = pydantic.Field()
    """
    Number of state checkpoints for this stream.
    """

    record_count: int = pydantic.Field()
    """
    Records synced for this stream in this run.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable status message (error reason, skip reason, etc).
    """

    total_range: typing.Optional[StreamProgressTotalRange] = pydantic.Field(default=None)
    """
    Full backfill time span for this stream.
    """

    completed_ranges: typing.Optional[typing.List[StreamProgressCompletedRangesItem]] = pydantic.Field(default=None)
    """
    Completed time sub-ranges within the total_range.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
