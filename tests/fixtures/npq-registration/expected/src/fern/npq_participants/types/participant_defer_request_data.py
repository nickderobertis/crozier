

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_defer_request_data_attributes import ParticipantDeferRequestDataAttributes


class ParticipantDeferRequestData(UniversalBaseModel):
    """
    A participant defer request data
    """

    type: str = pydantic.Field()
    """
    The data typed
    """

    attributes: ParticipantDeferRequestDataAttributes = pydantic.Field()
    """
    A participant defer request attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
