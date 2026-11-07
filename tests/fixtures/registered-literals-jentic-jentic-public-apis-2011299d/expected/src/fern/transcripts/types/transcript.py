

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .auto_highlights_result import AutoHighlightsResult
from .chapter import Chapter
from .content_safety_labels_result import ContentSafetyLabelsResult
from .entity import Entity
from .pii_policy import PiiPolicy
from .redact_pii_audio_quality import RedactPiiAudioQuality
from .sentiment_analysis_result import SentimentAnalysisResult
from .speech_model import SpeechModel
from .substitution_policy import SubstitutionPolicy
from .topic_detection_model_result import TopicDetectionModelResult
from .transcript_custom_spelling import TranscriptCustomSpelling
from .transcript_language_detection_options import TranscriptLanguageDetectionOptions
from .transcript_redact_pii_audio_options import TranscriptRedactPiiAudioOptions
from .transcript_remove_audio_tags import TranscriptRemoveAudioTags
from .transcript_speech_understanding import TranscriptSpeechUnderstanding
from .transcript_status import TranscriptStatus
from .transcript_translated_texts import TranscriptTranslatedTexts
from .transcript_utterance import TranscriptUtterance
from .transcript_word import TranscriptWord


class Transcript(UniversalBaseModel):
    """
    A transcript object
    """

    audio_channels: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of audio channels in the audio file. This is only present when [multichannel](https://www.assemblyai.com/docs/pre-recorded-audio/multichannel) is enabled.
    """

    audio_duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    The duration of this transcript object's media file, in seconds
    """

    audio_end_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The point in time, in milliseconds, in the file at which the transcription was terminated. See [Set the start and end of the transcript](https://www.assemblyai.com/docs/pre-recorded-audio/set-the-start-and-end-of-the-transcript) for more details.
    """

    audio_start_from: typing.Optional[int] = pydantic.Field(default=None)
    """
    The point in time, in milliseconds, in the file at which the transcription was started. See [Set the start and end of the transcript](https://www.assemblyai.com/docs/pre-recorded-audio/set-the-start-and-end-of-the-transcript) for more details.
    """

    audio_url: str = pydantic.Field()
    """
    The URL of the media that was transcribed
    """

    auto_chapters: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Auto Chapters](https://www.assemblyai.com/docs/speech-understanding/auto-chapters) is enabled, can be true or false. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible chapter summaries. See the [updated Auto Chapters page](https://www.assemblyai.com/docs/speech-understanding/auto-chapters) for details.
    
    Note: This parameter is only supported for the Universal-2 model.
    """

    auto_highlights: bool = pydantic.Field()
    """
    Whether [Key Phrases](https://www.assemblyai.com/docs/speech-understanding/key-phrases) is enabled, either true or false
    """

    auto_highlights_result: typing.Optional[AutoHighlightsResult] = pydantic.Field(default=None)
    """
    An array of results for the Key Phrases model, if it is enabled.
    See [Key Phrases](https://www.assemblyai.com/docs/speech-understanding/key-phrases) for more information.
    """

    chapters: typing.Optional[typing.List[Chapter]] = pydantic.Field(default=None)
    """
    An array of temporally sequential chapters for the audio file. See [Auto Chapters](https://www.assemblyai.com/docs/speech-understanding/auto-chapters) for more information.
    """

    confidence: typing.Optional[float] = pydantic.Field(default=None)
    """
    The confidence score for the transcript, between 0.0 (low confidence) and 1.0 (high confidence)
    """

    content_safety: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Content Moderation](https://www.assemblyai.com/docs/content-moderation) is enabled, can be true or false
    """

    content_safety_labels: typing.Optional[ContentSafetyLabelsResult] = pydantic.Field(default=None)
    """
    An array of results for the Content Moderation model, if it is enabled.
    See [Content moderation](https://www.assemblyai.com/docs/content-moderation) for more information.
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
    The domain-specific model applied to the transcript. When set to `"medical-v1"`, [Medical Mode](https://www.assemblyai.com/docs/pre-recorded-audio/medical-mode) was used to improve accuracy for medical terminology.
    """

    entities: typing.Optional[typing.List[Entity]] = pydantic.Field(default=None)
    """
    An array of results for the Entity Detection model, if it is enabled.
    See [Entity detection](https://www.assemblyai.com/docs/speech-understanding/entity-detection) for more information.
    """

    entity_detection: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Entity Detection](https://www.assemblyai.com/docs/speech-understanding/entity-detection) is enabled, can be true or false
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message of why the transcript failed
    """

    filter_profanity: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Profanity Filtering](https://www.assemblyai.com/docs/profanity-filtering) is enabled, either true or false
    """

    format_text: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Text Formatting](https://www.assemblyai.com/docs/pre-recorded-audio) is enabled, either true or false
    """

    iab_categories: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Topic Detection](https://www.assemblyai.com/docs/speech-understanding/topic-detection) is enabled, can be true or false
    """

    iab_categories_result: typing.Optional[TopicDetectionModelResult] = pydantic.Field(default=None)
    """
    The result of the Topic Detection model, if it is enabled.
    See [Topic Detection](https://www.assemblyai.com/docs/speech-understanding/topic-detection) for more information.
    """

    id: str = pydantic.Field()
    """
    The unique identifier of your transcript
    """

    keyterms_prompt: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Improve accuracy with up to 200 (for Universal-2) or 1000 (for Universal-3 Pro) domain-specific words or phrases (maximum 6 words per phrase). See [Keyterms Prompting](https://www.assemblyai.com/docs/pre-recorded-audio/keyterms-prompting) for more details.
    """

    language_code: typing.Optional["TranscriptLanguageCode"] = pydantic.Field(default=None)
    """
    The language of your audio file.
    Possible values are found in [Supported Languages](https://www.assemblyai.com/docs/pre-recorded-audio/supported-languages).
    The default value is 'en_us'.
    """

    language_codes: typing.Optional[typing.List["TranscriptLanguageCode"]] = pydantic.Field(default=None)
    """
    The language codes of your audio file. Used for [Code switching](/docs/speech-to-text/pre-recorded-audio/code-switching)
    One of the values specified must be `en`.
    """

    language_confidence: typing.Optional[float] = pydantic.Field(default=None)
    """
    The confidence score for the detected language, between 0.0 (low confidence) and 1.0 (high confidence). See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    """

    language_confidence_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    The confidence threshold for the automatically detected language.
    An error will be returned if the language confidence is below this threshold.
    See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    """

    language_detection: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Automatic language detection](/docs/pre-recorded-audio/automatic-language-detection) is enabled, either true or false
    """

    language_detection_options: typing.Optional[TranscriptLanguageDetectionOptions] = pydantic.Field(default=None)
    """
    Specify options for [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection).
    """

    multichannel: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Multichannel transcription](https://www.assemblyai.com/docs/pre-recorded-audio/multichannel) was enabled in the transcription request, either true or false
    """

    prompt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Provide natural language prompting of up to 1,500 words of contextual information to the model. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for best practices.
    
    Note: This parameter is only supported for the Universal-3 Pro model.
    """

    punctuate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Automatic Punctuation](https://www.assemblyai.com/docs/pre-recorded-audio) is enabled, either true or false
    """

    redact_pii: bool = pydantic.Field()
    """
    Whether [PII Redaction](https://www.assemblyai.com/docs/pii-redaction) is enabled, either true or false
    """

    redact_pii_audio: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether a redacted version of the audio file was generated,
    either true or false. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more information.
    """

    redact_pii_audio_options: typing.Optional[TranscriptRedactPiiAudioOptions] = pydantic.Field(default=None)
    """
    The options for PII-redacted audio, if redact_pii_audio is enabled.
    See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more information.
    """

    redact_pii_audio_quality: typing.Optional[RedactPiiAudioQuality] = pydantic.Field(default=None)
    """
    The audio quality of the PII-redacted audio file, if redact_pii_audio is enabled.
    See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more information.
    """

    redact_pii_policies: typing.Optional[typing.List[PiiPolicy]] = pydantic.Field(default=None)
    """
    The list of PII Redaction policies that were enabled, if PII Redaction is enabled.
    See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more information.
    """

    redact_pii_sub: typing.Optional[SubstitutionPolicy] = pydantic.Field(default=None)
    """
    The replacement logic for detected PII, can be `entity_type` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    """

    sentiment_analysis: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Sentiment Analysis](https://www.assemblyai.com/docs/speech-understanding/sentiment-analysis) is enabled, can be true or false
    """

    sentiment_analysis_results: typing.Optional[typing.List[SentimentAnalysisResult]] = pydantic.Field(default=None)
    """
    An array of results for the Sentiment Analysis model, if it is enabled.
    See [Sentiment Analysis](https://www.assemblyai.com/docs/speech-understanding/sentiment-analysis) for more information.
    """

    speaker_labels: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization) is enabled, can be true or false
    """

    speakers_expected: typing.Optional[int] = pydantic.Field(default=None)
    """
    Tell the speaker label model how many speakers it should attempt to identify. See [Set number of speakers expected](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization#set-number-of-speakers-expected) for more details.
    """

    speech_model_used: typing.Optional[SpeechModel] = pydantic.Field(default=None)
    """
    The speech model that was actually used for the transcription. See [Model Selection](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model) for available models.
    """

    speech_models: typing.Optional[typing.List[SpeechModel]] = pydantic.Field(default=None)
    """
    List multiple speech models in priority order, allowing our system to automatically route your audio to the best available option. See [Model Selection](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model) for available models and routing behavior.
    """

    speech_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    Defaults to null. Reject audio files that contain less than this fraction of speech.
    Valid values are in the range [0, 1] inclusive. See [Speech Threshold](https://www.assemblyai.com/docs/speech-threshold) for more details.
    """

    speech_understanding: typing.Optional[TranscriptSpeechUnderstanding] = pydantic.Field(default=None)
    """
    Speech understanding tasks like [Translation](https://www.assemblyai.com/docs/speech-understanding/translation), [Speaker Identification](https://www.assemblyai.com/docs/speech-understanding/speaker-identification), and [Custom Formatting](https://www.assemblyai.com/docs/speech-understanding/custom-formatting). See the task-specific docs for available options and configuration.
    """

    status: TranscriptStatus = pydantic.Field()
    """
    The status of your transcript. Possible values are queued, processing, completed, or error.
    """

    summarization: bool = pydantic.Field()
    """
    Whether [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization) is enabled, either true or false. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    
    Note: This parameter is only supported for the Universal-2 model.
    """

    summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    The generated summary of the media file, if [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization) is enabled. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    """

    summary_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Summarization model used to generate the summary,
    if [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization#summary-models) is enabled. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    """

    summary_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of summary generated, if [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization#summary-types) is enabled. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/overview) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    """

    remove_audio_tags: typing.Optional[TranscriptRemoveAudioTags] = pydantic.Field(default=None)
    """
    Whether [audio event tags](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-pro#audio-event-tags) were removed from the transcript text.
    
    Note: This parameter is only supported for the Universal-3 Pro model.
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    The temperature that was used for the model's response. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for more details.
    
    Note: This parameter can only be used with the Universal-3 Pro model.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The textual transcript of your media file
    """

    throttled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True while a request is throttled and false when a request is no longer throttled
    """

    utterances: typing.Optional[typing.List[TranscriptUtterance]] = pydantic.Field(default=None)
    """
    When multichannel or speaker_labels is enabled, a list of turn-by-turn utterance objects.
    See [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization) and [Multichannel transcription](https://www.assemblyai.com/docs/pre-recorded-audio/multichannel) for more information.
    """

    webhook_auth: bool = pydantic.Field()
    """
    Whether [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) authentication details were provided
    """

    webhook_auth_header_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The header name to be sent with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests
    """

    webhook_status_code: typing.Optional[int] = pydantic.Field(default=None)
    """
    The status code we received from your server when delivering the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) request, if a webhook URL was provided
    """

    webhook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to which we send [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests.
    """

    words: typing.Optional[typing.List[TranscriptWord]] = pydantic.Field(default=None)
    """
    An array of temporally-sequential word objects, one for each word in the transcript.
    """

    acoustic_model: str = pydantic.Field()
    """
    This parameter does not currently have any functionality attached to it.
    """

    custom_topics: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This parameter does not currently have any functionality attached to it.
    """

    language_model: str = pydantic.Field()
    """
    This parameter does not currently have any functionality attached to it.
    """

    speech_model: typing.Optional[SpeechModel] = pydantic.Field(default=None)
    """
    This parameter has been replaced with the `speech_models` parameter, learn more about the `speech_models` parameter [here](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model).
    """

    speed_boost: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This parameter does not currently have any functionality attached to it.
    """

    topics: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    This parameter does not currently have any functionality attached to it.
    """

    translated_texts: typing.Optional[TranscriptTranslatedTexts] = pydantic.Field(default=None)
    """
    Translated text keyed by language code. See [Translation](https://www.assemblyai.com/docs/speech-understanding/translation) for more details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .transcript_language_code import TranscriptLanguageCode

update_forward_refs(Transcript, TranscriptLanguageCode=TranscriptLanguageCode)
