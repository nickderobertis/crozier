

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_defer_request_data_attributes_course_identifier import (
    ParticipantDeferRequestDataAttributesCourseIdentifier,
)
from .participant_defer_request_data_attributes_reason import ParticipantDeferRequestDataAttributesReason


class ParticipantDeferRequestDataAttributes(UniversalBaseModel):
    """
    A participant defer request attributes
    """

    course_identifier: ParticipantDeferRequestDataAttributesCourseIdentifier = pydantic.Field()
    """
    The type of course the participant is enrolled in
    """

    reason: ParticipantDeferRequestDataAttributesReason = pydantic.Field()
    """
    The reason for the deferral
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
