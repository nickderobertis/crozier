

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .speaker_identification_request_body_speaker_identification_speaker_type import (
    SpeakerIdentificationRequestBodySpeakerIdentificationSpeakerType,
)
from .speaker_identification_request_body_speaker_identification_speakers_item import (
    SpeakerIdentificationRequestBodySpeakerIdentificationSpeakersItem,
)


class SpeakerIdentificationRequestBodySpeakerIdentification(UniversalBaseModel):
    speaker_type: SpeakerIdentificationRequestBodySpeakerIdentificationSpeakerType = pydantic.Field()
    """
    Type of speaker identification. See [Speaker Identification](https://www.assemblyai.com/docs/speech-understanding/speaker-identification) for details on each type.
    """

    known_values: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Required if speaker_type is "role". Each value must be 35 characters or less.
    """

    speakers: typing.Optional[typing.List[SpeakerIdentificationRequestBodySpeakerIdentificationSpeakersItem]] = (
        pydantic.Field(default=None)
    )
    """
    An array of speaker objects with metadata to improve identification accuracy. Each object should include a `role` or `name` (depending on `speaker_type`) and an optional `description` to help the model identify the speaker. You can also include any additional custom properties (e.g., `company`, `title`) to provide more context. Use this as an alternative to `known_values` when you want to provide additional context about each speaker.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
