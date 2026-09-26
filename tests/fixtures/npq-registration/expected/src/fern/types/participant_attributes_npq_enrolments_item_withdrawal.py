

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_attributes_npq_enrolments_item_withdrawal_reason import (
    ParticipantAttributesNpqEnrolmentsItemWithdrawalReason,
)


class ParticipantAttributesNpqEnrolmentsItemWithdrawal(UniversalBaseModel):
    """
    The details of an NPQ Participant withdrawal
    """

    reason: ParticipantAttributesNpqEnrolmentsItemWithdrawalReason = pydantic.Field()
    """
    The reason a participant was withdrawn
    """

    date: dt.datetime = pydantic.Field()
    """
    The date and time the participant was withdrawn
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
