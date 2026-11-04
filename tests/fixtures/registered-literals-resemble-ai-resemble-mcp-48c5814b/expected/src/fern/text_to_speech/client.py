

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTextToSpeechClient, RawTextToSpeechClient
from .types.stream_synthesize_request_precision import StreamSynthesizeRequestPrecision
from .types.synthesize_request_output_format import SynthesizeRequestOutputFormat
from .types.synthesize_request_precision import SynthesizeRequestPrecision
from .types.synthesize_response import SynthesizeResponse


OMIT = typing.cast(typing.Any, ...)


class TextToSpeechClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTextToSpeechClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTextToSpeechClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTextToSpeechClient
        """
        return self._raw_client

    def synthesize(
        self,
        *,
        voice_uuid: str,
        data: str,
        project_uuid: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        precision: typing.Optional[SynthesizeRequestPrecision] = OMIT,
        output_format: typing.Optional[SynthesizeRequestOutputFormat] = OMIT,
        sample_rate: typing.Optional[int] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        apply_custom_pronunciations: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SynthesizeResponse:
        """
        Generate speech synchronously from text or SSML. Returns complete audio as base64.

        Parameters
        ----------
        voice_uuid : str
            Voice UUID to use for synthesis

        data : str
            Text or SSML to synthesize (max 3,000 characters)

        project_uuid : typing.Optional[str]
            Optional project UUID to store the clip

        title : typing.Optional[str]
            Optional title for the generated clip

        model : typing.Optional[str]
            Model to use for synthesis. Pass `chatterbox-turbo` to use the Turbo model for lower latency and paralinguistic tag support. If not specified, defaults to Chatterbox or Chatterbox Multilingual based on the voice. Note - Chatterbox-Turbo is supported by all Rapid English voices and Pre Built Library voices.

        precision : typing.Optional[SynthesizeRequestPrecision]
            Audio precision for WAV output

        output_format : typing.Optional[SynthesizeRequestOutputFormat]
            Audio output format

        sample_rate : typing.Optional[int]
            Audio sample rate in Hz

        use_hd : typing.Optional[bool]
            Enable HD synthesis with small latency trade-off

        apply_custom_pronunciations : typing.Optional[bool]
            When true, automatically applies your team's custom pronunciations to matching words in the input text. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SynthesizeResponse
            Successful synthesis

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.text_to_speech.synthesize(
            voice_uuid="55592656",
            data="Hello from Resemble!",
        )
        """
        _response = self._raw_client.synthesize(
            voice_uuid=voice_uuid,
            data=data,
            project_uuid=project_uuid,
            title=title,
            model=model,
            precision=precision,
            output_format=output_format,
            sample_rate=sample_rate,
            use_hd=use_hd,
            apply_custom_pronunciations=apply_custom_pronunciations,
            request_options=request_options,
        )
        return _response.data

    def stream_synthesize(
        self,
        *,
        voice_uuid: str,
        data: str,
        project_uuid: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        precision: typing.Optional[StreamSynthesizeRequestPrecision] = OMIT,
        sample_rate: typing.Optional[int] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        apply_custom_pronunciations: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Stream audio as it's generated. Returns chunked WAV data for progressive playback.

        Parameters
        ----------
        voice_uuid : str
            Voice UUID to use for synthesis

        data : str
            Text or SSML to synthesize (max 2000 characters)

        project_uuid : typing.Optional[str]
            Optional project UUID to store the clip

        model : typing.Optional[str]
            Model to use for synthesis. Pass `chatterbox-turbo` to use the Turbo model for lower latency and paralinguistic tag support. If not specified, defaults to Chatterbox or Chatterbox Multilingual based on the voice. Note - Chatterbox-Turbo is supported by all Rapid English voices and Pre Built Library voices.

        precision : typing.Optional[StreamSynthesizeRequestPrecision]
            Audio precision

        sample_rate : typing.Optional[int]
            Audio sample rate in Hz

        use_hd : typing.Optional[bool]
            Enable HD synthesis with small latency trade-off

        apply_custom_pronunciations : typing.Optional[bool]
            When true, automatically applies your team's custom pronunciations to matching words in the input text. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Streaming audio response (chunked WAV)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.text_to_speech.stream_synthesize(
            voice_uuid="voice_uuid",
            data="data",
        )
        """
        with self._raw_client.stream_synthesize(
            voice_uuid=voice_uuid,
            data=data,
            project_uuid=project_uuid,
            model=model,
            precision=precision,
            sample_rate=sample_rate,
            use_hd=use_hd,
            apply_custom_pronunciations=apply_custom_pronunciations,
            request_options=request_options,
        ) as r:
            yield from r.data


class AsyncTextToSpeechClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTextToSpeechClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTextToSpeechClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTextToSpeechClient
        """
        return self._raw_client

    async def synthesize(
        self,
        *,
        voice_uuid: str,
        data: str,
        project_uuid: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        precision: typing.Optional[SynthesizeRequestPrecision] = OMIT,
        output_format: typing.Optional[SynthesizeRequestOutputFormat] = OMIT,
        sample_rate: typing.Optional[int] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        apply_custom_pronunciations: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SynthesizeResponse:
        """
        Generate speech synchronously from text or SSML. Returns complete audio as base64.

        Parameters
        ----------
        voice_uuid : str
            Voice UUID to use for synthesis

        data : str
            Text or SSML to synthesize (max 3,000 characters)

        project_uuid : typing.Optional[str]
            Optional project UUID to store the clip

        title : typing.Optional[str]
            Optional title for the generated clip

        model : typing.Optional[str]
            Model to use for synthesis. Pass `chatterbox-turbo` to use the Turbo model for lower latency and paralinguistic tag support. If not specified, defaults to Chatterbox or Chatterbox Multilingual based on the voice. Note - Chatterbox-Turbo is supported by all Rapid English voices and Pre Built Library voices.

        precision : typing.Optional[SynthesizeRequestPrecision]
            Audio precision for WAV output

        output_format : typing.Optional[SynthesizeRequestOutputFormat]
            Audio output format

        sample_rate : typing.Optional[int]
            Audio sample rate in Hz

        use_hd : typing.Optional[bool]
            Enable HD synthesis with small latency trade-off

        apply_custom_pronunciations : typing.Optional[bool]
            When true, automatically applies your team's custom pronunciations to matching words in the input text. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SynthesizeResponse
            Successful synthesis

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.text_to_speech.synthesize(
                voice_uuid="55592656",
                data="Hello from Resemble!",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.synthesize(
            voice_uuid=voice_uuid,
            data=data,
            project_uuid=project_uuid,
            title=title,
            model=model,
            precision=precision,
            output_format=output_format,
            sample_rate=sample_rate,
            use_hd=use_hd,
            apply_custom_pronunciations=apply_custom_pronunciations,
            request_options=request_options,
        )
        return _response.data

    async def stream_synthesize(
        self,
        *,
        voice_uuid: str,
        data: str,
        project_uuid: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        precision: typing.Optional[StreamSynthesizeRequestPrecision] = OMIT,
        sample_rate: typing.Optional[int] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        apply_custom_pronunciations: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Stream audio as it's generated. Returns chunked WAV data for progressive playback.

        Parameters
        ----------
        voice_uuid : str
            Voice UUID to use for synthesis

        data : str
            Text or SSML to synthesize (max 2000 characters)

        project_uuid : typing.Optional[str]
            Optional project UUID to store the clip

        model : typing.Optional[str]
            Model to use for synthesis. Pass `chatterbox-turbo` to use the Turbo model for lower latency and paralinguistic tag support. If not specified, defaults to Chatterbox or Chatterbox Multilingual based on the voice. Note - Chatterbox-Turbo is supported by all Rapid English voices and Pre Built Library voices.

        precision : typing.Optional[StreamSynthesizeRequestPrecision]
            Audio precision

        sample_rate : typing.Optional[int]
            Audio sample rate in Hz

        use_hd : typing.Optional[bool]
            Enable HD synthesis with small latency trade-off

        apply_custom_pronunciations : typing.Optional[bool]
            When true, automatically applies your team's custom pronunciations to matching words in the input text. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Streaming audio response (chunked WAV)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.text_to_speech.stream_synthesize(
                voice_uuid="voice_uuid",
                data="data",
            )


        asyncio.run(main())
        """
        async with self._raw_client.stream_synthesize(
            voice_uuid=voice_uuid,
            data=data,
            project_uuid=project_uuid,
            model=model,
            precision=precision,
            sample_rate=sample_rate,
            use_hd=use_hd,
            apply_custom_pronunciations=apply_custom_pronunciations,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk
