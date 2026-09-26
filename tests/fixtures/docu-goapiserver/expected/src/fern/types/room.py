

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Room(UniversalBaseModel):
    """
    Room.
    """

    id: str
    name: str
    capacity: typing.Optional[int] = None
    number: typing.Optional[int] = None
    transition_room_number: typing.Optional[int] = None
    transition_room_name: typing.Optional[str] = None
    transition_room_id: typing.Optional[str] = None
    auto_populate_transition_date: bool
    age_months_low: typing.Optional[float] = None
    age_months_high: typing.Optional[float] = None
    program_room: typing.Optional[str] = None
    program_room_id: typing.Optional[str] = None
    student_staff_ratio: typing.Optional[int] = None
    monthly_billing_plan_id: typing.Optional[str] = None
    monthly_billing_plan_name: typing.Optional[str] = None
    monthly_current_tuition: typing.Optional[float] = None
    weekly_billing_plan_id: typing.Optional[str] = None
    weekly_billing_plan_name: typing.Optional[str] = None
    weekly_current_tuition: typing.Optional[float] = None
    bi_weekly_billing_plan_id: typing.Optional[str] = None
    bi_weekly_billing_plan_name: typing.Optional[str] = None
    bi_weekly_current_tuition: typing.Optional[float] = None
    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    is_active: bool
    is_valid: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
