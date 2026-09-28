

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .activity_totals import ActivityTotals


class ActivitySummaryKid(UniversalBaseModel):
    """
    Activity Summary Kid.
    """

    activity_totals: ActivityTotals
    allergy: str
    color: str
    current_section_id: str = pydantic.Field()
    """
    Current section id.
    """

    first_name: str
    hide_messages: typing.Optional[typing.List[typing.Any]] = None
    id: str
    initials: str
    last_name: str
    name: str
    profile_pic_url: str
    registration_status: str
    signed_in_room: typing.Any
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
