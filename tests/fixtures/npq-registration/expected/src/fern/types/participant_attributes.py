

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_attributes_npq_enrolments_item import ParticipantAttributesNpqEnrolmentsItem
from .participant_attributes_participant_id_changes_item import ParticipantAttributesParticipantIdChangesItem


class ParticipantAttributes(UniversalBaseModel):
    full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full name of this NPQ participant
    """

    previous_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of previously used names
    """

    teacher_reference_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Teacher Reference Number (TRN) for this NPQ participant
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the application was last updated
    """

    npq_enrolments: typing.Optional[typing.List[ParticipantAttributesNpqEnrolmentsItem]] = pydantic.Field(default=None)
    """
    Information about the course(s) the participant is enrolled in
    """

    participant_id_changes: typing.Optional[typing.List[ParticipantAttributesParticipantIdChangesItem]] = (
        pydantic.Field(default=None)
    )
    """
    Information about the Participant ID changes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
