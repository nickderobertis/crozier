

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_outcome_attributes_course_identifier import ParticipantOutcomeAttributesCourseIdentifier
from .participant_outcome_attributes_state import ParticipantOutcomeAttributesState


class ParticipantOutcomeAttributes(UniversalBaseModel):
    state: typing.Optional[ParticipantOutcomeAttributesState] = pydantic.Field(default=None)
    """
    The state of the outcome (passed or failed)
    """

    completion_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the participant received the assessment outcome for this course
    """

    course_identifier: typing.Optional[ParticipantOutcomeAttributesCourseIdentifier] = pydantic.Field(default=None)
    """
    The NPQ course this NPQ application relates to
    """

    participant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of this NPQ participant
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date you created the participant-outcome record
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the participant-outcome record was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
