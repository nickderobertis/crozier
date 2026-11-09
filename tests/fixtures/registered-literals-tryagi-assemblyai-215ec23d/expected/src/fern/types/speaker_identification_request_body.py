

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .speaker_identification_request_body_speaker_identification import (
    SpeakerIdentificationRequestBodySpeakerIdentification,
)


class SpeakerIdentificationRequestBody(UniversalBaseModel):
    """
    Request body for [Speaker Identification](https://www.assemblyai.com/docs/speech-understanding/speaker-identification).
    """

    speaker_identification: SpeakerIdentificationRequestBodySpeakerIdentification

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
