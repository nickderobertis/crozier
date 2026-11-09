

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAudioClient, RawAudioClient
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


OMIT = typing.cast(typing.Any, ...)


class AudioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAudioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAudioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAudioClient
        """
        return self._raw_client

    def create_speech(
        self,
        *,
        model: CreateSpeechRequestModel,
        input: str,
        voice: CreateSpeechRequestVoice,
        response_format: typing.Optional[CreateSpeechRequestResponseFormat] = OMIT,
        speed: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
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
        typing.Iterator[bytes]
            OK
        """
        with self._raw_client.create_speech(
            model=model,
            input=input,
            voice=voice,
            response_format=response_format,
            speed=speed,
            request_options=request_options,
        ) as r:
            yield from r.data

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
    ) -> CreateTranscriptionResponse:
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
        CreateTranscriptionResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio.create_transcription(
            model="whisper-1",
        )
        """
        _response = self._raw_client.create_transcription(
            file=file,
            model=model,
            language=language,
            prompt=prompt,
            response_format=response_format,
            temperature=temperature,
            timestamp_granularities=timestamp_granularities,
            request_options=request_options,
        )
        return _response.data

    def create_translation(
        self,
        *,
        file: core.File,
        model: CreateTranslationRequestModel,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTranslationResponse:
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
        CreateTranslationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio.create_translation(
            model="whisper-1",
        )
        """
        _response = self._raw_client.create_translation(
            file=file,
            model=model,
            prompt=prompt,
            response_format=response_format,
            temperature=temperature,
            request_options=request_options,
        )
        return _response.data


class AsyncAudioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAudioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAudioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAudioClient
        """
        return self._raw_client

    async def create_speech(
        self,
        *,
        model: CreateSpeechRequestModel,
        input: str,
        voice: CreateSpeechRequestVoice,
        response_format: typing.Optional[CreateSpeechRequestResponseFormat] = OMIT,
        speed: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
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
        typing.AsyncIterator[bytes]
            OK
        """
        async with self._raw_client.create_speech(
            model=model,
            input=input,
            voice=voice,
            response_format=response_format,
            speed=speed,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

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
    ) -> CreateTranscriptionResponse:
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
        CreateTranscriptionResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio.create_transcription(
                model="whisper-1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_transcription(
            file=file,
            model=model,
            language=language,
            prompt=prompt,
            response_format=response_format,
            temperature=temperature,
            timestamp_granularities=timestamp_granularities,
            request_options=request_options,
        )
        return _response.data

    async def create_translation(
        self,
        *,
        file: core.File,
        model: CreateTranslationRequestModel,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTranslationResponse:
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
        CreateTranslationResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio.create_translation(
                model="whisper-1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_translation(
            file=file,
            model=model,
            prompt=prompt,
            response_format=response_format,
            temperature=temperature,
            request_options=request_options,
        )
        return _response.data
