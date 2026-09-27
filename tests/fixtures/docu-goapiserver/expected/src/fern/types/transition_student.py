

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert import Alert


class TransitionStudent(UniversalBaseModel):
    """
    Transition Student.
    """

    student_id: str = pydantic.Field()
    """
    Student id.
    """

    student_name: str
    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    procare_student_status: str
    ems_student_status: str
    room_id: str = pydantic.Field()
    """
    Room id.
    """

    room_name: str
    room_program: str
    room_changed_at: str
    dob: str
    admission_date: str
    enrollment_id: str = pydantic.Field()
    """
    Enrollment id.
    """

    transition_date: str
    transition_date2: typing_extensions.Annotated[
        str, FieldMetadata(alias="transition_date_2"), pydantic.Field(alias="transition_date_2")
    ]
    withdrawal_date: str
    transition_room_id: str = pydantic.Field()
    """
    Transition room id.
    """

    transition_room_name: str
    transition_room_program: str
    days_to_transition_date: int
    billing_plan: str
    transition_alert: str
    transition_alert1clear_user_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="transition_alert_1_clear_user_id"),
        pydantic.Field(alias="transition_alert_1_clear_user_id", description="Transition alert 1 clear user id."),
    ]
    """
    Transition alert 1 clear user id.
    """

    transition_alert2clear_user_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="transition_alert_2_clear_user_id"),
        pydantic.Field(alias="transition_alert_2_clear_user_id", description="Transition alert 2 clear user id."),
    ]
    """
    Transition alert 2 clear user id.
    """

    change_room_in_procare: str
    inconsistent_dates: bool
    transition_date_is_past_date: bool
    review_transition_date: bool
    ems_status_missing_info: bool
    transition_date_auto_assigned: bool
    transition_room_earlier: bool
    missing_transition_room: bool
    missing_active_plan: bool
    start_date_close_no_plan: bool
    current_room_is_transition_room: bool
    alerts: typing.Optional[typing.List[Alert]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
