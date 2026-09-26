

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_outcome_create_request_data_attributes_course_identifier import (
    ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier,
)
from .participant_outcome_create_request_data_attributes_state import ParticipantOutcomeCreateRequestDataAttributesState


class ParticipantOutcomeCreateRequestDataAttributes(UniversalBaseModel):
    """
    The NPQ outcome submission request attributes
    """

    course_identifier: ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier = pydantic.Field()
    """
    The type of course the participant is enrolled in
    """

    state: ParticipantOutcomeCreateRequestDataAttributesState = pydantic.Field()
    """
    The state of the outcome (passed or failed)
    """

    completion_date: str = pydantic.Field()
    """
    The date the participant received the assessment outcome for this course
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
