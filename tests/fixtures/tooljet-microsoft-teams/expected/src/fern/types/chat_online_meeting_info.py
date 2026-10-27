

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chat_online_meeting_info_organizer import ChatOnlineMeetingInfoOrganizer


class ChatOnlineMeetingInfo(UniversalBaseModel):
    calendar_event_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="calendarEventId"), pydantic.Field(alias="calendarEventId")
    ] = None
    join_web_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="joinWebUrl"), pydantic.Field(alias="joinWebUrl")
    ] = None
    organizer: typing.Optional[ChatOnlineMeetingInfoOrganizer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
