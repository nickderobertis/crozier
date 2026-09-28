

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .alert import Alert


class StudentProjection(UniversalBaseModel):
    """
    Student Projection.
    """

    id: typing.Optional[str] = None
    monday_item_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Monday item id.
    """

    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    school_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    School id.
    """

    school_name: typing.Optional[str] = None
    birth_date: typing.Optional[str] = None
    admission_date: typing.Optional[str] = None
    procare_student_status: typing.Optional[str] = None
    ems_student_status: typing.Optional[str] = None
    room_name: typing.Optional[str] = None
    room_id: typing.Optional[str] = None
    is_procare_desktop_classroom_schedule_room: typing.Optional[bool] = None
    start_date: typing.Optional[str] = None
    start_date_ems_entry: typing.Optional[str] = None
    procare_start_date: typing.Optional[str] = None
    preferred_start_date: typing.Optional[str] = None
    withdrawal_date: typing.Optional[str] = None
    withdrawal_date_ems_entry: typing.Optional[str] = None
    withdrawal_date_estimated: typing.Optional[str] = None
    procare_withdrawal_date: typing.Optional[str] = None
    transition_date: typing.Optional[str] = None
    transition_room: typing.Optional[str] = None
    transition_room_id: typing.Optional[str] = None
    transition_room_override: typing.Optional[str] = None
    transition_room_override_id: typing.Optional[str] = None
    transition_date2: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transition_date_2"), pydantic.Field(alias="transition_date_2")
    ] = None
    transition_room2: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transition_room_2"), pydantic.Field(alias="transition_room_2")
    ] = None
    transition_room2id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transition_room_2_id"), pydantic.Field(alias="transition_room_2_id")
    ] = None
    days_in_room: typing.Optional[int] = None
    room_changed_at: typing.Optional[str] = None
    last_valid_room_changed_at: typing.Optional[str] = None
    old_room: typing.Optional[str] = None
    billing_plan: typing.Optional[str] = None
    part_time: typing.Optional[str] = None
    siblings: typing.Optional[str] = None
    staff_child: typing.Optional[str] = None
    ems_start_date: typing.Optional[str] = None
    ems_withdrawal_date: typing.Optional[str] = None
    lead_source: typing.Optional[str] = None
    color_hex: typing.Optional[str] = None
    short_name: typing.Optional[str] = None
    family_balance: typing.Optional[float] = None
    parent1name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parent_1_name"), pydantic.Field(alias="parent_1_name")
    ] = None
    parent1email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parent_1_email"), pydantic.Field(alias="parent_1_email")
    ] = None
    parent1mobile_phone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parent_1_mobile_phone"),
        pydantic.Field(alias="parent_1_mobile_phone"),
    ] = None
    parent2name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parent_2_name"), pydantic.Field(alias="parent_2_name")
    ] = None
    parent2email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parent_2_email"), pydantic.Field(alias="parent_2_email")
    ] = None
    parent2mobile_phone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parent_2_mobile_phone"),
        pydantic.Field(alias="parent_2_mobile_phone"),
    ] = None
    family_id: typing.Optional[str] = None
    last_day_attended: typing.Optional[str] = None
    days_since_last_attendance: typing.Optional[int] = None
    procare_desktop_status_end_date: typing.Optional[str] = None
    procare_desktop_enrollment_status: typing.Optional[str] = None
    procare_desktop_status_end_date_next: typing.Optional[dt.datetime] = None
    procare_desktop_enrollment_status_next: typing.Optional[str] = None
    is_created_from_procare_desktop: typing.Optional[bool] = None
    enrollment_id: typing.Optional[str] = None
    days_enrolled: typing.Optional[int] = None
    months_enrolled: typing.Optional[float] = None
    age_at_start_date: typing.Optional[float] = None
    age_at_withdrawal_date: typing.Optional[float] = None
    enrollment_eligibility: typing.Optional[float] = None
    eligible_months_capture: typing.Optional[float] = None
    eligible_months_lost: typing.Optional[float] = None
    withdrawal_type: typing.Optional[str] = None
    transition_alert: typing.Optional[str] = None
    transition_alert1clear: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transition_alert_1_clear"),
        pydantic.Field(alias="transition_alert_1_clear"),
    ] = None
    transition_alert2clear: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transition_alert_2_clear"),
        pydantic.Field(alias="transition_alert_2_clear"),
    ] = None
    transition_data_updated_by: typing.Optional[str] = None
    transition_data_updated_at: typing.Optional[dt.datetime] = None
    tracker_new_class: typing.Optional[str] = None
    address: typing.Optional[Address] = None
    field_labels: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    alerts: typing.Optional[typing.List[Alert]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
