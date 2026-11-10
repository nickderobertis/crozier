

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .speaker_identification_request_body_speaker_identification_speaker_type import (
    SpeakerIdentificationRequestBodySpeakerIdentificationSpeakerType,
)


class SpeakerIdentificationRequestBodySpeakerIdentification(UniversalBaseModel):
    speaker_type: SpeakerIdentificationRequestBodySpeakerIdentificationSpeakerType = pydantic.Field()
    """
    Type of speaker identification
    """

    known_values: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Required if speaker_type is "role". Each value must be 35 characters or less.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
