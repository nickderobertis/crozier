

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TrackerStudent(UniversalBaseModel):
    """
    Tracker Student.
    """

    student_id: str = pydantic.Field()
    """
    Student id.
    """

    student_name: str
    procare_student_status: str
    birth_date: typing.Optional[str] = None
    age: float
    start_date: typing.Optional[str] = None
    withdrawal_date: typing.Optional[str] = None
    transition_date: typing.Optional[str] = None
    room_age: float
    transition_date_is_past_date: bool
    is_first_period_in_room_due_to_transition: bool
    is_age_less_than_room_age_low: bool
    is_age_greater_than_room_age_high: bool
    has_been_enrolled_for_over_room_days_limit: bool
    is_transition_date_within_days_limit: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
