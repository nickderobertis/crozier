

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
from .transcript_optional_params_remove_audio_tags import TranscriptOptionalParamsRemoveAudioTags
from .transcript_optional_params_speaker_options import TranscriptOptionalParamsSpeakerOptions
from .transcript_optional_params_speech_understanding import TranscriptOptionalParamsSpeechUnderstanding


class TranscriptOptionalParams(UniversalBaseModel):
    """
    The parameters for creating a transcript
    """

    audio_end_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The point in time, in milliseconds, to stop transcribing in your media file. See [Set the start and end of the transcript](https://www.assemblyai.com/docs/pre-recorded-audio/set-the-start-and-end-of-the-transcript) for more details.
    """

    audio_start_from: typing.Optional[int] = pydantic.Field(default=None)
    """
    The point in time, in milliseconds, to begin transcribing in your media file. See [Set the start and end of the transcript](https://www.assemblyai.com/docs/pre-recorded-audio/set-the-start-and-end-of-the-transcript) for more details.
    """

    auto_chapters: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Auto Chapters](https://www.assemblyai.com/docs/speech-understanding/auto-chapters), can be true or false. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible chapter summaries. See the [updated Auto Chapters page](https://www.assemblyai.com/docs/speech-understanding/auto-chapters) for details.
    
    Note: This parameter is only supported for the Universal-2 model.
    """

    auto_highlights: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Key Phrases](https://www.assemblyai.com/docs/speech-understanding/key-phrases), either true or false
    """

    content_safety: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Content Moderation](https://www.assemblyai.com/docs/content-moderation), can be true or false
    """

    content_safety_confidence: typing.Optional[int] = pydantic.Field(default=None)
    """
    The confidence threshold for the [Content Moderation](https://www.assemblyai.com/docs/content-moderation) model. Values must be between 25 and 100.
    """

    custom_spelling: typing.Optional[typing.List[TranscriptCustomSpelling]] = pydantic.Field(default=None)
    """
    Customize how words are spelled and formatted using to and from values. See [Custom Spelling](https://www.assemblyai.com/docs/pre-recorded-audio/custom-spelling) for more details.
    """

    disfluencies: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Transcribe [Filler Words](https://www.assemblyai.com/docs/pre-recorded-audio/filler-words), like "umm", in your media file; can be true or false
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Enable domain-specific transcription models to improve accuracy for specialized terminology. Set to `"medical-v1"` to enable [Medical Mode](https://www.assemblyai.com/docs/pre-recorded-audio/medical-mode) for improved accuracy of medical terms such as medications, procedures, conditions, and dosages.
    
    Supported languages: English (`en`), Spanish (`es`), German (`de`), French (`fr`). If used with an unsupported language, the parameter is ignored and a warning is returned.
    """

    entity_detection: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Entity Detection](https://www.assemblyai.com/docs/speech-understanding/entity-detection), can be true or false
    """

    filter_profanity: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Filter profanity from the transcribed text, can be true or false. See [Profanity Filtering](https://www.assemblyai.com/docs/profanity-filtering) for more details.
    """

    format_text: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Text Formatting](https://www.assemblyai.com/docs/pre-recorded-audio), can be true or false
    """

    iab_categories: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Topic Detection](https://www.assemblyai.com/docs/speech-understanding/topic-detection), can be true or false
    """

    keyterms_prompt: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Improve accuracy with up to 200 (for Universal-2) or 1000 (for Universal-3 Pro) domain-specific words or phrases (maximum 6 words per phrase). See [Keyterms Prompting](https://www.assemblyai.com/docs/pre-recorded-audio/keyterms-prompting) for more details.
    """

    language_code: typing.Optional[TranscriptOptionalParamsLanguageCode] = pydantic.Field(default=None)
    """
    The language of your audio file. Possible values are found in [Supported Languages](https://www.assemblyai.com/docs/pre-recorded-audio/supported-languages).
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
    Defaults to 0. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    """

    language_detection: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Automatic language detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection), either true or false.
    """

    language_detection_options: typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions] = pydantic.Field(
        default=None
    )
    """
    Specify options for [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection).
    """

    multichannel: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Multichannel](https://www.assemblyai.com/docs/pre-recorded-audio/multichannel) transcription, can be true or false.
    """

    prompt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Provide natural language prompting of up to 1,500 words of contextual information to the model. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for best practices.
    
    Note: This parameter is only supported for the Universal-3 Pro model.
    """

    punctuate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Automatic Punctuation](https://www.assemblyai.com/docs/pre-recorded-audio), can be true or false
    """

    redact_pii: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Redact PII from the transcribed text using the Redact PII model, can be true or false. See [PII Redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    """

    redact_pii_audio: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Generate a copy of the original media file with spoken PII "beeped" out, can be true or false. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more details.
    """

    redact_pii_audio_options: typing.Optional[TranscriptOptionalParamsRedactPiiAudioOptions] = pydantic.Field(
        default=None
    )
    """
    Specify options for [PII redacted audio](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) files.
    """

    redact_pii_audio_quality: typing.Optional[RedactPiiAudioQuality] = pydantic.Field(default=None)
    """
    Controls the filetype of the audio created by redact_pii_audio. Currently supports mp3 (default) and wav. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more details.
    """

    redact_pii_policies: typing.Optional[typing.List[PiiPolicy]] = pydantic.Field(default=None)
    """
    The list of PII Redaction policies to enable. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    """

    redact_pii_sub: typing.Optional[SubstitutionPolicy] = pydantic.Field(default=None)
    """
    The replacement logic for detected PII, can be `entity_type` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    """

    sentiment_analysis: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Sentiment Analysis](https://www.assemblyai.com/docs/speech-understanding/sentiment-analysis), can be true or false
    """

    speaker_labels: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization), can be true or false
    """

    speaker_options: typing.Optional[TranscriptOptionalParamsSpeakerOptions] = pydantic.Field(default=None)
    """
    Specify options for [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization#set-a-range-of-possible-speakers). Use this to set a range of possible speakers.
    """

    speakers_expected: typing.Optional[int] = pydantic.Field(default=None)
    """
    Tells the speaker label model how many speakers it should attempt to identify. See [Set number of speakers expected](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization#set-number-of-speakers-expected) for more details.
    """

    speech_models: typing.List[SpeechModel] = pydantic.Field()
    """
    List multiple speech models in priority order, allowing our system to automatically route your audio to the best available option. See [Model Selection](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model) for available models and routing behavior.
    """

    speech_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    Reject audio files that contain less than this fraction of speech.
    Valid values are in the range [0, 1] inclusive. See [Speech Threshold](https://www.assemblyai.com/docs/speech-threshold) for more details.
    """

    speech_understanding: typing.Optional[TranscriptOptionalParamsSpeechUnderstanding] = pydantic.Field(default=None)
    """
    Enable speech understanding tasks like [Translation](https://www.assemblyai.com/docs/speech-understanding/translation), [Speaker Identification](https://www.assemblyai.com/docs/speech-understanding/speaker-identification), and [Custom Formatting](https://www.assemblyai.com/docs/speech-understanding/custom-formatting). See the task-specific docs for available options and configuration.
    """

    summarization: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization), can be true or false. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    
    Note: This parameter is only supported for the Universal-2 model.
    """

    summary_model: typing.Optional[SummaryModel] = pydantic.Field(default=None)
    """
    The model to summarize the transcript. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    """

    summary_type: typing.Optional[SummaryType] = pydantic.Field(default=None)
    """
    The type of summary. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    """

    remove_audio_tags: typing.Optional[TranscriptOptionalParamsRemoveAudioTags] = pydantic.Field(default=None)
    """
    Remove [audio event tags](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-pro#audio-event-tags) from the transcript text. Set to `"all"` to remove all audio tags.
    
    Note: This parameter is only supported for the Universal-3 Pro model.
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    Control the amount of randomness injected into the model's response. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for more details.
    
    Note: This parameter can only be used with the Universal-3 Pro model.
    """

    webhook_auth_header_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The header name to be sent with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests
    """

    webhook_auth_header_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The header value to send back with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests for added security
    """

    webhook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to which we send [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests.
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
