

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTranscriptsClient, RawTranscriptsClient
from .types.paragraphs_response import ParagraphsResponse
from .types.pii_policy import PiiPolicy
from .types.redact_pii_audio_quality import RedactPiiAudioQuality
from .types.redacted_audio_response import RedactedAudioResponse
from .types.sentences_response import SentencesResponse
from .types.speech_model import SpeechModel
from .types.substitution_policy import SubstitutionPolicy
from .types.subtitle_format import SubtitleFormat
from .types.summary_model import SummaryModel
from .types.summary_type import SummaryType
from .types.transcript import Transcript
from .types.transcript_custom_spelling import TranscriptCustomSpelling
from .types.transcript_language_code import TranscriptLanguageCode
from .types.transcript_list import TranscriptList
from .types.transcript_optional_params_domain import TranscriptOptionalParamsDomain
from .types.transcript_optional_params_language_code import TranscriptOptionalParamsLanguageCode
from .types.transcript_optional_params_language_detection_options import (
    TranscriptOptionalParamsLanguageDetectionOptions,
)
from .types.transcript_optional_params_redact_pii_audio_options import TranscriptOptionalParamsRedactPiiAudioOptions
from .types.transcript_optional_params_remove_audio_tags import TranscriptOptionalParamsRemoveAudioTags
from .types.transcript_optional_params_speaker_options import TranscriptOptionalParamsSpeakerOptions
from .types.transcript_optional_params_speech_understanding import TranscriptOptionalParamsSpeechUnderstanding
from .types.transcript_status import TranscriptStatus
from .types.word_search_response import WordSearchResponse


OMIT = typing.cast(typing.Any, ...)


class TranscriptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTranscriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTranscriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTranscriptsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        status: typing.Optional[TranscriptStatus] = None,
        created_on: typing.Optional[dt.date] = None,
        before_id: typing.Optional[str] = None,
        after_id: typing.Optional[str] = None,
        throttled_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranscriptList:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Retrieve a list of transcripts you created.
        Transcripts are sorted from newest to oldest and can be retrieved for the last 90 days of usage. The previous URL always points to a page with older transcripts.

        If you need to retrieve transcripts from more than 90 days ago please reach out to our Support team at support@assemblyai.com.

        **Pagination**

        This endpoint returns paginated results. The response includes a `page_details` object with the following properties:
        - `page_details.limit` - Maximum number of transcripts per page.
        - `page_details.result_count` - Total number of transcripts returned on the current page.
        - `page_details.current_url` - URL to the current page.
        - `page_details.prev_url` - URL to the previous page of older transcripts.
        - `page_details.next_url` - URL to the next page of newer transcripts.

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum amount of transcripts to retrieve

        status : typing.Optional[TranscriptStatus]
            Filter by transcript status

        created_on : typing.Optional[dt.date]
            Only get transcripts created on this date

        before_id : typing.Optional[str]
            Get transcripts that were created before this transcript ID

        after_id : typing.Optional[str]
            Get transcripts that were created after this transcript ID

        throttled_only : typing.Optional[bool]
            Only get throttled transcripts, overrides the status filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptList
            A list of transcripts. Transcripts are sorted from newest to oldest. The previous URL always points to a page with older transcripts.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transcripts.list()
        """
        _response = self._raw_client.list(
            limit=limit,
            status=status,
            created_on=created_on,
            before_id=before_id,
            after_id=after_id,
            throttled_only=throttled_only,
            request_options=request_options,
        )
        return _response.data

    def submit(
        self,
        *,
        audio_url: str,
        audio_end_at: typing.Optional[int] = OMIT,
        audio_start_from: typing.Optional[int] = OMIT,
        auto_chapters: typing.Optional[bool] = OMIT,
        auto_highlights: typing.Optional[bool] = OMIT,
        content_safety: typing.Optional[bool] = OMIT,
        content_safety_confidence: typing.Optional[int] = OMIT,
        custom_spelling: typing.Optional[typing.Sequence[TranscriptCustomSpelling]] = OMIT,
        disfluencies: typing.Optional[bool] = OMIT,
        domain: typing.Optional[TranscriptOptionalParamsDomain] = OMIT,
        entity_detection: typing.Optional[bool] = OMIT,
        filter_profanity: typing.Optional[bool] = OMIT,
        format_text: typing.Optional[bool] = OMIT,
        iab_categories: typing.Optional[bool] = OMIT,
        keyterms_prompt: typing.Optional[typing.Sequence[str]] = OMIT,
        language_code: typing.Optional[TranscriptOptionalParamsLanguageCode] = OMIT,
        language_codes: typing.Optional[typing.Sequence[TranscriptLanguageCode]] = OMIT,
        language_confidence_threshold: typing.Optional[float] = OMIT,
        language_detection: typing.Optional[bool] = OMIT,
        language_detection_options: typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions] = OMIT,
        multichannel: typing.Optional[bool] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        punctuate: typing.Optional[bool] = OMIT,
        redact_pii: typing.Optional[bool] = OMIT,
        redact_pii_audio: typing.Optional[bool] = OMIT,
        redact_pii_audio_options: typing.Optional[TranscriptOptionalParamsRedactPiiAudioOptions] = OMIT,
        redact_pii_audio_quality: typing.Optional[RedactPiiAudioQuality] = OMIT,
        redact_pii_policies: typing.Optional[typing.Sequence[PiiPolicy]] = OMIT,
        redact_pii_sub: typing.Optional[SubstitutionPolicy] = OMIT,
        redact_pii_return_unredacted: typing.Optional[bool] = OMIT,
        redact_static_entities: typing.Optional[typing.Dict[str, typing.Sequence[str]]] = OMIT,
        sentiment_analysis: typing.Optional[bool] = OMIT,
        speaker_labels: typing.Optional[bool] = OMIT,
        speaker_options: typing.Optional[TranscriptOptionalParamsSpeakerOptions] = OMIT,
        speakers_expected: typing.Optional[int] = OMIT,
        speech_models: typing.Optional[typing.Sequence[SpeechModel]] = OMIT,
        speech_threshold: typing.Optional[float] = OMIT,
        speech_understanding: typing.Optional[TranscriptOptionalParamsSpeechUnderstanding] = OMIT,
        summarization: typing.Optional[bool] = OMIT,
        summary_model: typing.Optional[SummaryModel] = OMIT,
        summary_type: typing.Optional[SummaryType] = OMIT,
        remove_audio_tags: typing.Optional[TranscriptOptionalParamsRemoveAudioTags] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        webhook_auth_header_name: typing.Optional[str] = OMIT,
        webhook_auth_header_value: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        custom_topics: typing.Optional[bool] = OMIT,
        speech_model: typing.Optional[SpeechModel] = OMIT,
        topics: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Transcript:
        """
        <Note>To use our EU server for transcription, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Create a transcript from a media file that is accessible via a URL.

        Parameters
        ----------
        audio_url : str
            The URL of the audio or video file to transcribe.

        audio_end_at : typing.Optional[int]
            The point in time, in milliseconds, to stop transcribing in your media file. See [Set the start and end of the transcript](https://www.assemblyai.com/docs/pre-recorded-audio/set-the-start-and-end-of-the-transcript) for more details.

        audio_start_from : typing.Optional[int]
            The point in time, in milliseconds, to begin transcribing in your media file. See [Set the start and end of the transcript](https://www.assemblyai.com/docs/pre-recorded-audio/set-the-start-and-end-of-the-transcript) for more details.

        auto_chapters : typing.Optional[bool]
            Enable [Auto Chapters](https://www.assemblyai.com/docs/speech-understanding/auto-chapters), can be true or false. Requires `punctuate` to be `true`, and cannot be enabled together with `summarization`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible chapter summaries. See the [updated Auto Chapters page](https://www.assemblyai.com/docs/speech-understanding/auto-chapters) for details.

            Note: This parameter is only supported for the Universal-2 model.

        auto_highlights : typing.Optional[bool]
            Enable [Key Phrases](https://www.assemblyai.com/docs/speech-understanding/key-phrases), either true or false

        content_safety : typing.Optional[bool]
            Enable [Content Moderation](https://www.assemblyai.com/docs/content-moderation), can be true or false

        content_safety_confidence : typing.Optional[int]
            The confidence threshold for the [Content Moderation](https://www.assemblyai.com/docs/content-moderation) model. Values must be between 25 and 100. Requires `content_safety` to be enabled; otherwise it's ignored.

        custom_spelling : typing.Optional[typing.Sequence[TranscriptCustomSpelling]]
            Customize how words are spelled and formatted using to and from values. Each `to` value must be a single word, and each `from` phrase can contain at most 5 words. See [Custom Spelling](https://www.assemblyai.com/docs/pre-recorded-audio/correct-spelling-of-terms) for more details.

        disfluencies : typing.Optional[bool]
            Transcribe [Filler Words](https://www.assemblyai.com/docs/pre-recorded-audio/include-filler-words), like "umm", in your media file; can be true or false. Supported on Universal-3.5 Pro and Universal-2.

        domain : typing.Optional[TranscriptOptionalParamsDomain]
            Enable domain-specific transcription models to improve accuracy for specialized terminology. Set to `"medical-v1"` to enable [Medical Mode](https://www.assemblyai.com/docs/pre-recorded-audio/medical-mode) for improved accuracy of medical terms such as medications, procedures, conditions, and dosages.

            Supported languages: English (`en`), Spanish (`es`), German (`de`), French (`fr`). If `medical-v1` is used with an unsupported language, the parameter is ignored and a warning is returned.

        entity_detection : typing.Optional[bool]
            Enable [Entity Detection](https://www.assemblyai.com/docs/speech-understanding/entity-detection), can be true or false

        filter_profanity : typing.Optional[bool]
            Filter profanity from the transcribed text, can be true or false. See [Profanity Filtering](https://www.assemblyai.com/docs/profanity-filtering) for more details.

        format_text : typing.Optional[bool]
            Enable [Text Formatting](https://www.assemblyai.com/docs/pre-recorded-audio), can be true or false

        iab_categories : typing.Optional[bool]
            Enable [Topic Detection](https://www.assemblyai.com/docs/speech-understanding/topic-detection), can be true or false

        keyterms_prompt : typing.Optional[typing.Sequence[str]]
            Improve accuracy with up to 200 (for Universal-2) or 1000 (for Universal-3.5 Pro) domain-specific words or phrases (maximum 6 words per phrase). See [Keyterms Prompting](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro/prompting#keyterms-prompting) for more details.

        language_code : typing.Optional[TranscriptOptionalParamsLanguageCode]
            The language of your audio file. Possible values are found in [Supported Languages](https://www.assemblyai.com/docs/pre-recorded-audio/supported-languages).
            If you don't specify a language, it's detected automatically. Cannot be used together with `language_detection`.

        language_codes : typing.Optional[typing.Sequence[TranscriptLanguageCode]]
            The language codes of your audio file. Used for [Code switching](/speech-to-text/pre-recorded-audio/code-switching)
            One of the values specified must be `en`.

        language_confidence_threshold : typing.Optional[float]
            The confidence threshold for the automatically detected language.
            An error will be returned if the language confidence is below this threshold.
            Defaults to 0. Can only be set when `language_detection` is enabled. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.

        language_detection : typing.Optional[bool]
            [Automatic language detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) identifies the spoken language and routes the request to the best model. It's applied automatically when you don't specify a `language_code`. Set to `false` only together with a `language_code`; disabling it without specifying a language returns an error.

        language_detection_options : typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions]
            Specify options for [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection).

        multichannel : typing.Optional[bool]
            Enable [Multichannel](https://www.assemblyai.com/docs/pre-recorded-audio/transcribe-multiple-audio-channels) transcription, can be true or false.

        prompt : typing.Optional[str]
            Provide natural language prompting of up to 1,500 words of contextual information to the model. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for best practices.

            Note: This parameter is only supported for the Universal-3.5 Pro model.

        punctuate : typing.Optional[bool]
            Enable [Automatic Punctuation](https://www.assemblyai.com/docs/pre-recorded-audio), can be true or false

        redact_pii : typing.Optional[bool]
            Redact PII from the transcribed text using the Redact PII model, can be true or false. Requires `format_text` to be `true`. See [PII Redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.

        redact_pii_audio : typing.Optional[bool]
            Generate a copy of the original media file with spoken PII "beeped" out, can be true or false. Requires `redact_pii` to be `true`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more details.

        redact_pii_audio_options : typing.Optional[TranscriptOptionalParamsRedactPiiAudioOptions]
            Specify options for [PII redacted audio](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) files.

        redact_pii_audio_quality : typing.Optional[RedactPiiAudioQuality]
            Controls the filetype of the audio created by redact_pii_audio. Currently supports mp3 (default) and wav. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more details.

        redact_pii_policies : typing.Optional[typing.Sequence[PiiPolicy]]
            The list of PII Redaction policies to enable. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.

        redact_pii_sub : typing.Optional[SubstitutionPolicy]
            The replacement logic for detected PII, can be `entity_name` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.

        redact_pii_return_unredacted : typing.Optional[bool]
            When set to `true`, returns the original unredacted transcript alongside the redacted one in the same response. Requires `redact_pii` to be `true`, otherwise a 400 error is returned.

            When enabled, the response includes the additional fields `unredacted_text`, `unredacted_words`, and `unredacted_utterances`. The existing `text`, `words`, and `utterances` fields remain fully redacted. When disabled (default), the response is unchanged and contains only the redacted transcript. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.

        redact_static_entities : typing.Optional[typing.Dict[str, typing.Sequence[str]]]
            A map of user-defined terms to redact, where each key is a redaction label and each value is a list of exact terms to match (e.g. `{ "INTERNAL_TOOL": ["Bearclaw", "Cubclaw"] }`). Each matching term in the transcript is redacted using the `redact_pii_sub` substitution, on top of standard PII Redaction. Useful for redacting specific, predefined terms (proprietary names, internal codenames) that aren't general PII categories.

            This is a literal find-and-replace (tolerant of casing, surrounding punctuation, and minor spacing/hyphenation), not a model — it does not generalize beyond the terms you provide. Requires `redact_pii` to be `true`, otherwise a 400 error is returned. When `redact_pii_audio` is enabled, matched terms are also redacted in the audio output. You can provide up to 100 labels, each with up to 200 terms of at most 200 characters; a label may contain only letters, numbers, spaces, underscores, and hyphens (max 80 characters). See [Static Entity Redaction](https://www.assemblyai.com/docs/guardrails/redact-pii-from-transcripts#static-entity-redaction) for more details.

        sentiment_analysis : typing.Optional[bool]
            Enable [Sentiment Analysis](https://www.assemblyai.com/docs/speech-understanding/sentiment-analysis), can be true or false. Requires `punctuate` to be `true`.

        speaker_labels : typing.Optional[bool]
            Enable [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers), can be true or false. Requires `punctuate` to be `true`.

        speaker_options : typing.Optional[TranscriptOptionalParamsSpeakerOptions]
            Specify options for [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-a-range-of-possible-speakers). Use this to set a range of possible speakers. Requires `speaker_labels` to be `true`, and cannot be used together with `speakers_expected`. When both bounds are set, `min_speakers_expected` must be less than or equal to `max_speakers_expected`.

        speakers_expected : typing.Optional[int]
            Tells the speaker label model how many speakers it should attempt to identify. Requires `speaker_labels` to be `true` and must be a positive integer; cannot be used together with `speaker_options`. See [Set number of speakers expected](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-number-of-speakers-expected) for more details.

        speech_models : typing.Optional[typing.Sequence[SpeechModel]]
            Optional. Supported values: `universal-3-5-pro`, `universal-2`. If omitted, defaults to `["universal-3-5-pro", "universal-2"]`. See [Model Selection](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model) for available models and routing behavior.

        speech_threshold : typing.Optional[float]
            Reject audio files that contain less than this fraction of speech.
            Valid values are in the range [0, 1] inclusive. See [Speech Threshold](https://www.assemblyai.com/docs/speech-threshold) for more details.

        speech_understanding : typing.Optional[TranscriptOptionalParamsSpeechUnderstanding]
            Enable speech understanding tasks like [Translation](https://www.assemblyai.com/docs/speech-understanding/translation), [Speaker Identification](https://www.assemblyai.com/docs/speech-understanding/speaker-identification), and [Custom Formatting](https://www.assemblyai.com/docs/speech-understanding/custom-formatting). See the task-specific docs for available options and configuration.

        summarization : typing.Optional[bool]
            Enable [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization), can be true or false. Requires both `punctuate` and `format_text` to be `true`, and cannot be enabled together with `auto_chapters`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.

            Note: This parameter is only supported for the Universal-2 model.

        summary_model : typing.Optional[SummaryModel]
            The model to summarize the transcript. Must be set together with `summary_type`. Compatibility - `catchy` supports `gist` and `headline`; `informative` and `conversational` support `headline`, `paragraph`, `bullets`, and `bullets_verbose`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.

        summary_type : typing.Optional[SummaryType]
            The type of summary. Must be set together with `summary_model`; see `summary_model` for the supported model and type combinations. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.

        remove_audio_tags : typing.Optional[TranscriptOptionalParamsRemoveAudioTags]
            Universal-3.5 Pro generates rich transcripts that can include inline annotations such as audio event markers and speaker cues. Set to `"all"` to remove all inline annotations, or `"speaker"` to remove only speaker cues while keeping other annotations. By default, all inline annotations are removed.

            Note: This parameter is only supported for the Universal-3.5 Pro model.

        temperature : typing.Optional[float]
            Control the amount of randomness injected into the model's response. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for more details.

            Note: This parameter only takes effect on the Universal-3.5 Pro model.

        webhook_auth_header_name : typing.Optional[str]
            The header name to be sent with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests. Must be 1-1000 characters and contain only ASCII letters, numbers, hyphens, and underscores. Requires `webhook_auth_header_value` and `webhook_url` to also be set.

        webhook_auth_header_value : typing.Optional[str]
            The header value to send back with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests for added security. Must be 1-1000 characters and must not contain carriage returns or newlines. Requires `webhook_auth_header_name` and `webhook_url` to also be set.

        webhook_url : typing.Optional[str]
            The URL to which we send [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests.

        custom_topics : typing.Optional[bool]
            This parameter does not currently have any functionality attached to it.

        speech_model : typing.Optional[SpeechModel]
            This parameter has been replaced with the `speech_models` parameter, learn more about the `speech_models` parameter [here](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model).

        topics : typing.Optional[typing.Sequence[str]]
            This parameter does not currently have any functionality attached to it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Transcript
            Transcript created and queued for processing

        Examples
        --------
        from fern.transcripts import (
            TranscriptCustomSpelling,
            TranscriptOptionalParamsSpeechUnderstanding,
        )

        from fern import (
            FernApi,
            TranslationRequestBody,
            TranslationRequestBodyTranslation,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transcripts.submit(
            audio_end_at=280,
            audio_start_from=10,
            auto_highlights=True,
            content_safety=True,
            custom_spelling=[
                TranscriptCustomSpelling(
                    from_=["dicarlo"],
                    to="Decarlo",
                )
            ],
            disfluencies=False,
            entity_detection=True,
            filter_profanity=True,
            format_text=True,
            iab_categories=True,
            language_confidence_threshold=0.7,
            language_detection=True,
            multichannel=True,
            punctuate=True,
            redact_pii=True,
            redact_pii_audio=True,
            redact_pii_audio_quality="mp3",
            redact_pii_policies=["us_social_security_number", "credit_card_number"],
            redact_pii_sub="hash",
            sentiment_analysis=True,
            speaker_labels=True,
            speakers_expected=2,
            speech_threshold=0.5,
            speech_understanding=TranscriptOptionalParamsSpeechUnderstanding(
                request=TranslationRequestBody(
                    translation=TranslationRequestBodyTranslation(
                        target_languages=["es", "de"],
                        formal=True,
                        match_original_utterance=True,
                    ),
                ),
            ),
            webhook_auth_header_name="webhook-secret",
            webhook_auth_header_value="webhook-secret-value",
            webhook_url="https://your-webhook-url/path",
            audio_url="https://assembly.ai/wildfires.mp3",
        )
        """
        _response = self._raw_client.submit(
            audio_url=audio_url,
            audio_end_at=audio_end_at,
            audio_start_from=audio_start_from,
            auto_chapters=auto_chapters,
            auto_highlights=auto_highlights,
            content_safety=content_safety,
            content_safety_confidence=content_safety_confidence,
            custom_spelling=custom_spelling,
            disfluencies=disfluencies,
            domain=domain,
            entity_detection=entity_detection,
            filter_profanity=filter_profanity,
            format_text=format_text,
            iab_categories=iab_categories,
            keyterms_prompt=keyterms_prompt,
            language_code=language_code,
            language_codes=language_codes,
            language_confidence_threshold=language_confidence_threshold,
            language_detection=language_detection,
            language_detection_options=language_detection_options,
            multichannel=multichannel,
            prompt=prompt,
            punctuate=punctuate,
            redact_pii=redact_pii,
            redact_pii_audio=redact_pii_audio,
            redact_pii_audio_options=redact_pii_audio_options,
            redact_pii_audio_quality=redact_pii_audio_quality,
            redact_pii_policies=redact_pii_policies,
            redact_pii_sub=redact_pii_sub,
            redact_pii_return_unredacted=redact_pii_return_unredacted,
            redact_static_entities=redact_static_entities,
            sentiment_analysis=sentiment_analysis,
            speaker_labels=speaker_labels,
            speaker_options=speaker_options,
            speakers_expected=speakers_expected,
            speech_models=speech_models,
            speech_threshold=speech_threshold,
            speech_understanding=speech_understanding,
            summarization=summarization,
            summary_model=summary_model,
            summary_type=summary_type,
            remove_audio_tags=remove_audio_tags,
            temperature=temperature,
            webhook_auth_header_name=webhook_auth_header_name,
            webhook_auth_header_value=webhook_auth_header_value,
            webhook_url=webhook_url,
            custom_topics=custom_topics,
            speech_model=speech_model,
            topics=topics,
            request_options=request_options,
        )
        return _response.data

    def get(self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Transcript:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Get the transcript resource. The transcript is ready when the "status" is "completed".

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Transcript
            The transcript resource

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transcripts.get(
            transcript_id="transcript_id",
        )
        """
        _response = self._raw_client.get(transcript_id, request_options=request_options)
        return _response.data

    def delete(self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Transcript:
        """
        <Note>To delete your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Remove the data from the transcript and mark it as deleted.
        <Warning>Files uploaded via the `/upload` endpoint are immediately deleted alongside the transcript when you make a DELETE request, ensuring your data is removed from our systems right away.</Warning>

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Transcript
            The deleted transcript response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transcripts.delete(
            transcript_id="transcript_id",
        )
        """
        _response = self._raw_client.delete(transcript_id, request_options=request_options)
        return _response.data

    def get_subtitles(
        self,
        transcript_id: str,
        subtitle_format: SubtitleFormat,
        *,
        chars_per_caption: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Export your transcript in SRT or VTT format to use with a video player for subtitles and closed captions.

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        subtitle_format : SubtitleFormat
            The format of the captions

        chars_per_caption : typing.Optional[int]
            The maximum number of characters per caption

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The exported captions as text

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transcripts.get_subtitles(
            transcript_id="transcript_id",
            subtitle_format="srt",
        )
        """
        _response = self._raw_client.get_subtitles(
            transcript_id, subtitle_format, chars_per_caption=chars_per_caption, request_options=request_options
        )
        return _response.data

    def get_sentences(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SentencesResponse:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Get the transcript split by sentences. The API will attempt to semantically segment the transcript into sentences to create more reader-friendly transcripts.

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SentencesResponse
            Exported sentences

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transcripts.get_sentences(
            transcript_id="transcript_id",
        )
        """
        _response = self._raw_client.get_sentences(transcript_id, request_options=request_options)
        return _response.data

    def get_paragraphs(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ParagraphsResponse:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Get the transcript split by paragraphs. The API will attempt to semantically segment your transcript into paragraphs to create more reader-friendly transcripts.

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParagraphsResponse
            Exported paragraphs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transcripts.get_paragraphs(
            transcript_id="transcript_id",
        )
        """
        _response = self._raw_client.get_paragraphs(transcript_id, request_options=request_options)
        return _response.data

    def word_search(
        self,
        transcript_id: str,
        *,
        words: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WordSearchResponse:
        """
        <Note>To search through a transcription created on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Search through the transcript for keywords. You can search for individual words, numbers, or phrases containing up to five words or numbers.

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        words : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Keywords to search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WordSearchResponse
            Word search response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transcripts.word_search(
            transcript_id="transcript_id",
            words=["words"],
        )
        """
        _response = self._raw_client.word_search(transcript_id, words=words, request_options=request_options)
        return _response.data

    def get_redacted_audio(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RedactedAudioResponse:
        """
        <Note>To retrieve the redacted audio on the EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com` in the `GET` request above.</Note>
        <Note>Redacted audio files are only available for 24 hours. Make sure to download the file within this time frame.</Note>
        Retrieve the redacted audio object containing the status and URL to the redacted audio.

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedactedAudioResponse
            The redacted audio object containing the status and URL to the redacted audio

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.transcripts.get_redacted_audio(
            transcript_id="transcript_id",
        )
        """
        _response = self._raw_client.get_redacted_audio(transcript_id, request_options=request_options)
        return _response.data


class AsyncTranscriptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTranscriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTranscriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTranscriptsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        status: typing.Optional[TranscriptStatus] = None,
        created_on: typing.Optional[dt.date] = None,
        before_id: typing.Optional[str] = None,
        after_id: typing.Optional[str] = None,
        throttled_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranscriptList:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Retrieve a list of transcripts you created.
        Transcripts are sorted from newest to oldest and can be retrieved for the last 90 days of usage. The previous URL always points to a page with older transcripts.

        If you need to retrieve transcripts from more than 90 days ago please reach out to our Support team at support@assemblyai.com.

        **Pagination**

        This endpoint returns paginated results. The response includes a `page_details` object with the following properties:
        - `page_details.limit` - Maximum number of transcripts per page.
        - `page_details.result_count` - Total number of transcripts returned on the current page.
        - `page_details.current_url` - URL to the current page.
        - `page_details.prev_url` - URL to the previous page of older transcripts.
        - `page_details.next_url` - URL to the next page of newer transcripts.

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum amount of transcripts to retrieve

        status : typing.Optional[TranscriptStatus]
            Filter by transcript status

        created_on : typing.Optional[dt.date]
            Only get transcripts created on this date

        before_id : typing.Optional[str]
            Get transcripts that were created before this transcript ID

        after_id : typing.Optional[str]
            Get transcripts that were created after this transcript ID

        throttled_only : typing.Optional[bool]
            Only get throttled transcripts, overrides the status filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptList
            A list of transcripts. Transcripts are sorted from newest to oldest. The previous URL always points to a page with older transcripts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcripts.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            limit=limit,
            status=status,
            created_on=created_on,
            before_id=before_id,
            after_id=after_id,
            throttled_only=throttled_only,
            request_options=request_options,
        )
        return _response.data

    async def submit(
        self,
        *,
        audio_url: str,
        audio_end_at: typing.Optional[int] = OMIT,
        audio_start_from: typing.Optional[int] = OMIT,
        auto_chapters: typing.Optional[bool] = OMIT,
        auto_highlights: typing.Optional[bool] = OMIT,
        content_safety: typing.Optional[bool] = OMIT,
        content_safety_confidence: typing.Optional[int] = OMIT,
        custom_spelling: typing.Optional[typing.Sequence[TranscriptCustomSpelling]] = OMIT,
        disfluencies: typing.Optional[bool] = OMIT,
        domain: typing.Optional[TranscriptOptionalParamsDomain] = OMIT,
        entity_detection: typing.Optional[bool] = OMIT,
        filter_profanity: typing.Optional[bool] = OMIT,
        format_text: typing.Optional[bool] = OMIT,
        iab_categories: typing.Optional[bool] = OMIT,
        keyterms_prompt: typing.Optional[typing.Sequence[str]] = OMIT,
        language_code: typing.Optional[TranscriptOptionalParamsLanguageCode] = OMIT,
        language_codes: typing.Optional[typing.Sequence[TranscriptLanguageCode]] = OMIT,
        language_confidence_threshold: typing.Optional[float] = OMIT,
        language_detection: typing.Optional[bool] = OMIT,
        language_detection_options: typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions] = OMIT,
        multichannel: typing.Optional[bool] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        punctuate: typing.Optional[bool] = OMIT,
        redact_pii: typing.Optional[bool] = OMIT,
        redact_pii_audio: typing.Optional[bool] = OMIT,
        redact_pii_audio_options: typing.Optional[TranscriptOptionalParamsRedactPiiAudioOptions] = OMIT,
        redact_pii_audio_quality: typing.Optional[RedactPiiAudioQuality] = OMIT,
        redact_pii_policies: typing.Optional[typing.Sequence[PiiPolicy]] = OMIT,
        redact_pii_sub: typing.Optional[SubstitutionPolicy] = OMIT,
        redact_pii_return_unredacted: typing.Optional[bool] = OMIT,
        redact_static_entities: typing.Optional[typing.Dict[str, typing.Sequence[str]]] = OMIT,
        sentiment_analysis: typing.Optional[bool] = OMIT,
        speaker_labels: typing.Optional[bool] = OMIT,
        speaker_options: typing.Optional[TranscriptOptionalParamsSpeakerOptions] = OMIT,
        speakers_expected: typing.Optional[int] = OMIT,
        speech_models: typing.Optional[typing.Sequence[SpeechModel]] = OMIT,
        speech_threshold: typing.Optional[float] = OMIT,
        speech_understanding: typing.Optional[TranscriptOptionalParamsSpeechUnderstanding] = OMIT,
        summarization: typing.Optional[bool] = OMIT,
        summary_model: typing.Optional[SummaryModel] = OMIT,
        summary_type: typing.Optional[SummaryType] = OMIT,
        remove_audio_tags: typing.Optional[TranscriptOptionalParamsRemoveAudioTags] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        webhook_auth_header_name: typing.Optional[str] = OMIT,
        webhook_auth_header_value: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        custom_topics: typing.Optional[bool] = OMIT,
        speech_model: typing.Optional[SpeechModel] = OMIT,
        topics: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Transcript:
        """
        <Note>To use our EU server for transcription, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Create a transcript from a media file that is accessible via a URL.

        Parameters
        ----------
        audio_url : str
            The URL of the audio or video file to transcribe.

        audio_end_at : typing.Optional[int]
            The point in time, in milliseconds, to stop transcribing in your media file. See [Set the start and end of the transcript](https://www.assemblyai.com/docs/pre-recorded-audio/set-the-start-and-end-of-the-transcript) for more details.

        audio_start_from : typing.Optional[int]
            The point in time, in milliseconds, to begin transcribing in your media file. See [Set the start and end of the transcript](https://www.assemblyai.com/docs/pre-recorded-audio/set-the-start-and-end-of-the-transcript) for more details.

        auto_chapters : typing.Optional[bool]
            Enable [Auto Chapters](https://www.assemblyai.com/docs/speech-understanding/auto-chapters), can be true or false. Requires `punctuate` to be `true`, and cannot be enabled together with `summarization`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible chapter summaries. See the [updated Auto Chapters page](https://www.assemblyai.com/docs/speech-understanding/auto-chapters) for details.

            Note: This parameter is only supported for the Universal-2 model.

        auto_highlights : typing.Optional[bool]
            Enable [Key Phrases](https://www.assemblyai.com/docs/speech-understanding/key-phrases), either true or false

        content_safety : typing.Optional[bool]
            Enable [Content Moderation](https://www.assemblyai.com/docs/content-moderation), can be true or false

        content_safety_confidence : typing.Optional[int]
            The confidence threshold for the [Content Moderation](https://www.assemblyai.com/docs/content-moderation) model. Values must be between 25 and 100. Requires `content_safety` to be enabled; otherwise it's ignored.

        custom_spelling : typing.Optional[typing.Sequence[TranscriptCustomSpelling]]
            Customize how words are spelled and formatted using to and from values. Each `to` value must be a single word, and each `from` phrase can contain at most 5 words. See [Custom Spelling](https://www.assemblyai.com/docs/pre-recorded-audio/correct-spelling-of-terms) for more details.

        disfluencies : typing.Optional[bool]
            Transcribe [Filler Words](https://www.assemblyai.com/docs/pre-recorded-audio/include-filler-words), like "umm", in your media file; can be true or false. Supported on Universal-3.5 Pro and Universal-2.

        domain : typing.Optional[TranscriptOptionalParamsDomain]
            Enable domain-specific transcription models to improve accuracy for specialized terminology. Set to `"medical-v1"` to enable [Medical Mode](https://www.assemblyai.com/docs/pre-recorded-audio/medical-mode) for improved accuracy of medical terms such as medications, procedures, conditions, and dosages.

            Supported languages: English (`en`), Spanish (`es`), German (`de`), French (`fr`). If `medical-v1` is used with an unsupported language, the parameter is ignored and a warning is returned.

        entity_detection : typing.Optional[bool]
            Enable [Entity Detection](https://www.assemblyai.com/docs/speech-understanding/entity-detection), can be true or false

        filter_profanity : typing.Optional[bool]
            Filter profanity from the transcribed text, can be true or false. See [Profanity Filtering](https://www.assemblyai.com/docs/profanity-filtering) for more details.

        format_text : typing.Optional[bool]
            Enable [Text Formatting](https://www.assemblyai.com/docs/pre-recorded-audio), can be true or false

        iab_categories : typing.Optional[bool]
            Enable [Topic Detection](https://www.assemblyai.com/docs/speech-understanding/topic-detection), can be true or false

        keyterms_prompt : typing.Optional[typing.Sequence[str]]
            Improve accuracy with up to 200 (for Universal-2) or 1000 (for Universal-3.5 Pro) domain-specific words or phrases (maximum 6 words per phrase). See [Keyterms Prompting](https://www.assemblyai.com/docs/pre-recorded-audio/universal-3-5-pro/prompting#keyterms-prompting) for more details.

        language_code : typing.Optional[TranscriptOptionalParamsLanguageCode]
            The language of your audio file. Possible values are found in [Supported Languages](https://www.assemblyai.com/docs/pre-recorded-audio/supported-languages).
            If you don't specify a language, it's detected automatically. Cannot be used together with `language_detection`.

        language_codes : typing.Optional[typing.Sequence[TranscriptLanguageCode]]
            The language codes of your audio file. Used for [Code switching](/speech-to-text/pre-recorded-audio/code-switching)
            One of the values specified must be `en`.

        language_confidence_threshold : typing.Optional[float]
            The confidence threshold for the automatically detected language.
            An error will be returned if the language confidence is below this threshold.
            Defaults to 0. Can only be set when `language_detection` is enabled. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.

        language_detection : typing.Optional[bool]
            [Automatic language detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) identifies the spoken language and routes the request to the best model. It's applied automatically when you don't specify a `language_code`. Set to `false` only together with a `language_code`; disabling it without specifying a language returns an error.

        language_detection_options : typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions]
            Specify options for [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection).

        multichannel : typing.Optional[bool]
            Enable [Multichannel](https://www.assemblyai.com/docs/pre-recorded-audio/transcribe-multiple-audio-channels) transcription, can be true or false.

        prompt : typing.Optional[str]
            Provide natural language prompting of up to 1,500 words of contextual information to the model. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for best practices.

            Note: This parameter is only supported for the Universal-3.5 Pro model.

        punctuate : typing.Optional[bool]
            Enable [Automatic Punctuation](https://www.assemblyai.com/docs/pre-recorded-audio), can be true or false

        redact_pii : typing.Optional[bool]
            Redact PII from the transcribed text using the Redact PII model, can be true or false. Requires `format_text` to be `true`. See [PII Redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.

        redact_pii_audio : typing.Optional[bool]
            Generate a copy of the original media file with spoken PII "beeped" out, can be true or false. Requires `redact_pii` to be `true`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more details.

        redact_pii_audio_options : typing.Optional[TranscriptOptionalParamsRedactPiiAudioOptions]
            Specify options for [PII redacted audio](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) files.

        redact_pii_audio_quality : typing.Optional[RedactPiiAudioQuality]
            Controls the filetype of the audio created by redact_pii_audio. Currently supports mp3 (default) and wav. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction#request-for-redacted-audio) for more details.

        redact_pii_policies : typing.Optional[typing.Sequence[PiiPolicy]]
            The list of PII Redaction policies to enable. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.

        redact_pii_sub : typing.Optional[SubstitutionPolicy]
            The replacement logic for detected PII, can be `entity_name` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.

        redact_pii_return_unredacted : typing.Optional[bool]
            When set to `true`, returns the original unredacted transcript alongside the redacted one in the same response. Requires `redact_pii` to be `true`, otherwise a 400 error is returned.

            When enabled, the response includes the additional fields `unredacted_text`, `unredacted_words`, and `unredacted_utterances`. The existing `text`, `words`, and `utterances` fields remain fully redacted. When disabled (default), the response is unchanged and contains only the redacted transcript. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.

        redact_static_entities : typing.Optional[typing.Dict[str, typing.Sequence[str]]]
            A map of user-defined terms to redact, where each key is a redaction label and each value is a list of exact terms to match (e.g. `{ "INTERNAL_TOOL": ["Bearclaw", "Cubclaw"] }`). Each matching term in the transcript is redacted using the `redact_pii_sub` substitution, on top of standard PII Redaction. Useful for redacting specific, predefined terms (proprietary names, internal codenames) that aren't general PII categories.

            This is a literal find-and-replace (tolerant of casing, surrounding punctuation, and minor spacing/hyphenation), not a model — it does not generalize beyond the terms you provide. Requires `redact_pii` to be `true`, otherwise a 400 error is returned. When `redact_pii_audio` is enabled, matched terms are also redacted in the audio output. You can provide up to 100 labels, each with up to 200 terms of at most 200 characters; a label may contain only letters, numbers, spaces, underscores, and hyphens (max 80 characters). See [Static Entity Redaction](https://www.assemblyai.com/docs/guardrails/redact-pii-from-transcripts#static-entity-redaction) for more details.

        sentiment_analysis : typing.Optional[bool]
            Enable [Sentiment Analysis](https://www.assemblyai.com/docs/speech-understanding/sentiment-analysis), can be true or false. Requires `punctuate` to be `true`.

        speaker_labels : typing.Optional[bool]
            Enable [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers), can be true or false. Requires `punctuate` to be `true`.

        speaker_options : typing.Optional[TranscriptOptionalParamsSpeakerOptions]
            Specify options for [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-a-range-of-possible-speakers). Use this to set a range of possible speakers. Requires `speaker_labels` to be `true`, and cannot be used together with `speakers_expected`. When both bounds are set, `min_speakers_expected` must be less than or equal to `max_speakers_expected`.

        speakers_expected : typing.Optional[int]
            Tells the speaker label model how many speakers it should attempt to identify. Requires `speaker_labels` to be `true` and must be a positive integer; cannot be used together with `speaker_options`. See [Set number of speakers expected](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-number-of-speakers-expected) for more details.

        speech_models : typing.Optional[typing.Sequence[SpeechModel]]
            Optional. Supported values: `universal-3-5-pro`, `universal-2`. If omitted, defaults to `["universal-3-5-pro", "universal-2"]`. See [Model Selection](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model) for available models and routing behavior.

        speech_threshold : typing.Optional[float]
            Reject audio files that contain less than this fraction of speech.
            Valid values are in the range [0, 1] inclusive. See [Speech Threshold](https://www.assemblyai.com/docs/speech-threshold) for more details.

        speech_understanding : typing.Optional[TranscriptOptionalParamsSpeechUnderstanding]
            Enable speech understanding tasks like [Translation](https://www.assemblyai.com/docs/speech-understanding/translation), [Speaker Identification](https://www.assemblyai.com/docs/speech-understanding/speaker-identification), and [Custom Formatting](https://www.assemblyai.com/docs/speech-understanding/custom-formatting). See the task-specific docs for available options and configuration.

        summarization : typing.Optional[bool]
            Enable [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization), can be true or false. Requires both `punctuate` and `format_text` to be `true`, and cannot be enabled together with `auto_chapters`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.

            Note: This parameter is only supported for the Universal-2 model.

        summary_model : typing.Optional[SummaryModel]
            The model to summarize the transcript. Must be set together with `summary_type`. Compatibility - `catchy` supports `gist` and `headline`; `informative` and `conversational` support `headline`, `paragraph`, `bullets`, and `bullets_verbose`. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.

        summary_type : typing.Optional[SummaryType]
            The type of summary. Must be set together with `summary_model`; see `summary_model` for the supported model and type combinations. Deprecated - use [LLM Gateway](https://www.assemblyai.com/docs/llm-gateway/quickstart) instead for more flexible summaries. See the [updated Summarization page](https://www.assemblyai.com/docs/speech-understanding/summarization) for details.

        remove_audio_tags : typing.Optional[TranscriptOptionalParamsRemoveAudioTags]
            Universal-3.5 Pro generates rich transcripts that can include inline annotations such as audio event markers and speaker cues. Set to `"all"` to remove all inline annotations, or `"speaker"` to remove only speaker cues while keeping other annotations. By default, all inline annotations are removed.

            Note: This parameter is only supported for the Universal-3.5 Pro model.

        temperature : typing.Optional[float]
            Control the amount of randomness injected into the model's response. See the [Prompting Guide](https://www.assemblyai.com/docs/pre-recorded-audio/prompting) for more details.

            Note: This parameter only takes effect on the Universal-3.5 Pro model.

        webhook_auth_header_name : typing.Optional[str]
            The header name to be sent with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests. Must be 1-1000 characters and contain only ASCII letters, numbers, hyphens, and underscores. Requires `webhook_auth_header_value` and `webhook_url` to also be set.

        webhook_auth_header_value : typing.Optional[str]
            The header value to send back with the transcript completed or failed [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests for added security. Must be 1-1000 characters and must not contain carriage returns or newlines. Requires `webhook_auth_header_name` and `webhook_url` to also be set.

        webhook_url : typing.Optional[str]
            The URL to which we send [webhook](https://www.assemblyai.com/docs/deployment/webhooks-for-pre-recorded-audio) requests.

        custom_topics : typing.Optional[bool]
            This parameter does not currently have any functionality attached to it.

        speech_model : typing.Optional[SpeechModel]
            This parameter has been replaced with the `speech_models` parameter, learn more about the `speech_models` parameter [here](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model).

        topics : typing.Optional[typing.Sequence[str]]
            This parameter does not currently have any functionality attached to it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Transcript
            Transcript created and queued for processing

        Examples
        --------
        import asyncio

        from fern.transcripts import (
            TranscriptCustomSpelling,
            TranscriptOptionalParamsSpeechUnderstanding,
        )

        from fern import (
            AsyncFernApi,
            TranslationRequestBody,
            TranslationRequestBodyTranslation,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcripts.submit(
                audio_end_at=280,
                audio_start_from=10,
                auto_highlights=True,
                content_safety=True,
                custom_spelling=[
                    TranscriptCustomSpelling(
                        from_=["dicarlo"],
                        to="Decarlo",
                    )
                ],
                disfluencies=False,
                entity_detection=True,
                filter_profanity=True,
                format_text=True,
                iab_categories=True,
                language_confidence_threshold=0.7,
                language_detection=True,
                multichannel=True,
                punctuate=True,
                redact_pii=True,
                redact_pii_audio=True,
                redact_pii_audio_quality="mp3",
                redact_pii_policies=["us_social_security_number", "credit_card_number"],
                redact_pii_sub="hash",
                sentiment_analysis=True,
                speaker_labels=True,
                speakers_expected=2,
                speech_threshold=0.5,
                speech_understanding=TranscriptOptionalParamsSpeechUnderstanding(
                    request=TranslationRequestBody(
                        translation=TranslationRequestBodyTranslation(
                            target_languages=["es", "de"],
                            formal=True,
                            match_original_utterance=True,
                        ),
                    ),
                ),
                webhook_auth_header_name="webhook-secret",
                webhook_auth_header_value="webhook-secret-value",
                webhook_url="https://your-webhook-url/path",
                audio_url="https://assembly.ai/wildfires.mp3",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit(
            audio_url=audio_url,
            audio_end_at=audio_end_at,
            audio_start_from=audio_start_from,
            auto_chapters=auto_chapters,
            auto_highlights=auto_highlights,
            content_safety=content_safety,
            content_safety_confidence=content_safety_confidence,
            custom_spelling=custom_spelling,
            disfluencies=disfluencies,
            domain=domain,
            entity_detection=entity_detection,
            filter_profanity=filter_profanity,
            format_text=format_text,
            iab_categories=iab_categories,
            keyterms_prompt=keyterms_prompt,
            language_code=language_code,
            language_codes=language_codes,
            language_confidence_threshold=language_confidence_threshold,
            language_detection=language_detection,
            language_detection_options=language_detection_options,
            multichannel=multichannel,
            prompt=prompt,
            punctuate=punctuate,
            redact_pii=redact_pii,
            redact_pii_audio=redact_pii_audio,
            redact_pii_audio_options=redact_pii_audio_options,
            redact_pii_audio_quality=redact_pii_audio_quality,
            redact_pii_policies=redact_pii_policies,
            redact_pii_sub=redact_pii_sub,
            redact_pii_return_unredacted=redact_pii_return_unredacted,
            redact_static_entities=redact_static_entities,
            sentiment_analysis=sentiment_analysis,
            speaker_labels=speaker_labels,
            speaker_options=speaker_options,
            speakers_expected=speakers_expected,
            speech_models=speech_models,
            speech_threshold=speech_threshold,
            speech_understanding=speech_understanding,
            summarization=summarization,
            summary_model=summary_model,
            summary_type=summary_type,
            remove_audio_tags=remove_audio_tags,
            temperature=temperature,
            webhook_auth_header_name=webhook_auth_header_name,
            webhook_auth_header_value=webhook_auth_header_value,
            webhook_url=webhook_url,
            custom_topics=custom_topics,
            speech_model=speech_model,
            topics=topics,
            request_options=request_options,
        )
        return _response.data

    async def get(self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Transcript:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Get the transcript resource. The transcript is ready when the "status" is "completed".

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Transcript
            The transcript resource

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcripts.get(
                transcript_id="transcript_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(transcript_id, request_options=request_options)
        return _response.data

    async def delete(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Transcript:
        """
        <Note>To delete your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Remove the data from the transcript and mark it as deleted.
        <Warning>Files uploaded via the `/upload` endpoint are immediately deleted alongside the transcript when you make a DELETE request, ensuring your data is removed from our systems right away.</Warning>

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Transcript
            The deleted transcript response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcripts.delete(
                transcript_id="transcript_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(transcript_id, request_options=request_options)
        return _response.data

    async def get_subtitles(
        self,
        transcript_id: str,
        subtitle_format: SubtitleFormat,
        *,
        chars_per_caption: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Export your transcript in SRT or VTT format to use with a video player for subtitles and closed captions.

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        subtitle_format : SubtitleFormat
            The format of the captions

        chars_per_caption : typing.Optional[int]
            The maximum number of characters per caption

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The exported captions as text

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcripts.get_subtitles(
                transcript_id="transcript_id",
                subtitle_format="srt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subtitles(
            transcript_id, subtitle_format, chars_per_caption=chars_per_caption, request_options=request_options
        )
        return _response.data

    async def get_sentences(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SentencesResponse:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Get the transcript split by sentences. The API will attempt to semantically segment the transcript into sentences to create more reader-friendly transcripts.

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SentencesResponse
            Exported sentences

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcripts.get_sentences(
                transcript_id="transcript_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sentences(transcript_id, request_options=request_options)
        return _response.data

    async def get_paragraphs(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ParagraphsResponse:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Get the transcript split by paragraphs. The API will attempt to semantically segment your transcript into paragraphs to create more reader-friendly transcripts.

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParagraphsResponse
            Exported paragraphs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcripts.get_paragraphs(
                transcript_id="transcript_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_paragraphs(transcript_id, request_options=request_options)
        return _response.data

    async def word_search(
        self,
        transcript_id: str,
        *,
        words: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WordSearchResponse:
        """
        <Note>To search through a transcription created on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Search through the transcript for keywords. You can search for individual words, numbers, or phrases containing up to five words or numbers.

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        words : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Keywords to search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WordSearchResponse
            Word search response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcripts.word_search(
                transcript_id="transcript_id",
                words=["words"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.word_search(transcript_id, words=words, request_options=request_options)
        return _response.data

    async def get_redacted_audio(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RedactedAudioResponse:
        """
        <Note>To retrieve the redacted audio on the EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com` in the `GET` request above.</Note>
        <Note>Redacted audio files are only available for 24 hours. Make sure to download the file within this time frame.</Note>
        Retrieve the redacted audio object containing the status and URL to the redacted audio.

        Parameters
        ----------
        transcript_id : str
            ID of the transcript

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedactedAudioResponse
            The redacted audio object containing the status and URL to the redacted audio

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcripts.get_redacted_audio(
                transcript_id="transcript_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_redacted_audio(transcript_id, request_options=request_options)
        return _response.data
