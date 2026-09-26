

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id_attribute import IdAttribute
from .participant_attributes import ParticipantAttributes
from .participant_type import ParticipantType


class Participant(UniversalBaseModel):
    """
    The details of an NPQ Participant
    """

    id: IdAttribute
    type: ParticipantType = pydantic.Field()
    """
    The data type
    """

    attributes: ParticipantAttributes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
