

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id_attribute import IdAttribute
from .participant_outcome_attributes import ParticipantOutcomeAttributes
from .participant_outcome_type import ParticipantOutcomeType


class ParticipantOutcome(UniversalBaseModel):
    """
    The details of an NPQ outcome
    """

    id: IdAttribute
    type: ParticipantOutcomeType = pydantic.Field()
    """
    The data type
    """

    attributes: ParticipantOutcomeAttributes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
