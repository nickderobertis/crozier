

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
from .transcript_optional_params_domain import TranscriptOptionalParamsDomain
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
    Enable [Auto Chapters](https://www.assemblyai.com/docs/speech-understanding/auto-chapters), can be true or false. Requires `punctuate` to be `true`, and cannot be enabled together with `summarization`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible chapter summaries. See the [updated Auto Chapters page](https://www.assemblyai.com/docs/speech-understanding/auto-chapters) for details.
    
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
    The confidence threshold for the [Content Moderation](https://www.assemblyai.com/docs/content-moderation) model. Values must be between 25 and 100. Requires `content_safety` to be enabled; otherwise it's ignored.
    """

    custom_spelling: typing.Optional[typing.List[TranscriptCustomSpelling]] = pydantic.Field(default=None)
    """
    Customize how words are spelled and formatted using to and from values. Each `to` value must be a single word, and each `from` phrase can contain at most 5 words. See [Custom Spelling](https://www.assemblyai.com/docs/pre-recorded-audio/correct-spelling-of-terms) for more details.
    """

    disfluencies: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Transcribe [Filler Words](https://www.assemblyai.com/docs/pre-recorded-audio/include-filler-words), like "umm", in your media file; can be true or false. Supported on Universal-3.5 Pro and Universal-2.
    """

    domain: typing.Optional[TranscriptOptionalParamsDomain] = pydantic.Field(default=None)
    """
    Enable domain-specific transcription models to improve accuracy for specialized terminology. Set to `"medical-v1"` to enable [Medical Mode](https://www.assemblyai.com/docs/pre-recorded-audio/medical-mode) for improved accuracy of medical terms such as medications, procedures, conditions, and dosages.
    
    Supported languages: English (`en`), Spanish (`es`), German (`de`), French (`fr`). If `medical-v1` is used with an unsupported language, the parameter is ignored and a warning is returned.
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
    Improve accuracy with up to 200 (for Universal-2) or 1000 (for Universal-3.5 Pro) domain-specific words or phrases (maximum 6 words per phrase). See [Keyterms Prompting](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro/prompting#keyterms-prompting) for more details.
    """

    language_code: typing.Optional[TranscriptOptionalParamsLanguageCode] = pydantic.Field(default=None)
    """
    The language of your audio file. Possible values are found in [Supported Languages](https://www.assemblyai.com/docs/pre-recorded-audio/supported-languages).
    If you don't specify a language, it's detected automatically. Cannot be used together with `language_detection`.
    """

    language_codes: typing.Optional[typing.List["TranscriptLanguageCode"]] = pydantic.Field(default=None)
    """
    The language codes of your audio file. Used for [Code switching](/speech-to-text/pre-recorded-audio/code-switching)
    One of the values specified must be `en`.
    """

    language_confidence_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    The confidence threshold for the automatically detected language.
    An error will be returned if the language confidence is below this threshold.
    Defaults to 0. Can only be set when `language_detection` is enabled. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    """

    language_detection: typing.Optional[bool] = pydantic.Field(default=None)
    """
    [Automatic language detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) identifies the spoken language and routes the request to the best model. It's applied automatically when you don't specify a `language_code`. Set to `false` only together with a `language_code`; disabling it without specifying a language returns an error.
    """

    language_detection_options: typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions] = pydantic.Field(
        default=None
    )
    """
    Specify options for [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection).
    """

    multichannel: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Multichannel](https://www.assemblyai.com/docs/pre-recorded-audio/transcribe-multiple-audio-channels) transcription, can be true or false.
    """

    prompt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Provide natural language prompting of up to 1,500 words of contextual information to the model. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for best practices.
    
    Note: This parameter is only supported for the Universal-3.5 Pro model.
    """

    punctuate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Automatic Punctuation](https://www.assemblyai.com/docs/pre-recorded-audio), can be true or false
    """

    redact_pii: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Redact PII from the transcribed text using the Redact PII model, can be true or false. Requires `format_text` to be `true`. See [PII Redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    """

    redact_pii_audio: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Generate a copy of the original media file with spoken PII "beeped" out, can be true or false. Requires `redact_pii` to be `true`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more details.
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
    The replacement logic for detected PII, can be `entity_name` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    """

    redact_pii_return_unredacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When set to `true`, returns the original unredacted transcript alongside the redacted one in the same response. Requires `redact_pii` to be `true`, otherwise a 400 error is returned.
    
    When enabled, the response includes the additional fields `unredacted_text`, `unredacted_words`, and `unredacted_utterances`. The existing `text`, `words`, and `utterances` fields remain fully redacted. When disabled (default), the response is unchanged and contains only the redacted transcript. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    """

    redact_static_entities: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic.Field(default=None)
    """
    A map of user-defined terms to redact, where each key is a redaction label and each value is a list of exact terms to match (e.g. `{ "INTERNAL_TOOL": ["Bearclaw", "Cubclaw"] }`). Each matching term in the transcript is redacted using the `redact_pii_sub` substitution, on top of standard PII Redaction. Useful for redacting specific, predefined terms (proprietary names, internal codenames) that aren't general PII categories.
    
    This is a literal find-and-replace (tolerant of casing, surrounding punctuation, and minor spacing/hyphenation), not a model — it does not generalize beyond the terms you provide. Requires `redact_pii` to be `true`, otherwise a 400 error is returned. When `redact_pii_audio` is enabled, matched terms are also redacted in the audio output. You can provide up to 100 labels, each with up to 200 terms of at most 200 characters; a label may contain only letters, numbers, spaces, underscores, and hyphens (max 80 characters). See [Static Entity Redaction](https://www.assemblyai.com/docs/guardrails/redact-pii-from-transcripts#static-entity-redaction) for more details.
    """

    sentiment_analysis: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Sentiment Analysis](https://www.assemblyai.com/docs/speech-understanding/sentiment-analysis), can be true or false. Requires `punctuate` to be `true`.
    """

    speaker_labels: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers), can be true or false. Requires `punctuate` to be `true`.
    """

    speaker_options: typing.Optional[TranscriptOptionalParamsSpeakerOptions] = pydantic.Field(default=None)
    """
    Specify options for [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-a-range-of-possible-speakers). Use this to set a range of possible speakers. Requires `speaker_labels` to be `true`, and cannot be used together with `speakers_expected`. When both bounds are set, `min_speakers_expected` must be less than or equal to `max_speakers_expected`.
    """

    speakers_expected: typing.Optional[int] = pydantic.Field(default=None)
    """
    Tells the speaker label model how many speakers it should attempt to identify. Requires `speaker_labels` to be `true` and must be a positive integer; cannot be used together with `speaker_options`. See [Set number of speakers expected](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-number-of-speakers-expected) for more details.
    """

    speech_models: typing.Optional[typing.List[SpeechModel]] = pydantic.Field(default=None)
    """
    Optional. Supported values: `universal-3-5-pro`, `universal-2`. If omitted, defaults to `["universal-3-5-pro", "universal-2"]`. See [Model Selection](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model) for available models and routing behavior.
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
    Enable [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization), can be true or false. Requires both `punctuate` and `format_text` to be `true`, and cannot be enabled together with `auto_chapters`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    
    Note: This parameter is only supported for the Universal-2 model.
    """

    summary_model: typing.Optional[SummaryModel] = pydantic.Field(default=None)
    """
    The model to summarize the transcript. Must be set together with `summary_type`. Compatibility - `catchy` supports `gist` and `headline`; `informative` and `conversational` support `headline`, `paragraph`, `bullets`, and `bullets_verbose`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    """

    summary_type: typing.Optional[SummaryType] = pydantic.Field(default=None)
    """
    The type of summary. Must be set together with `summary_model`; see `summary_model` for the supported model and type combinations. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.
    """

    remove_audio_tags: typing.Optional[TranscriptOptionalParamsRemoveAudioTags] = pydantic.Field(default=None)
    """
    Universal-3.5 Pro generates rich transcripts that can include inline annotations such as audio event markers and speaker cues. Set to `"all"` to remove all inline annotations, or `"speaker"` to remove only speaker cues while keeping other annotations. By default, all inline annotations are removed.
    
    Note: This parameter is only supported for the Universal-3.5 Pro model.
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    Control the amount of randomness injected into the model's response. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for more details.
    
    Note: This parameter only takes effect on the Universal-3.5 Pro model.
    """

    webhook_auth_header_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The header name to be sent with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests. Must be 1-1000 characters and contain only ASCII letters, numbers, hyphens, and underscores. Requires `webhook_auth_header_value` and `webhook_url` to also be set.
    """

    webhook_auth_header_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The header value to send back with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests for added security. Must be 1-1000 characters and must not contain carriage returns or newlines. Requires `webhook_auth_header_name` and `webhook_url` to also be set.
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
