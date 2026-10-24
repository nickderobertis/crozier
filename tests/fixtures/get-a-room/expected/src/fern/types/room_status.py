

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .room_status_status import RoomStatusStatus


class RoomStatus(UniversalBaseModel):
    room_id: str
    status: RoomStatusStatus
    created_at: dt.datetime
    expires_at: dt.datetime
    message_count: int
    message_bytes: int
    message_bytes_limit: int
    attachment_count: int
    attachment_bytes: int
    attachment_bytes_limit: int
    last_number: int
    has_final: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
