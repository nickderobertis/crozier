

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .room_attachment import RoomAttachment
from .room_message_role import RoomMessageRole


class RoomMessage(UniversalBaseModel):
    number: int
    role: RoomMessageRole
    text: str
    created_at: dt.datetime
    attachments: typing.List[RoomAttachment]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
