

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_withdraw_request_data_attributes_course_identifier import (
    ParticipantWithdrawRequestDataAttributesCourseIdentifier,
)
from .participant_withdraw_request_data_attributes_reason import ParticipantWithdrawRequestDataAttributesReason


class ParticipantWithdrawRequestDataAttributes(UniversalBaseModel):
    """
    A participant withdraw request attributes
    """

    course_identifier: ParticipantWithdrawRequestDataAttributesCourseIdentifier = pydantic.Field()
    """
    The type of course the participant is enrolled in
    """

    reason: ParticipantWithdrawRequestDataAttributesReason = pydantic.Field()
    """
    The reason for the withdrawal
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
