

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_flows_updated_payload_event import PostFlowsUpdatedPayloadEvent
from .post_flows_updated_payload_event_type import PostFlowsUpdatedPayloadEventType


class PostFlowsUpdatedPayload(UniversalBaseModel):
    """
    Information about a Flow for which the metadata has been modified.
    """

    event_timestamp: dt.datetime = pydantic.Field()
    """
    Timestamp at which the Flow was modified
    """

    event_type: PostFlowsUpdatedPayloadEventType
    event: PostFlowsUpdatedPayloadEvent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
