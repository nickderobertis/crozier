

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SpeakerIdentificationRequestBodySpeakerIdentificationSpeakersItem(UniversalBaseModel):
    role: typing.Optional[str] = pydantic.Field(default=None)
    """
    The role of the speaker. Required when `speaker_type` is "role".
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the speaker. Required when `speaker_type` is "name".
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the speaker to help the model identify them based on conversational context.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
