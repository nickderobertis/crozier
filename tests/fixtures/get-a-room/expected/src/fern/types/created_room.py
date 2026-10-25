

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreatedRoom(UniversalBaseModel):
    room_id: str
    expires_at: dt.datetime
    creator_capability: str
    lead_invitation_url: str
    lead_invitation_message: str
    guest_invitation_url: str
    guest_invitation_message: str
    observer_url: str
    observer_message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
