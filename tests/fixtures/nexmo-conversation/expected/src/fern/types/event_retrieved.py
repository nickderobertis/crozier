

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .event_body import EventBody
from .event_id import EventId
from .event_type import EventType
from .href_event import HrefEvent
from .member_id import MemberId
from .member_state import MemberState
from .timestamp_created import TimestampCreated


class EventRetrieved(UniversalBaseModel):
    """
    Retrieve Events Response Payload Object Item
    """

    body: EventBody
    from_: typing_extensions.Annotated[
        typing.Optional[MemberId], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    href: HrefEvent
    id: EventId
    state: typing.Optional[MemberState] = None
    timestamp: TimestampCreated
    to: typing.Optional[MemberId] = None
    type: EventType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
