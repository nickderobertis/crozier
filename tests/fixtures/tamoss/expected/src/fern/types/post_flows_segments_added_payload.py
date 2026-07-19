

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_flows_segments_added_payload_event import PostFlowsSegmentsAddedPayloadEvent
from .post_flows_segments_added_payload_event_type import PostFlowsSegmentsAddedPayloadEventType


class PostFlowsSegmentsAddedPayload(UniversalBaseModel):
    """
    Notification that new Segments have been added to a Flow.
    """

    event_timestamp: dt.datetime = pydantic.Field()
    """
    Timestamp at which the most recent Segment in the timerange was added (and the message generated)
    """

    event_type: PostFlowsSegmentsAddedPayloadEventType
    event: PostFlowsSegmentsAddedPayloadEvent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
