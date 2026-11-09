

import typing

from ...types.action_items_request_body import ActionItemsRequestBody
from ...types.custom_formatting_request_body import CustomFormattingRequestBody
from ...types.speaker_identification_request_body import SpeakerIdentificationRequestBody
from ...types.summarization_request_body import SummarizationRequestBody
from ...types.translation_request_body import TranslationRequestBody

TranscriptSpeechUnderstandingRequest = typing.Union[
    TranslationRequestBody,
    SpeakerIdentificationRequestBody,
    CustomFormattingRequestBody,
    SummarizationRequestBody,
    ActionItemsRequestBody,
]
