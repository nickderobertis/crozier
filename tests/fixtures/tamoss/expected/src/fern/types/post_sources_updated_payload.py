

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_sources_updated_payload_event import PostSourcesUpdatedPayloadEvent
from .post_sources_updated_payload_event_type import PostSourcesUpdatedPayloadEventType


class PostSourcesUpdatedPayload(UniversalBaseModel):
    """
    Information about a Source for which the metadata has been modified.
    """

    event_timestamp: dt.datetime = pydantic.Field()
    """
    Timestamp at which the Source was modified
    """

    event_type: PostSourcesUpdatedPayloadEventType
    event: PostSourcesUpdatedPayloadEvent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
