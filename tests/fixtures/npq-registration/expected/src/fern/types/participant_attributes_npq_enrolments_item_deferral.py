

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_attributes_npq_enrolments_item_deferral_reason import (
    ParticipantAttributesNpqEnrolmentsItemDeferralReason,
)


class ParticipantAttributesNpqEnrolmentsItemDeferral(UniversalBaseModel):
    """
    The details of an NPQ Participant deferral
    """

    reason: ParticipantAttributesNpqEnrolmentsItemDeferralReason = pydantic.Field()
    """
    The reason a participant was deferred
    """

    date: dt.datetime = pydantic.Field()
    """
    The date and time the participant was deferred
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
