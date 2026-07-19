

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_flows_created_payload_event import PostFlowsCreatedPayloadEvent
from .post_flows_created_payload_event_type import PostFlowsCreatedPayloadEventType


class PostFlowsCreatedPayload(UniversalBaseModel):
    """
    Information about a Flow which has been newly created in this service instance
    """

    event_timestamp: dt.datetime = pydantic.Field()
    """
    Timestamp at which the new Flow was created
    """

    event_type: PostFlowsCreatedPayloadEventType
    event: PostFlowsCreatedPayloadEvent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
