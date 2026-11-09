

import contextlib
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.create_speech_request_model import CreateSpeechRequestModel
from .types.create_speech_request_response_format import CreateSpeechRequestResponseFormat
from .types.create_speech_request_voice import CreateSpeechRequestVoice
from .types.create_transcription_request_model import CreateTranscriptionRequestModel
from .types.create_transcription_request_response_format import CreateTranscriptionRequestResponseFormat
from .types.create_transcription_request_timestamp_granularities_item import (
    CreateTranscriptionRequestTimestampGranularitiesItem,
)
from .types.create_transcription_response import CreateTranscriptionResponse
from .types.create_translation_request_model import CreateTranslationRequestModel
from .types.create_translation_response import CreateTranslationResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAudioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def create_speech(
        self,
        *,
        model: CreateSpeechRequestModel,
        input: str,
        voice: CreateSpeechRequestVoice,
        response_format: typing.Optional[CreateSpeechRequestResponseFormat] = OMIT,
        speed: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        model : CreateSpeechRequestModel
            One of the available [TTS models](/docs/models/tts): `tts-1` or `tts-1-hd`

        input : str
            The text to generate audio for. The maximum length is 4096 characters.

        voice : CreateSpeechRequestVoice
            The voice to use when generating the audio. Supported voices are `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`. Previews of the voices are available in the [Text to speech guide](/docs/guides/text-to-speech/voice-options).

        response_format : typing.Optional[CreateSpeechRequestResponseFormat]
            The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

        speed : typing.Optional[float]
            The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            OK
        """
        with self._client_wrapper.httpx_client.stream(
            "audio/speech",
            method="POST",
            json={
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=CreateSpeechRequestModel, direction="write"
                ),
                "input": input,
                "voice": voice,
                "response_format": response_format,
                "speed": speed,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def create_transcription(
        self,
        *,
        file: core.File,
        model: CreateTranscriptionRequestModel,
        language: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[CreateTranscriptionRequestResponseFormat] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        timestamp_granularities: typing.Optional[
            typing.List[CreateTranscriptionRequestTimestampGranularitiesItem]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTranscriptionResponse]:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : CreateTranscriptionRequestModel
            ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

        language : typing.Optional[str]
            The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.

        prompt : typing.Optional[str]
            An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should match the audio language.

        response_format : typing.Optional[CreateTranscriptionRequestResponseFormat]
            The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

        temperature : typing.Optional[float]
            The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

        timestamp_granularities : typing.Optional[typing.List[CreateTranscriptionRequestTimestampGranularitiesItem]]
            The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTranscriptionResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "audio/transcriptions",
            method="POST",
            data={
                "model": model,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
                "timestamp_granularities[]": jsonable_encoder(timestamp_granularities)
                if timestamp_granularities is not OMIT
                else OMIT,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTranscriptionResponse,
                    parse_obj_as(
                        type_=CreateTranscriptionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_translation(
        self,
        *,
        file: core.File,
        model: CreateTranslationRequestModel,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTranslationResponse]:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : CreateTranslationRequestModel
            ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

        prompt : typing.Optional[str]
            An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should be in English.

        response_format : typing.Optional[str]
            The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

        temperature : typing.Optional[float]
            The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTranslationResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "audio/translations",
            method="POST",
            data={
                "model": model,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTranslationResponse,
                    parse_obj_as(
                        type_=CreateTranslationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAudioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def create_speech(
        self,
        *,
        model: CreateSpeechRequestModel,
        input: str,
        voice: CreateSpeechRequestVoice,
        response_format: typing.Optional[CreateSpeechRequestResponseFormat] = OMIT,
        speed: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        model : CreateSpeechRequestModel
            One of the available [TTS models](/docs/models/tts): `tts-1` or `tts-1-hd`

        input : str
            The text to generate audio for. The maximum length is 4096 characters.

        voice : CreateSpeechRequestVoice
            The voice to use when generating the audio. Supported voices are `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`. Previews of the voices are available in the [Text to speech guide](/docs/guides/text-to-speech/voice-options).

        response_format : typing.Optional[CreateSpeechRequestResponseFormat]
            The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

        speed : typing.Optional[float]
            The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            OK
        """
        async with self._client_wrapper.httpx_client.stream(
            "audio/speech",
            method="POST",
            json={
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=CreateSpeechRequestModel, direction="write"
                ),
                "input": input,
                "voice": voice,
                "response_format": response_format,
                "speed": speed,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def create_transcription(
        self,
        *,
        file: core.File,
        model: CreateTranscriptionRequestModel,
        language: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[CreateTranscriptionRequestResponseFormat] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        timestamp_granularities: typing.Optional[
            typing.List[CreateTranscriptionRequestTimestampGranularitiesItem]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTranscriptionResponse]:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : CreateTranscriptionRequestModel
            ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

        language : typing.Optional[str]
            The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.

        prompt : typing.Optional[str]
            An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should match the audio language.

        response_format : typing.Optional[CreateTranscriptionRequestResponseFormat]
            The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

        temperature : typing.Optional[float]
            The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

        timestamp_granularities : typing.Optional[typing.List[CreateTranscriptionRequestTimestampGranularitiesItem]]
            The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTranscriptionResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "audio/transcriptions",
            method="POST",
            data={
                "model": model,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
                "timestamp_granularities[]": jsonable_encoder(timestamp_granularities)
                if timestamp_granularities is not OMIT
                else OMIT,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTranscriptionResponse,
                    parse_obj_as(
                        type_=CreateTranscriptionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_translation(
        self,
        *,
        file: core.File,
        model: CreateTranslationRequestModel,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTranslationResponse]:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : CreateTranslationRequestModel
            ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

        prompt : typing.Optional[str]
            An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should be in English.

        response_format : typing.Optional[str]
            The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

        temperature : typing.Optional[float]
            The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTranslationResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "audio/translations",
            method="POST",
            data={
                "model": model,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTranslationResponse,
                    parse_obj_as(
                        type_=CreateTranslationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
