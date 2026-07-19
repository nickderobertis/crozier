

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_sources_deleted_payload_event import PostSourcesDeletedPayloadEvent
from .post_sources_deleted_payload_event_type import PostSourcesDeletedPayloadEventType


class PostSourcesDeletedPayload(UniversalBaseModel):
    """
    Notification that a Source has been deleted.
    """

    event_timestamp: dt.datetime = pydantic.Field()
    """
    Timestamp at which the Source was modified
    """

    event_type: PostSourcesDeletedPayloadEventType
    event: PostSourcesDeletedPayloadEvent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
