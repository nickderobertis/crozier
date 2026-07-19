

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_flows_deleted_payload_event import PostFlowsDeletedPayloadEvent
from .post_flows_deleted_payload_event_type import PostFlowsDeletedPayloadEventType


class PostFlowsDeletedPayload(UniversalBaseModel):
    """
    Notification that a Flow has been deleted (or scheduled for deletion).
    """

    event_timestamp: dt.datetime = pydantic.Field()
    """
    Timestamp at which the Flow was modified
    """

    event_type: PostFlowsDeletedPayloadEventType
    event: PostFlowsDeletedPayloadEvent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
