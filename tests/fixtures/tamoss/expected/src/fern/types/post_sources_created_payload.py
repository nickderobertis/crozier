

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_sources_created_payload_event import PostSourcesCreatedPayloadEvent
from .post_sources_created_payload_event_type import PostSourcesCreatedPayloadEventType


class PostSourcesCreatedPayload(UniversalBaseModel):
    """
    Information about a Source which has been newly created in this service instance
    """

    event_timestamp: dt.datetime = pydantic.Field()
    """
    Timestamp at which the new Source was created
    """

    event_type: PostSourcesCreatedPayloadEventType
    event: PostSourcesCreatedPayloadEvent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
