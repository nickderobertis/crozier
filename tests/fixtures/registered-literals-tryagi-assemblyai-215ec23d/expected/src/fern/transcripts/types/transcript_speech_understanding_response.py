

import typing

from ...types.action_items_response import ActionItemsResponse
from ...types.custom_formatting_response import CustomFormattingResponse
from ...types.speaker_identification_response import SpeakerIdentificationResponse
from ...types.summarization_response import SummarizationResponse
from ...types.translation_response import TranslationResponse

TranscriptSpeechUnderstandingResponse = typing.Union[
    TranslationResponse,
    SpeakerIdentificationResponse,
    CustomFormattingResponse,
    SummarizationResponse,
    ActionItemsResponse,
]
