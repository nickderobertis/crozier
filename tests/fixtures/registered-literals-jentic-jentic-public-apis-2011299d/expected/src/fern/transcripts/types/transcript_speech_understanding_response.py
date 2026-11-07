

import typing

from ...types.custom_formatting_response import CustomFormattingResponse
from ...types.speaker_identification_response import SpeakerIdentificationResponse
from ...types.translation_response import TranslationResponse

TranscriptSpeechUnderstandingResponse = typing.Union[
    TranslationResponse, SpeakerIdentificationResponse, CustomFormattingResponse
]
