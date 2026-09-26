

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert import Alert
from .available_space import AvailableSpace


class LeadProjection(UniversalBaseModel):
    """
    Lead Projection.
    """

    lead_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Lead id.
    """

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
    status: typing.Optional[str] = None
    date_of_birth: typing.Optional[str] = None
    current_age: typing.Optional[float] = None
    intended_start_date: typing.Optional[str] = None
    periods_lead_room_available: typing.Optional[typing.List[AvailableSpace]] = None
    parent1name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parent1_name"), pydantic.Field(alias="parent1_name")
    ] = None
    parent1email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parent1_email"), pydantic.Field(alias="parent1_email")
    ] = None
    parent1mobile: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parent1_mobile"), pydantic.Field(alias="parent1_mobile")
    ] = None
    created_at: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None
    available_space: typing.Optional[str] = None
    source: typing.Optional[str] = None
    intellikid_status: typing.Optional[str] = None
    intellikid_children_status: typing.Optional[str] = None
    intellikid_lead_status: typing.Optional[str] = None
    intellikid_source: typing.Optional[str] = None
    notes: typing.Optional[str] = None
    student_status: typing.Optional[str] = None
    onboarding_status: typing.Optional[str] = None
    ems_status: typing.Optional[str] = None
    start_date: typing.Optional[str] = None
    withdrawal_date: typing.Optional[str] = None
    lineleader_child_id: typing.Optional[int] = None
    lineleader_family_id: typing.Optional[int] = None
    lineleader_center_id: typing.Optional[int] = None
    lineleader_center_name: typing.Optional[str] = None
    lineleader_status: typing.Optional[str] = None
    lineleader_classroom: typing.Optional[str] = None
    stage_inquiry_call_completed: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    stage_tour_completed: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    stage_not_viable: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    stage_not_interested: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    stage_no_response: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    stage_no_response_timed_out: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stage value as a string in the read representation; PATCH uses a boolean.
    """

    is_crm_intended_start_date: typing.Optional[bool] = None
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
