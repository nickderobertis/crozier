

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .activity_attendee import ActivityAttendee
from .activity_show_as import ActivityShowAs
from .activity_type import ActivityType
from .address import Address
from .custom_field import CustomField


class Activity(UniversalBaseModel):
    account_id: typing.Optional[str] = None
    activity_date: typing.Optional[str] = None
    activity_datetime: typing.Optional[str] = None
    all_day_event: typing.Optional[bool] = None
    archived: typing.Optional[bool] = None
    asset_id: typing.Optional[str] = None
    attendees: typing.Optional[typing.List[ActivityAttendee]] = None
    campaign_id: typing.Optional[str] = None
    case_id: typing.Optional[str] = None
    child: typing.Optional[bool] = None
    company_id: typing.Optional[str] = None
    contact_id: typing.Optional[str] = None
    contract_id: typing.Optional[str] = None
    created_at: typing.Optional[str] = None
    created_by: typing.Optional[str] = None
    custom_fields: typing.Optional[typing.List[CustomField]] = None
    custom_object_id: typing.Optional[str] = None
    deleted: typing.Optional[bool] = None
    description: typing.Optional[str] = None
    done: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the Activity is done or not
    """

    downstream_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The third-party API ID of original entity
    """

    duration_minutes: typing.Optional[int] = None
    duration_seconds: typing.Optional[int] = None
    end_date: typing.Optional[str] = None
    end_datetime: typing.Optional[str] = None
    event_sub_type: typing.Optional[str] = None
    group_event: typing.Optional[bool] = None
    group_event_type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    lead_id: typing.Optional[str] = None
    location: typing.Optional[str] = None
    location_address: typing.Optional[Address] = None
    note: typing.Optional[str] = None
    opportunity_id: typing.Optional[str] = None
    owner_id: typing.Optional[str] = None
    private: typing.Optional[bool] = None
    product_id: typing.Optional[str] = None
    recurrent: typing.Optional[bool] = None
    reminder_datetime: typing.Optional[str] = None
    reminder_set: typing.Optional[bool] = None
    show_as: typing.Optional[ActivityShowAs] = None
    solution_id: typing.Optional[str] = None
    start_datetime: typing.Optional[str] = None
    title: typing.Optional[str] = None
    type: ActivityType
    updated_at: typing.Optional[str] = None
    updated_by: typing.Optional[str] = None
    user_id: typing.Optional[str] = None
    video_conference_id: typing.Optional[str] = None
    video_conference_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
