

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .speaker_identification_response_speaker_identification import SpeakerIdentificationResponseSpeakerIdentification


class SpeakerIdentificationResponse(UniversalBaseModel):
    speaker_identification: typing.Optional[SpeakerIdentificationResponseSpeakerIdentification] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
