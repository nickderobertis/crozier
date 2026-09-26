

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_outcome import ParticipantOutcome


class ParticipantOutcomesResponse(UniversalBaseModel):
    """
    A list of participant outcomes
    """

    data: typing.List[ParticipantOutcome]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
