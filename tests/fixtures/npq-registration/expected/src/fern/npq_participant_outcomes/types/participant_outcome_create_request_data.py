

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_outcome_create_request_data_attributes import ParticipantOutcomeCreateRequestDataAttributes


class ParticipantOutcomeCreateRequestData(UniversalBaseModel):
    """
    The NPQ outcome submission request attributes
    """

    type: str = pydantic.Field()
    """
    The data typed
    """

    attributes: ParticipantOutcomeCreateRequestDataAttributes = pydantic.Field()
    """
    The NPQ outcome submission request attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
