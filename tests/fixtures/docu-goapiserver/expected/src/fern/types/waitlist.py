

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .waitlist_room_eligibility import WaitlistRoomEligibility


class Waitlist(UniversalBaseModel):
    """
    Waitlist.
    """

    student_id: str = pydantic.Field()
    """
    Student id.
    """

    first_name: str
    last_name: str
    student_name: str
    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    birth_date: typing.Optional[str] = None
    current_age_months: typing.Optional[float] = None
    preferred_start_date: typing.Optional[str] = None
    preferred_start_date_last_update: typing.Optional[str] = None
    preferred_start_date_age_at: typing.Optional[float] = None
    preferred_start_date_is_past_date: bool
    period_if_room_is_elegible: typing.Optional[typing.List[WaitlistRoomEligibility]] = None
    row_has_elegible_room: bool
    joined_waitlist: typing.Optional[str] = None
    siblings: str
    has_alerts: bool
    is_intellikid_student: bool
    school_color_hex: str
    school_short_name: str
    procare_desktop_enrollment_status: typing.Optional[str] = None
    procare_student_status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
