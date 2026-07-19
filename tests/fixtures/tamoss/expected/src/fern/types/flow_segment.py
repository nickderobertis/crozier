

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .object_core import ObjectCore
from .timerange import Timerange
from .timestamp import Timestamp


class FlowSegment(ObjectCore):
    """
    Provides the location and metadata of the media files corresponding to timerange segments of a Flow.
    """

    object_id: str = pydantic.Field()
    """
    The object store identifier for the Media Object.
    """

    ts_offset: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The timestamp offset between the sample timestamps stored in the media file and the corresponding timestamp in the Segment, ie. ts_offset = segment ts - media object ts. Assumed to be 0:0 if not set. Format as described by the [Timestamp](#/schemas/timestamp) type
    """

    timerange: Timerange = pydantic.Field()
    """
    The timerange for the samples contained in the Segment. The timerange start is always inclusive. If samples have a duration then the timerange end is exclusive and covers at least the duration of the last sample. The exclusive timerange end will typically be set to the timestamp of the next sample. If the samples don't have a duration then the timerange end is inclusive. Format is described by the [TimeRange](#/schemas/timerange) type. Note that where temporal re-ordering is used, the timerange and samples refers to the presentation timeline.
    """

    last_duration: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The difference between the exclusive end of the `timerange` and the last sample timestamp. Format as described by the [Timestamp](#/schemas/timestamp) type, but cannot be negative
    """

    object_timerange: typing.Optional[Timerange] = pydantic.Field(default=None)
    """
    The timerange covering the sample timestamps embedded in or derived from the Media Object itself, on the Media Object's timeline.
    """

    sample_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The start of the Segment represented as a count of samples from the start of the Media Object. Note that a sample is a video frame or audio sample. A (coded) audio frame has multiple audio samples. Assumed to be 0 if not set. DEPRECATED: Use object_timerange instead - see AppNote 0036. Service implementations SHOULD continue to store and return it if set.
    """

    sample_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The count of samples in the Segment (which may be fewer than in the Media Object). The count could be less than expected given the Segment duration and rate if there are gaps. If not set, every sample from sample_offset onwards is used. Note that a sample is a video frame or audio sample. A (coded) audio frame has multiple audio samples. DEPRECATED: Use object_timerange instead - see AppNote 0036. Service implementations SHOULD continue to store and return it if set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
