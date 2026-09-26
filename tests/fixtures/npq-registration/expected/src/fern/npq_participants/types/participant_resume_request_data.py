

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_resume_request_data_attributes import ParticipantResumeRequestDataAttributes


class ParticipantResumeRequestData(UniversalBaseModel):
    """
    A participant resume request data
    """

    type: str = pydantic.Field()
    """
    The data typed
    """

    attributes: ParticipantResumeRequestDataAttributes = pydantic.Field()
    """
    A participant resume request attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
