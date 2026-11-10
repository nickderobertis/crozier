

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.gateway_timeout_error import GatewayTimeoutError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error import Error
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
from .types.transcript_optional_params_language_code import TranscriptOptionalParamsLanguageCode
from .types.transcript_optional_params_language_detection_options import (
    TranscriptOptionalParamsLanguageDetectionOptions,
)
from .types.transcript_optional_params_redact_pii_audio_options import TranscriptOptionalParamsRedactPiiAudioOptions
from .types.transcript_optional_params_speaker_options import TranscriptOptionalParamsSpeakerOptions
from .types.transcript_optional_params_speech_understanding import TranscriptOptionalParamsSpeechUnderstanding
from .types.transcript_status import TranscriptStatus
from .types.word_search_response import WordSearchResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTranscriptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[TranscriptList]:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Retrieve a list of transcripts you created.
        Transcripts are sorted from newest to oldest and can be retrieved for the last 90 days of usage. The previous URL always points to a page with older transcripts.

        If you need to retrieve transcripts from more than 90 days ago please reach out to our Support team at support@assemblyai.com.

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
        HttpResponse[TranscriptList]
            A list of transcripts. Transcripts are sorted from newest to oldest. The previous URL always points to a page with older transcripts.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/transcript",
            method="GET",
            params={
                "limit": limit,
                "status": status,
                "created_on": str(created_on) if created_on is not None else None,
                "before_id": before_id,
                "after_id": after_id,
                "throttled_only": throttled_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TranscriptList,
                    parse_obj_as(
                        type_=TranscriptList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def submit(
        self,
        *,
        audio_url: str,
        speech_models: typing.Sequence[SpeechModel],
        audio_end_at: typing.Optional[int] = OMIT,
        audio_start_from: typing.Optional[int] = OMIT,
        auto_chapters: typing.Optional[bool] = OMIT,
        auto_highlights: typing.Optional[bool] = OMIT,
        content_safety: typing.Optional[bool] = OMIT,
        content_safety_confidence: typing.Optional[int] = OMIT,
        custom_spelling: typing.Optional[typing.Sequence[TranscriptCustomSpelling]] = OMIT,
        disfluencies: typing.Optional[bool] = OMIT,
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
        sentiment_analysis: typing.Optional[bool] = OMIT,
        speaker_labels: typing.Optional[bool] = OMIT,
        speaker_options: typing.Optional[TranscriptOptionalParamsSpeakerOptions] = OMIT,
        speakers_expected: typing.Optional[int] = OMIT,
        speech_threshold: typing.Optional[float] = OMIT,
        speech_understanding: typing.Optional[TranscriptOptionalParamsSpeechUnderstanding] = OMIT,
        summarization: typing.Optional[bool] = OMIT,
        summary_model: typing.Optional[SummaryModel] = OMIT,
        summary_type: typing.Optional[SummaryType] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        webhook_auth_header_name: typing.Optional[str] = OMIT,
        webhook_auth_header_value: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        custom_topics: typing.Optional[bool] = OMIT,
        speech_model: typing.Optional[SpeechModel] = OMIT,
        topics: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Transcript]:
        """
        <Note>To use our EU server for transcription, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Create a transcript from a media file that is accessible via a URL.

        Parameters
        ----------
        audio_url : str
            The URL of the audio or video file to transcribe.

        speech_models : typing.Sequence[SpeechModel]
            List multiple speech models in priority order, allowing our system to automatically route your audio to the best available option.

        audio_end_at : typing.Optional[int]
            The point in time, in milliseconds, to stop transcribing in your media file

        audio_start_from : typing.Optional[int]
            The point in time, in milliseconds, to begin transcribing in your media file

        auto_chapters : typing.Optional[bool]
            Enable [Auto Chapters](https://www.assemblyai.com/docs/models/auto-chapters), can be true or false

        auto_highlights : typing.Optional[bool]
            Enable Key Phrases, either true or false

        content_safety : typing.Optional[bool]
            Enable [Content Moderation](https://www.assemblyai.com/docs/models/content-moderation), can be true or false

        content_safety_confidence : typing.Optional[int]
            The confidence threshold for the Content Moderation model. Values must be between 25 and 100.

        custom_spelling : typing.Optional[typing.Sequence[TranscriptCustomSpelling]]
            Customize how words are spelled and formatted using to and from values

        disfluencies : typing.Optional[bool]
            Transcribe Filler Words, like "umm", in your media file; can be true or false

        entity_detection : typing.Optional[bool]
            Enable [Entity Detection](https://www.assemblyai.com/docs/models/entity-detection), can be true or false

        filter_profanity : typing.Optional[bool]
            Filter profanity from the transcribed text, can be true or false

        format_text : typing.Optional[bool]
            Enable Text Formatting, can be true or false

        iab_categories : typing.Optional[bool]
            Enable [Topic Detection](https://www.assemblyai.com/docs/models/topic-detection), can be true or false

        keyterms_prompt : typing.Optional[typing.Sequence[str]]
            Improve accuracy with up to 200 (for Universal-2) or 1000 (for Universal-3-Pro) domain-specific words or phrases (maximum 6 words per phrase).

        language_code : typing.Optional[TranscriptOptionalParamsLanguageCode]
            The language of your audio file. Possible values are found in [Supported Languages](https://www.assemblyai.com/docs/concepts/supported-languages).
            The default value is 'en_us'.

        language_codes : typing.Optional[typing.Sequence[TranscriptLanguageCode]]
            The language codes of your audio file. Used for [Code switching](/docs/speech-to-text/pre-recorded-audio/code-switching)
            One of the values specified must be `en`.

        language_confidence_threshold : typing.Optional[float]
            The confidence threshold for the automatically detected language.
            An error will be returned if the language confidence is below this threshold.
            Defaults to 0.

        language_detection : typing.Optional[bool]
            Enable [Automatic language detection](https://www.assemblyai.com/docs/models/speech-recognition#automatic-language-detection), either true or false.

        language_detection_options : typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions]
            Specify options for Automatic Language Detection.

        multichannel : typing.Optional[bool]
            Enable [Multichannel](https://www.assemblyai.com/docs/models/speech-recognition#multichannel-transcription) transcription, can be true or false.

        prompt : typing.Optional[str]
            Provide natural language prompting of up to 1,500 words of contextual information to the model.

            Note: This parameter is only supported for the Universal-3-Pro model.

        punctuate : typing.Optional[bool]
            Enable Automatic Punctuation, can be true or false

        redact_pii : typing.Optional[bool]
            Redact PII from the transcribed text using the Redact PII model, can be true or false

        redact_pii_audio : typing.Optional[bool]
            Generate a copy of the original media file with spoken PII "beeped" out, can be true or false. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.

        redact_pii_audio_options : typing.Optional[TranscriptOptionalParamsRedactPiiAudioOptions]
            Specify options for PII redacted audio files.

        redact_pii_audio_quality : typing.Optional[RedactPiiAudioQuality]
            Controls the filetype of the audio created by redact_pii_audio. Currently supports mp3 (default) and wav. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.

        redact_pii_policies : typing.Optional[typing.Sequence[PiiPolicy]]
            The list of PII Redaction policies to enable. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.

        redact_pii_sub : typing.Optional[SubstitutionPolicy]
            The replacement logic for detected PII, can be `entity_type` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.

        sentiment_analysis : typing.Optional[bool]
            Enable [Sentiment Analysis](https://www.assemblyai.com/docs/models/sentiment-analysis), can be true or false

        speaker_labels : typing.Optional[bool]
            Enable [Speaker diarization](https://www.assemblyai.com/docs/models/speaker-diarization), can be true or false

        speaker_options : typing.Optional[TranscriptOptionalParamsSpeakerOptions]
            Specify options for speaker diarization.

        speakers_expected : typing.Optional[int]
            Tells the speaker label model how many speakers it should attempt to identify. See [Speaker diarization](https://www.assemblyai.com/docs/models/speaker-diarization) for more details.

        speech_threshold : typing.Optional[float]
            Reject audio files that contain less than this fraction of speech.
            Valid values are in the range [0, 1] inclusive.

        speech_understanding : typing.Optional[TranscriptOptionalParamsSpeechUnderstanding]
            Enable speech understanding tasks like translation, speaker identification, and custom formatting

        summarization : typing.Optional[bool]
            Enable [Summarization](https://www.assemblyai.com/docs/models/summarization), can be true or false

        summary_model : typing.Optional[SummaryModel]
            The model to summarize the transcript

        summary_type : typing.Optional[SummaryType]
            The type of summary

        temperature : typing.Optional[float]
            Control the amount of randomness injected into the model's response.

            Note: This parameter can only be used with the Universal-3-Pro model.

        webhook_auth_header_name : typing.Optional[str]
            The header name to be sent with the transcript completed or failed webhook requests

        webhook_auth_header_value : typing.Optional[str]
            The header value to send back with the transcript completed or failed webhook requests for added security

        webhook_url : typing.Optional[str]
            The URL to which we send webhook requests.
            We sends two different types of webhook requests.
            One request when a transcript is completed or failed, and one request when the redacted audio is ready if redact_pii_audio is enabled.

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
        HttpResponse[Transcript]
            Transcript created and queued for processing
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/transcript",
            method="POST",
            json={
                "audio_url": audio_url,
                "audio_end_at": audio_end_at,
                "audio_start_from": audio_start_from,
                "auto_chapters": auto_chapters,
                "auto_highlights": auto_highlights,
                "content_safety": content_safety,
                "content_safety_confidence": content_safety_confidence,
                "custom_spelling": convert_and_respect_annotation_metadata(
                    object_=custom_spelling, annotation=typing.Sequence[TranscriptCustomSpelling], direction="write"
                ),
                "disfluencies": disfluencies,
                "entity_detection": entity_detection,
                "filter_profanity": filter_profanity,
                "format_text": format_text,
                "iab_categories": iab_categories,
                "keyterms_prompt": keyterms_prompt,
                "language_code": convert_and_respect_annotation_metadata(
                    object_=language_code, annotation=TranscriptOptionalParamsLanguageCode, direction="write"
                ),
                "language_codes": convert_and_respect_annotation_metadata(
                    object_=language_codes, annotation=typing.Sequence[TranscriptLanguageCode], direction="write"
                ),
                "language_confidence_threshold": language_confidence_threshold,
                "language_detection": language_detection,
                "language_detection_options": convert_and_respect_annotation_metadata(
                    object_=language_detection_options,
                    annotation=TranscriptOptionalParamsLanguageDetectionOptions,
                    direction="write",
                ),
                "multichannel": multichannel,
                "prompt": prompt,
                "punctuate": punctuate,
                "redact_pii": redact_pii,
                "redact_pii_audio": redact_pii_audio,
                "redact_pii_audio_options": convert_and_respect_annotation_metadata(
                    object_=redact_pii_audio_options,
                    annotation=TranscriptOptionalParamsRedactPiiAudioOptions,
                    direction="write",
                ),
                "redact_pii_audio_quality": redact_pii_audio_quality,
                "redact_pii_policies": redact_pii_policies,
                "redact_pii_sub": redact_pii_sub,
                "sentiment_analysis": sentiment_analysis,
                "speaker_labels": speaker_labels,
                "speaker_options": convert_and_respect_annotation_metadata(
                    object_=speaker_options, annotation=TranscriptOptionalParamsSpeakerOptions, direction="write"
                ),
                "speakers_expected": speakers_expected,
                "speech_models": speech_models,
                "speech_threshold": speech_threshold,
                "speech_understanding": convert_and_respect_annotation_metadata(
                    object_=speech_understanding,
                    annotation=TranscriptOptionalParamsSpeechUnderstanding,
                    direction="write",
                ),
                "summarization": summarization,
                "summary_model": summary_model,
                "summary_type": summary_type,
                "temperature": temperature,
                "webhook_auth_header_name": webhook_auth_header_name,
                "webhook_auth_header_value": webhook_auth_header_value,
                "webhook_url": webhook_url,
                "custom_topics": custom_topics,
                "speech_model": speech_model,
                "topics": topics,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Transcript,
                    parse_obj_as(
                        type_=Transcript,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Transcript]:
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
        HttpResponse[Transcript]
            The transcript resource
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Transcript,
                    parse_obj_as(
                        type_=Transcript,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Transcript]:
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
        HttpResponse[Transcript]
            The deleted transcript response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Transcript,
                    parse_obj_as(
                        type_=Transcript,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_subtitles(
        self,
        transcript_id: str,
        subtitle_format: SubtitleFormat,
        *,
        chars_per_caption: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
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
        HttpResponse[str]
            The exported captions as text
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}/{encode_path_param(subtitle_format)}",
            method="GET",
            params={
                "chars_per_caption": chars_per_caption,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_sentences(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SentencesResponse]:
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
        HttpResponse[SentencesResponse]
            Exported sentences
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}/sentences",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SentencesResponse,
                    parse_obj_as(
                        type_=SentencesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_paragraphs(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ParagraphsResponse]:
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
        HttpResponse[ParagraphsResponse]
            Exported paragraphs
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}/paragraphs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParagraphsResponse,
                    parse_obj_as(
                        type_=ParagraphsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def word_search(
        self,
        transcript_id: str,
        *,
        words: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WordSearchResponse]:
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
        HttpResponse[WordSearchResponse]
            Word search response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}/word-search",
            method="GET",
            params={
                "words": ",".join(map(str, words)) if isinstance(words, (list, tuple, set)) else words,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WordSearchResponse,
                    parse_obj_as(
                        type_=WordSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_redacted_audio(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RedactedAudioResponse]:
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
        HttpResponse[RedactedAudioResponse]
            The redacted audio object containing the status and URL to the redacted audio
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}/redacted-audio",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RedactedAudioResponse,
                    parse_obj_as(
                        type_=RedactedAudioResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTranscriptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[TranscriptList]:
        """
        <Note>To retrieve your transcriptions on our EU server, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Retrieve a list of transcripts you created.
        Transcripts are sorted from newest to oldest and can be retrieved for the last 90 days of usage. The previous URL always points to a page with older transcripts.

        If you need to retrieve transcripts from more than 90 days ago please reach out to our Support team at support@assemblyai.com.

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
        AsyncHttpResponse[TranscriptList]
            A list of transcripts. Transcripts are sorted from newest to oldest. The previous URL always points to a page with older transcripts.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/transcript",
            method="GET",
            params={
                "limit": limit,
                "status": status,
                "created_on": str(created_on) if created_on is not None else None,
                "before_id": before_id,
                "after_id": after_id,
                "throttled_only": throttled_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TranscriptList,
                    parse_obj_as(
                        type_=TranscriptList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def submit(
        self,
        *,
        audio_url: str,
        speech_models: typing.Sequence[SpeechModel],
        audio_end_at: typing.Optional[int] = OMIT,
        audio_start_from: typing.Optional[int] = OMIT,
        auto_chapters: typing.Optional[bool] = OMIT,
        auto_highlights: typing.Optional[bool] = OMIT,
        content_safety: typing.Optional[bool] = OMIT,
        content_safety_confidence: typing.Optional[int] = OMIT,
        custom_spelling: typing.Optional[typing.Sequence[TranscriptCustomSpelling]] = OMIT,
        disfluencies: typing.Optional[bool] = OMIT,
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
        sentiment_analysis: typing.Optional[bool] = OMIT,
        speaker_labels: typing.Optional[bool] = OMIT,
        speaker_options: typing.Optional[TranscriptOptionalParamsSpeakerOptions] = OMIT,
        speakers_expected: typing.Optional[int] = OMIT,
        speech_threshold: typing.Optional[float] = OMIT,
        speech_understanding: typing.Optional[TranscriptOptionalParamsSpeechUnderstanding] = OMIT,
        summarization: typing.Optional[bool] = OMIT,
        summary_model: typing.Optional[SummaryModel] = OMIT,
        summary_type: typing.Optional[SummaryType] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        webhook_auth_header_name: typing.Optional[str] = OMIT,
        webhook_auth_header_value: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        custom_topics: typing.Optional[bool] = OMIT,
        speech_model: typing.Optional[SpeechModel] = OMIT,
        topics: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Transcript]:
        """
        <Note>To use our EU server for transcription, replace `api.assemblyai.com` with `api.eu.assemblyai.com`.</Note>
        Create a transcript from a media file that is accessible via a URL.

        Parameters
        ----------
        audio_url : str
            The URL of the audio or video file to transcribe.

        speech_models : typing.Sequence[SpeechModel]
            List multiple speech models in priority order, allowing our system to automatically route your audio to the best available option.

        audio_end_at : typing.Optional[int]
            The point in time, in milliseconds, to stop transcribing in your media file

        audio_start_from : typing.Optional[int]
            The point in time, in milliseconds, to begin transcribing in your media file

        auto_chapters : typing.Optional[bool]
            Enable [Auto Chapters](https://www.assemblyai.com/docs/models/auto-chapters), can be true or false

        auto_highlights : typing.Optional[bool]
            Enable Key Phrases, either true or false

        content_safety : typing.Optional[bool]
            Enable [Content Moderation](https://www.assemblyai.com/docs/models/content-moderation), can be true or false

        content_safety_confidence : typing.Optional[int]
            The confidence threshold for the Content Moderation model. Values must be between 25 and 100.

        custom_spelling : typing.Optional[typing.Sequence[TranscriptCustomSpelling]]
            Customize how words are spelled and formatted using to and from values

        disfluencies : typing.Optional[bool]
            Transcribe Filler Words, like "umm", in your media file; can be true or false

        entity_detection : typing.Optional[bool]
            Enable [Entity Detection](https://www.assemblyai.com/docs/models/entity-detection), can be true or false

        filter_profanity : typing.Optional[bool]
            Filter profanity from the transcribed text, can be true or false

        format_text : typing.Optional[bool]
            Enable Text Formatting, can be true or false

        iab_categories : typing.Optional[bool]
            Enable [Topic Detection](https://www.assemblyai.com/docs/models/topic-detection), can be true or false

        keyterms_prompt : typing.Optional[typing.Sequence[str]]
            Improve accuracy with up to 200 (for Universal-2) or 1000 (for Universal-3-Pro) domain-specific words or phrases (maximum 6 words per phrase).

        language_code : typing.Optional[TranscriptOptionalParamsLanguageCode]
            The language of your audio file. Possible values are found in [Supported Languages](https://www.assemblyai.com/docs/concepts/supported-languages).
            The default value is 'en_us'.

        language_codes : typing.Optional[typing.Sequence[TranscriptLanguageCode]]
            The language codes of your audio file. Used for [Code switching](/docs/speech-to-text/pre-recorded-audio/code-switching)
            One of the values specified must be `en`.

        language_confidence_threshold : typing.Optional[float]
            The confidence threshold for the automatically detected language.
            An error will be returned if the language confidence is below this threshold.
            Defaults to 0.

        language_detection : typing.Optional[bool]
            Enable [Automatic language detection](https://www.assemblyai.com/docs/models/speech-recognition#automatic-language-detection), either true or false.

        language_detection_options : typing.Optional[TranscriptOptionalParamsLanguageDetectionOptions]
            Specify options for Automatic Language Detection.

        multichannel : typing.Optional[bool]
            Enable [Multichannel](https://www.assemblyai.com/docs/models/speech-recognition#multichannel-transcription) transcription, can be true or false.

        prompt : typing.Optional[str]
            Provide natural language prompting of up to 1,500 words of contextual information to the model.

            Note: This parameter is only supported for the Universal-3-Pro model.

        punctuate : typing.Optional[bool]
            Enable Automatic Punctuation, can be true or false

        redact_pii : typing.Optional[bool]
            Redact PII from the transcribed text using the Redact PII model, can be true or false

        redact_pii_audio : typing.Optional[bool]
            Generate a copy of the original media file with spoken PII "beeped" out, can be true or false. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.

        redact_pii_audio_options : typing.Optional[TranscriptOptionalParamsRedactPiiAudioOptions]
            Specify options for PII redacted audio files.

        redact_pii_audio_quality : typing.Optional[RedactPiiAudioQuality]
            Controls the filetype of the audio created by redact_pii_audio. Currently supports mp3 (default) and wav. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.

        redact_pii_policies : typing.Optional[typing.Sequence[PiiPolicy]]
            The list of PII Redaction policies to enable. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.

        redact_pii_sub : typing.Optional[SubstitutionPolicy]
            The replacement logic for detected PII, can be `entity_type` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.

        sentiment_analysis : typing.Optional[bool]
            Enable [Sentiment Analysis](https://www.assemblyai.com/docs/models/sentiment-analysis), can be true or false

        speaker_labels : typing.Optional[bool]
            Enable [Speaker diarization](https://www.assemblyai.com/docs/models/speaker-diarization), can be true or false

        speaker_options : typing.Optional[TranscriptOptionalParamsSpeakerOptions]
            Specify options for speaker diarization.

        speakers_expected : typing.Optional[int]
            Tells the speaker label model how many speakers it should attempt to identify. See [Speaker diarization](https://www.assemblyai.com/docs/models/speaker-diarization) for more details.

        speech_threshold : typing.Optional[float]
            Reject audio files that contain less than this fraction of speech.
            Valid values are in the range [0, 1] inclusive.

        speech_understanding : typing.Optional[TranscriptOptionalParamsSpeechUnderstanding]
            Enable speech understanding tasks like translation, speaker identification, and custom formatting

        summarization : typing.Optional[bool]
            Enable [Summarization](https://www.assemblyai.com/docs/models/summarization), can be true or false

        summary_model : typing.Optional[SummaryModel]
            The model to summarize the transcript

        summary_type : typing.Optional[SummaryType]
            The type of summary

        temperature : typing.Optional[float]
            Control the amount of randomness injected into the model's response.

            Note: This parameter can only be used with the Universal-3-Pro model.

        webhook_auth_header_name : typing.Optional[str]
            The header name to be sent with the transcript completed or failed webhook requests

        webhook_auth_header_value : typing.Optional[str]
            The header value to send back with the transcript completed or failed webhook requests for added security

        webhook_url : typing.Optional[str]
            The URL to which we send webhook requests.
            We sends two different types of webhook requests.
            One request when a transcript is completed or failed, and one request when the redacted audio is ready if redact_pii_audio is enabled.

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
        AsyncHttpResponse[Transcript]
            Transcript created and queued for processing
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/transcript",
            method="POST",
            json={
                "audio_url": audio_url,
                "audio_end_at": audio_end_at,
                "audio_start_from": audio_start_from,
                "auto_chapters": auto_chapters,
                "auto_highlights": auto_highlights,
                "content_safety": content_safety,
                "content_safety_confidence": content_safety_confidence,
                "custom_spelling": convert_and_respect_annotation_metadata(
                    object_=custom_spelling, annotation=typing.Sequence[TranscriptCustomSpelling], direction="write"
                ),
                "disfluencies": disfluencies,
                "entity_detection": entity_detection,
                "filter_profanity": filter_profanity,
                "format_text": format_text,
                "iab_categories": iab_categories,
                "keyterms_prompt": keyterms_prompt,
                "language_code": convert_and_respect_annotation_metadata(
                    object_=language_code, annotation=TranscriptOptionalParamsLanguageCode, direction="write"
                ),
                "language_codes": convert_and_respect_annotation_metadata(
                    object_=language_codes, annotation=typing.Sequence[TranscriptLanguageCode], direction="write"
                ),
                "language_confidence_threshold": language_confidence_threshold,
                "language_detection": language_detection,
                "language_detection_options": convert_and_respect_annotation_metadata(
                    object_=language_detection_options,
                    annotation=TranscriptOptionalParamsLanguageDetectionOptions,
                    direction="write",
                ),
                "multichannel": multichannel,
                "prompt": prompt,
                "punctuate": punctuate,
                "redact_pii": redact_pii,
                "redact_pii_audio": redact_pii_audio,
                "redact_pii_audio_options": convert_and_respect_annotation_metadata(
                    object_=redact_pii_audio_options,
                    annotation=TranscriptOptionalParamsRedactPiiAudioOptions,
                    direction="write",
                ),
                "redact_pii_audio_quality": redact_pii_audio_quality,
                "redact_pii_policies": redact_pii_policies,
                "redact_pii_sub": redact_pii_sub,
                "sentiment_analysis": sentiment_analysis,
                "speaker_labels": speaker_labels,
                "speaker_options": convert_and_respect_annotation_metadata(
                    object_=speaker_options, annotation=TranscriptOptionalParamsSpeakerOptions, direction="write"
                ),
                "speakers_expected": speakers_expected,
                "speech_models": speech_models,
                "speech_threshold": speech_threshold,
                "speech_understanding": convert_and_respect_annotation_metadata(
                    object_=speech_understanding,
                    annotation=TranscriptOptionalParamsSpeechUnderstanding,
                    direction="write",
                ),
                "summarization": summarization,
                "summary_model": summary_model,
                "summary_type": summary_type,
                "temperature": temperature,
                "webhook_auth_header_name": webhook_auth_header_name,
                "webhook_auth_header_value": webhook_auth_header_value,
                "webhook_url": webhook_url,
                "custom_topics": custom_topics,
                "speech_model": speech_model,
                "topics": topics,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Transcript,
                    parse_obj_as(
                        type_=Transcript,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Transcript]:
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
        AsyncHttpResponse[Transcript]
            The transcript resource
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Transcript,
                    parse_obj_as(
                        type_=Transcript,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Transcript]:
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
        AsyncHttpResponse[Transcript]
            The deleted transcript response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Transcript,
                    parse_obj_as(
                        type_=Transcript,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_subtitles(
        self,
        transcript_id: str,
        subtitle_format: SubtitleFormat,
        *,
        chars_per_caption: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]
            The exported captions as text
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}/{encode_path_param(subtitle_format)}",
            method="GET",
            params={
                "chars_per_caption": chars_per_caption,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_sentences(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SentencesResponse]:
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
        AsyncHttpResponse[SentencesResponse]
            Exported sentences
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}/sentences",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SentencesResponse,
                    parse_obj_as(
                        type_=SentencesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_paragraphs(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ParagraphsResponse]:
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
        AsyncHttpResponse[ParagraphsResponse]
            Exported paragraphs
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}/paragraphs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParagraphsResponse,
                    parse_obj_as(
                        type_=ParagraphsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def word_search(
        self,
        transcript_id: str,
        *,
        words: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WordSearchResponse]:
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
        AsyncHttpResponse[WordSearchResponse]
            Word search response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}/word-search",
            method="GET",
            params={
                "words": ",".join(map(str, words)) if isinstance(words, (list, tuple, set)) else words,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WordSearchResponse,
                    parse_obj_as(
                        type_=WordSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_redacted_audio(
        self, transcript_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RedactedAudioResponse]:
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
        AsyncHttpResponse[RedactedAudioResponse]
            The redacted audio object containing the status and URL to the redacted audio
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/transcript/{encode_path_param(transcript_id)}/redacted-audio",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RedactedAudioResponse,
                    parse_obj_as(
                        type_=RedactedAudioResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
