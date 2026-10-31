

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.audio_config import AudioConfig
from ..types.enhancer_config import EnhancerConfig
from ..types.google_text_synthesize_response import GoogleTextSynthesizeResponse
from ..types.synthesis_input import SynthesisInput
from ..types.voice_selection_params import VoiceSelectionParams
from .raw_client import AsyncRawGoogleApiClient, RawGoogleApiClient


OMIT = typing.cast(typing.Any, ...)


class GoogleApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGoogleApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGoogleApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGoogleApiClient
        """
        return self._raw_client

    def google_text_synthesize(
        self,
        *,
        input: SynthesisInput,
        voice: VoiceSelectionParams,
        audio_config: AudioConfig,
        enhancer_config: typing.Optional[EnhancerConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleTextSynthesizeResponse:
        """
        google api document: <br/>
        [https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize](https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize)

        - 多个属性在本系统中无用仅仅是为了兼容google api
        - voice 中的 topP, topK, temperature 为本系统中的参数
        - voice.name 即 speaker name （或者speaker seed）
        - voice.seed 为 infer seed （可在webui中测试具体作用）

        - 编码格式影响的是 audioContent 的二进制格式，所以所有format都是返回带有base64数据的json

        Parameters
        ----------
        input : SynthesisInput

        voice : VoiceSelectionParams

        audio_config : AudioConfig

        enhancer_config : typing.Optional[EnhancerConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleTextSynthesizeResponse
            Successful Response

        Examples
        --------
        from fern import AudioConfig, FernApi, SynthesisInput, VoiceSelectionParams

        client = FernApi()
        client.google_api.google_text_synthesize(
            input=SynthesisInput(),
            voice=VoiceSelectionParams(),
            audio_config=AudioConfig(),
        )
        """
        _response = self._raw_client.google_text_synthesize(
            input=input,
            voice=voice,
            audio_config=audio_config,
            enhancer_config=enhancer_config,
            request_options=request_options,
        )
        return _response.data

    def speech_recognize(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Performs synchronous speech recognition: receive results after all audio has been sent and processed.

        Parameters
        ----------
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
        client.google_api.speech_recognize()
        """
        _response = self._raw_client.speech_recognize(request_options=request_options)
        return _response.data

    def long_running_recognize(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Performs asynchronous speech recognition: receive results via the google.longrunning.Operations interface.

        Parameters
        ----------
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
        client.google_api.long_running_recognize()
        """
        _response = self._raw_client.long_running_recognize(request_options=request_options)
        return _response.data


class AsyncGoogleApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGoogleApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGoogleApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGoogleApiClient
        """
        return self._raw_client

    async def google_text_synthesize(
        self,
        *,
        input: SynthesisInput,
        voice: VoiceSelectionParams,
        audio_config: AudioConfig,
        enhancer_config: typing.Optional[EnhancerConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleTextSynthesizeResponse:
        """
        google api document: <br/>
        [https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize](https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize)

        - 多个属性在本系统中无用仅仅是为了兼容google api
        - voice 中的 topP, topK, temperature 为本系统中的参数
        - voice.name 即 speaker name （或者speaker seed）
        - voice.seed 为 infer seed （可在webui中测试具体作用）

        - 编码格式影响的是 audioContent 的二进制格式，所以所有format都是返回带有base64数据的json

        Parameters
        ----------
        input : SynthesisInput

        voice : VoiceSelectionParams

        audio_config : AudioConfig

        enhancer_config : typing.Optional[EnhancerConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleTextSynthesizeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AudioConfig, SynthesisInput, VoiceSelectionParams

        client = AsyncFernApi()


        async def main() -> None:
            await client.google_api.google_text_synthesize(
                input=SynthesisInput(),
                voice=VoiceSelectionParams(),
                audio_config=AudioConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.google_text_synthesize(
            input=input,
            voice=voice,
            audio_config=audio_config,
            enhancer_config=enhancer_config,
            request_options=request_options,
        )
        return _response.data

    async def speech_recognize(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Performs synchronous speech recognition: receive results after all audio has been sent and processed.

        Parameters
        ----------
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
            await client.google_api.speech_recognize()


        asyncio.run(main())
        """
        _response = await self._raw_client.speech_recognize(request_options=request_options)
        return _response.data

    async def long_running_recognize(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Performs asynchronous speech recognition: receive results via the google.longrunning.Operations interface.

        Parameters
        ----------
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
            await client.google_api.long_running_recognize()


        asyncio.run(main())
        """
        _response = await self._raw_client.long_running_recognize(request_options=request_options)
        return _response.data
