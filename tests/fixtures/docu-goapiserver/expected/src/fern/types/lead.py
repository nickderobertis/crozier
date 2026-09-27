

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert import Alert
from .available_space import AvailableSpace


class Lead(UniversalBaseModel):
    """
    Lead.
    """

    lead_id: str = pydantic.Field()
    """
    Lead id.
    """

    monday_item_id: str = pydantic.Field()
    """
    Monday item id.
    """

    first_name: str
    last_name: str
    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    status: str
    date_of_birth: str
    current_age: typing.Optional[float] = pydantic.Field(default=None)
    """
    Child age in months.
    """

    intended_start_date: str
    periods_lead_room_available: typing.Optional[typing.List[AvailableSpace]] = None
    parent1name: typing_extensions.Annotated[
        str, FieldMetadata(alias="parent1_name"), pydantic.Field(alias="parent1_name")
    ]
    parent1email: typing_extensions.Annotated[
        str, FieldMetadata(alias="parent1_email"), pydantic.Field(alias="parent1_email")
    ]
    parent1mobile: typing_extensions.Annotated[
        str, FieldMetadata(alias="parent1_mobile"), pydantic.Field(alias="parent1_mobile")
    ]
    created_at: str
    updated_at: str
    available_space: str
    available_space_match: str
    available_space_match_persisted: typing.Optional[dt.datetime] = None
    source: str
    intellikid_status: str
    intellikid_children_status: str
    intellikid_lead_status: str
    intellikid_source: str
    notes: str
    student_status: str
    procare_desktop_enrollment_status: str
    onboarding_status: str
    ems_status: str
    start_date: str
    withdrawal_date: str
    lineleader_child_id: typing.Optional[int] = None
    lineleader_family_id: typing.Optional[int] = None
    lineleader_center_id: typing.Optional[int] = None
    lineleader_center_name: typing.Optional[str] = None
    lineleader_status: typing.Optional[str] = None
    lineleader_classroom: typing.Optional[str] = None
    lineleader_child_flagged_as_duplicated: bool
    stage_inquiry_call_completed: str = pydantic.Field()
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    stage_tour_completed: str = pydantic.Field()
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    stage_not_viable: str = pydantic.Field()
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    stage_not_interested: str = pydantic.Field()
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    stage_no_response: str = pydantic.Field()
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    stage_no_response_timed_out: str = pydantic.Field()
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    is_crm_intended_start_date: bool
    lead_to_enrollment_date: typing.Optional[float] = None
    age_at_start_date_months: typing.Optional[float] = None
    age_at_lead_created_at_months: typing.Optional[float] = None
    alerts: typing.Optional[typing.List[Alert]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
