

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_resume_request_data_attributes_course_identifier import (
    ParticipantResumeRequestDataAttributesCourseIdentifier,
)


class ParticipantResumeRequestDataAttributes(UniversalBaseModel):
    """
    A participant resume request attributes
    """

    course_identifier: ParticipantResumeRequestDataAttributesCourseIdentifier = pydantic.Field()
    """
    The type of course the participant is enrolled in
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
