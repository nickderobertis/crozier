

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_flows_segments_deleted_payload_event import PostFlowsSegmentsDeletedPayloadEvent
from .post_flows_segments_deleted_payload_event_type import PostFlowsSegmentsDeletedPayloadEventType


class PostFlowsSegmentsDeletedPayload(UniversalBaseModel):
    """
    Notification that Segments have been deleted from a Flow.
    """

    event_timestamp: dt.datetime = pydantic.Field()
    """
    Timestamp at which the most recent Segment in the timerange was added (and the message generated)
    """

    event_type: PostFlowsSegmentsDeletedPayloadEventType
    event: PostFlowsSegmentsDeletedPayloadEvent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
