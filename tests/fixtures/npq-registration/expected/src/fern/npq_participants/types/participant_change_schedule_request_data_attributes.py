

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_change_schedule_request_data_attributes_course_identifier import (
    ParticipantChangeScheduleRequestDataAttributesCourseIdentifier,
)
from .participant_change_schedule_request_data_attributes_schedule_identifier import (
    ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier,
)


class ParticipantChangeScheduleRequestDataAttributes(UniversalBaseModel):
    """
    An NPQ participant change schedule request attributes
    """

    schedule_identifier: ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier = pydantic.Field()
    """
    The new schedule of the participant
    """

    course_identifier: ParticipantChangeScheduleRequestDataAttributesCourseIdentifier = pydantic.Field()
    """
    The type of course the participant is enrolled in
    """

    cohort: typing.Optional[str] = pydantic.Field(default=None)
    """
    Providers may change an NPQ participant's cohort up until the point of submitting a started declaration. The value indicates which call-off contract funds this participant's training. 2023 indicates a participant that has started, or will start, their training in the 2023/24 academic year.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
