

import typing

from ...types.custom_formatting_request_body import CustomFormattingRequestBody
from ...types.speaker_identification_request_body import SpeakerIdentificationRequestBody
from ...types.translation_request_body import TranslationRequestBody

TranscriptSpeechUnderstandingRequest = typing.Union[
    TranslationRequestBody, SpeakerIdentificationRequestBody, CustomFormattingRequestBody
]
