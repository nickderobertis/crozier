

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .pii_policy import PiiPolicy
from .redact_pii_audio_quality import RedactPiiAudioQuality
from .speech_model import SpeechModel
from .substitution_policy import SubstitutionPolicy
from .summary_model import SummaryModel
from .summary_type import SummaryType
from .transcript_custom_spelling import TranscriptCustomSpelling
from .transcript_optional_params_language_code import TranscriptOptionalParamsLanguageCode
from .transcript_optional_params_language_detection_options import TranscriptOptionalParamsLanguageDetectionOptions
from .transcript_optional_params_redact_pii_audio_options import TranscriptOptionalParamsRedactPiiAudioOptions
from .transcript_optional_params_speaker_options import TranscriptOptionalParamsSpeakerOptions
from .transcript_optional_params_speech_understanding import TranscriptOptionalParamsSpeechUnderstanding


class TranscriptOptionalParams(UniversalBaseModel):
    """
    The parameters for creating a transcript
    """

    audio_end_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The point in time, in milliseconds, to stop transcribing in your media file
    """

    audio_start_from: typing.Optional[int] = pydantic.Field(default=None)
    """
    The point in time, in milliseconds, to begin transcribing in your media file
    """

    auto_chapters: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Auto Chapters](https://www.assemblyai.com/docs/models/auto-chapters), can be true or false
    """

    auto_highlights: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable Key Phrases, either true or false
    """

    content_safety: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Content Moderation](https://www.assemblyai.com/docs/models/content-moderation), can be true or false
    """

    content_safety_confidence: typing.Optional[int] = pydantic.Field(default=None)
    """
    The confidence threshold for the Content Moderation model. Values must be between 25 and 100.
    """

    custom_spelling: typing.Optional[typing.List[TranscriptCustomSpelling]] = pydantic.Field(default=None)
    """
    Customize how words are spelled and formatted using to and from values
    """

    disfluencies: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Transcribe Filler Words, like "umm", in your media file; can be true or false
    """

    entity_detection: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Entity Detection](https://www.assemblyai.com/docs/models/entity-detection), can be true or false
    """

    filter_profanity: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Filter profanity from the transcribed text, can be true or false
    """

    format_text: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable Text Formatting, can be true or false
    """

    iab_categories: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Topic Detection](https://www.assemblyai.com/docs/models/topic-detection), can be true or false
    """

    keyterms_prompt: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Improve accuracy with up to 200 (for Universal-2) or 1000 (for Universal-3-Pro) domain-specific words or phrases (maximum 6 words per phrase).
    """

    language_code: typing.Optional[TranscriptOptionalParamsLanguageCode] = pydantic.Field(default=None)
    """
    The language of your audio file. Possible values are found in [Supported Languages](https://www.assemblyai.com/docs/concepts/supported-languages).
    The default value is 'en_us'.
    """

    language_codes: typing.Optional[typing.List["TranscriptLanguageCode"]] = pydantic.Field(default=None)
    """
    The language codes of your audio file. Used for [Code switching](/docs/speech-to-text/pre-recorded-audio/code-switching)
    One of the values specified must be `en`.
    """

    language_confidence_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    The confidence threshold for the automatically detected language.
    An error will be returned if the language confidence is below this threshold.
    Defaults to 0.
    """

    language_detection: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Automatic language detection](https://www.assemblyai.com/docs/models/speech-recognition#automatic-language-detection), either true or false.
    """

    language_detection_options: typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions] = pydantic.Field(
        default=None
    )
    """
    Specify options for Automatic Language Detection.
    """

    multichannel: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Multichannel](https://www.assemblyai.com/docs/models/speech-recognition#multichannel-transcription) transcription, can be true or false.
    """

    prompt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Provide natural language prompting of up to 1,500 words of contextual information to the model.
    
    Note: This parameter is only supported for the Universal-3-Pro model.
    """

    punctuate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable Automatic Punctuation, can be true or false
    """

    redact_pii: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Redact PII from the transcribed text using the Redact PII model, can be true or false
    """

    redact_pii_audio: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Generate a copy of the original media file with spoken PII "beeped" out, can be true or false. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.
    """

    redact_pii_audio_options: typing.Optional[TranscriptOptionalParamsRedactPiiAudioOptions] = pydantic.Field(
        default=None
    )
    """
    Specify options for PII redacted audio files.
    """

    redact_pii_audio_quality: typing.Optional[RedactPiiAudioQuality] = pydantic.Field(default=None)
    """
    Controls the filetype of the audio created by redact_pii_audio. Currently supports mp3 (default) and wav. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.
    """

    redact_pii_policies: typing.Optional[typing.List[PiiPolicy]] = pydantic.Field(default=None)
    """
    The list of PII Redaction policies to enable. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.
    """

    redact_pii_sub: typing.Optional[SubstitutionPolicy] = pydantic.Field(default=None)
    """
    The replacement logic for detected PII, can be `entity_type` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.
    """

    sentiment_analysis: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Sentiment Analysis](https://www.assemblyai.com/docs/models/sentiment-analysis), can be true or false
    """

    speaker_labels: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Speaker diarization](https://www.assemblyai.com/docs/models/speaker-diarization), can be true or false
    """

    speaker_options: typing.Optional[TranscriptOptionalParamsSpeakerOptions] = pydantic.Field(default=None)
    """
    Specify options for speaker diarization.
    """

    speakers_expected: typing.Optional[int] = pydantic.Field(default=None)
    """
    Tells the speaker label model how many speakers it should attempt to identify. See [Speaker diarization](https://www.assemblyai.com/docs/models/speaker-diarization) for more details.
    """

    speech_models: typing.List[SpeechModel] = pydantic.Field()
    """
    List multiple speech models in priority order, allowing our system to automatically route your audio to the best available option.
    """

    speech_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    Reject audio files that contain less than this fraction of speech.
    Valid values are in the range [0, 1] inclusive.
    """

    speech_understanding: typing.Optional[TranscriptOptionalParamsSpeechUnderstanding] = pydantic.Field(default=None)
    """
    Enable speech understanding tasks like translation, speaker identification, and custom formatting
    """

    summarization: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Summarization](https://www.assemblyai.com/docs/models/summarization), can be true or false
    """

    summary_model: typing.Optional[SummaryModel] = pydantic.Field(default=None)
    """
    The model to summarize the transcript
    """

    summary_type: typing.Optional[SummaryType] = pydantic.Field(default=None)
    """
    The type of summary
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    Control the amount of randomness injected into the model's response.
    
    Note: This parameter can only be used with the Universal-3-Pro model.
    """

    webhook_auth_header_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The header name to be sent with the transcript completed or failed webhook requests
    """

    webhook_auth_header_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The header value to send back with the transcript completed or failed webhook requests for added security
    """

    webhook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to which we send webhook requests.
    We sends two different types of webhook requests.
    One request when a transcript is completed or failed, and one request when the redacted audio is ready if redact_pii_audio is enabled.
    """

    custom_topics: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This parameter does not currently have any functionality attached to it.
    """

    speech_model: typing.Optional[SpeechModel] = pydantic.Field(default=None)
    """
    This parameter has been replaced with the `speech_models` parameter, learn more about the `speech_models` parameter [here](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model).
    """

    topics: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    This parameter does not currently have any functionality attached to it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .transcript_language_code import TranscriptLanguageCode

update_forward_refs(TranscriptOptionalParams, TranscriptLanguageCode=TranscriptLanguageCode)
