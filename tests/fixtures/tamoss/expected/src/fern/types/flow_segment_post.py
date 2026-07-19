

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flow_segment_post_get_urls_item import FlowSegmentPostGetUrlsItem
from .timerange import Timerange
from .timestamp import Timestamp


class FlowSegmentPost(UniversalBaseModel):
    """
    Provides the location and metadata of the media files corresponding to timerange Segments of a Flow.
    """

    object_id: str = pydantic.Field()
    """
    The Object identifier for the Media Object.
    """

    ts_offset: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The timestamp offset between the sample timestamps stored in, or inferred from, the media file and the corresponding timestamp in the Segment, ie. ts_offset = segment ts - media object ts. Assumed to be 0:0 if not set. Format as described by the [Timestamp](#/schemas/timestamp) type
    """

    timerange: Timerange = pydantic.Field()
    """
    The timerange for the samples contained in the Segment. The timerange start is always inclusive. If samples have a duration then the timerange end is exclusive and covers at least the duration of the last sample. The exclusive timerange end will typically be set to the timestamp of the next sample. If the samples don't have a duration then the timerange end is inclusive. Format is described by the [TimeRange](#/schemas/timerange) type. Note that where temporal re-ordering is used, the timerange and samples refers to the presentation timeline.
    """

    object_timerange: typing.Optional[Timerange] = pydantic.Field(default=None)
    """
    The timerange covering the sample timestamps embedded in or derived from the Media Object itself, on the Media Object's timeline. If not given at first registration of an Object, defaults to `timerange - ts_offset` on the assumption that the Flow Segment uses the entire Media Object. Clients should not set this when Media Objects are re-used. Service implementations should reject requests where `object_timerange` is set to a value that conflicts with the existing Media Object metadata.
    """

    last_duration: typing.Optional[Timestamp] = pydantic.Field(default=None)
    """
    The difference between the exclusive end of the `timerange` and the last sample timestamp. Format as described by the [Timestamp](#/schemas/timestamp) type, but cannot be negative
    """

    sample_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The start of the Segment represented as a count of samples from the start of the Object. Note that a sample is a video frame or audio sample. A (coded) audio frame has multiple audio samples. Assumed to be 0 if not set. Must be set if the Flow Segment doesn't start at the beginning of the Media Object. DEPRECATED: Use object_timerange instead - see AppNote 0036. Service implementations SHOULD continue to store and return it if set.
    """

    sample_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The count of samples in the Segment (which may be fewer than in the Object). The count could be less than expected given the Segment duration and rate if there are gaps. If not set, every sample from sample_offset onwards is used. Must be set if the Flow Segment doesn't use the entire Media Object. Note that a sample is a video frame or audio sample. A (coded) audio frame has multiple audio samples. DEPRECATED: Use object_timerange instead - see AppNote 0036. Service implementations SHOULD continue to store and return it if set.
    """

    get_urls: typing.Optional[typing.List[FlowSegmentPostGetUrlsItem]] = pydantic.Field(default=None)
    """
    A list of URLs to which a GET request can be made to directly retrieve the contents of the Media Object. This is required by the `http_object_store` Storage Backend type, which is the only one currently described. Clients may choose any URL in the list and treat them as identical, however service instances may sort the list such that the preferred URL is first. `get_urls` should only be used to add uncontrolled URLs. URLs for the provided object_id controlled by the service instance will be populated automatically by the service instance.
    """

    key_frame_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of key frames in the Media Object. This should be set greater than zero when the Media Object contains key frames that serve as a stream access point
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
