

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .activity_attendee_status import ActivityAttendeeStatus


class ActivityAttendee(UniversalBaseModel):
    contact_id: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    email_address: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    id: typing.Optional[str] = None
    is_organizer: typing.Optional[bool] = None
    last_name: typing.Optional[str] = None
    middle_name: typing.Optional[str] = None
    name: typing.Optional[str] = None
    prefix: typing.Optional[str] = None
    status: typing.Optional[ActivityAttendeeStatus] = None
    suffix: typing.Optional[str] = None
    updated_at: typing.Optional[dt.datetime] = None
    user_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
