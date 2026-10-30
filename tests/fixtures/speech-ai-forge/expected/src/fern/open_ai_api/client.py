

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.audio_format import AudioFormat
from .raw_client import AsyncRawOpenAiApiClient, RawOpenAiApiClient


OMIT = typing.cast(typing.Any, ...)


class OpenAiApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOpenAiApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOpenAiApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOpenAiApiClient
        """
        return self._raw_client

    def openai_speech_api(
        self,
        *,
        input: str,
        model: typing.Optional[str] = OMIT,
        voice: typing.Optional[str] = OMIT,
        response_format: typing.Optional[AudioFormat] = OMIT,
        speed: typing.Optional[float] = OMIT,
        seed: typing.Optional[int] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        style: typing.Optional[str] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        spliter_threshold: typing.Optional[float] = OMIT,
        eos: typing.Optional[str] = OMIT,
        enhance: typing.Optional[bool] = OMIT,
        denoise: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        bitrate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        openai api document:
        [https://platform.openai.com/docs/guides/text-to-speech](https://platform.openai.com/docs/guides/text-to-speech)

        以下属性为本系统自定义属性，不在openai文档中：
        - batch_size: 是否开启batch合成，小于等于1表示不使用batch （不推荐）
        - spliter_threshold: 开启batch合成时，句子分割的阈值
        - style: 风格

        > model 可填任意值

        Parameters
        ----------
        input : str

        model : typing.Optional[str]

        voice : typing.Optional[str]

        response_format : typing.Optional[AudioFormat]

        speed : typing.Optional[float]
            Speed of the audio

        seed : typing.Optional[int]

        temperature : typing.Optional[float]

        top_k : typing.Optional[int]

        top_p : typing.Optional[float]

        style : typing.Optional[str]

        batch_size : typing.Optional[int]
            Batch size

        spliter_threshold : typing.Optional[float]
            Threshold for sentence spliter

        eos : typing.Optional[str]

        enhance : typing.Optional[bool]

        denoise : typing.Optional[bool]

        stream : typing.Optional[bool]

        bitrate : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.open_ai_api.openai_speech_api(
            input="input",
        )
        """
        _response = self._raw_client.openai_speech_api(
            input=input,
            model=model,
            voice=voice,
            response_format=response_format,
            speed=speed,
            seed=seed,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            style=style,
            batch_size=batch_size,
            spliter_threshold=spliter_threshold,
            eos=eos,
            enhance=enhance,
            denoise=denoise,
            stream=stream,
            bitrate=bitrate,
            request_options=request_options,
        )
        return _response.data

    def transcribe(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        timestamp_granularities: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Transcribes audio into the input language.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        language : typing.Optional[str]

        prompt : typing.Optional[str]

        response_format : typing.Optional[str]

        temperature : typing.Optional[float]

        timestamp_granularities : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.open_ai_api.transcribe()
        """
        _response = self._raw_client.transcribe(
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


class AsyncOpenAiApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOpenAiApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOpenAiApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOpenAiApiClient
        """
        return self._raw_client

    async def openai_speech_api(
        self,
        *,
        input: str,
        model: typing.Optional[str] = OMIT,
        voice: typing.Optional[str] = OMIT,
        response_format: typing.Optional[AudioFormat] = OMIT,
        speed: typing.Optional[float] = OMIT,
        seed: typing.Optional[int] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        style: typing.Optional[str] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        spliter_threshold: typing.Optional[float] = OMIT,
        eos: typing.Optional[str] = OMIT,
        enhance: typing.Optional[bool] = OMIT,
        denoise: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        bitrate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        openai api document:
        [https://platform.openai.com/docs/guides/text-to-speech](https://platform.openai.com/docs/guides/text-to-speech)

        以下属性为本系统自定义属性，不在openai文档中：
        - batch_size: 是否开启batch合成，小于等于1表示不使用batch （不推荐）
        - spliter_threshold: 开启batch合成时，句子分割的阈值
        - style: 风格

        > model 可填任意值

        Parameters
        ----------
        input : str

        model : typing.Optional[str]

        voice : typing.Optional[str]

        response_format : typing.Optional[AudioFormat]

        speed : typing.Optional[float]
            Speed of the audio

        seed : typing.Optional[int]

        temperature : typing.Optional[float]

        top_k : typing.Optional[int]

        top_p : typing.Optional[float]

        style : typing.Optional[str]

        batch_size : typing.Optional[int]
            Batch size

        spliter_threshold : typing.Optional[float]
            Threshold for sentence spliter

        eos : typing.Optional[str]

        enhance : typing.Optional[bool]

        denoise : typing.Optional[bool]

        stream : typing.Optional[bool]

        bitrate : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.open_ai_api.openai_speech_api(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.openai_speech_api(
            input=input,
            model=model,
            voice=voice,
            response_format=response_format,
            speed=speed,
            seed=seed,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            style=style,
            batch_size=batch_size,
            spliter_threshold=spliter_threshold,
            eos=eos,
            enhance=enhance,
            denoise=denoise,
            stream=stream,
            bitrate=bitrate,
            request_options=request_options,
        )
        return _response.data

    async def transcribe(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        timestamp_granularities: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Transcribes audio into the input language.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        language : typing.Optional[str]

        prompt : typing.Optional[str]

        response_format : typing.Optional[str]

        temperature : typing.Optional[float]

        timestamp_granularities : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.open_ai_api.transcribe()


        asyncio.run(main())
        """
        _response = await self._raw_client.transcribe(
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
