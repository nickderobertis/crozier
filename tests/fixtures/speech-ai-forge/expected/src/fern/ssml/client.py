

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.adjust_config import AdjustConfig
from ..types.audio_format import AudioFormat
from ..types.enhancer_config import EnhancerConfig
from .raw_client import AsyncRawSsmlClient, RawSsmlClient


OMIT = typing.cast(typing.Any, ...)


class SsmlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSsmlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSsmlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSsmlClient
        """
        return self._raw_client

    def synthesize_ssml_api(
        self,
        *,
        ssml: str,
        format: typing.Optional[AudioFormat] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        eos: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        spliter_thr: typing.Optional[int] = OMIT,
        enhancer: typing.Optional[EnhancerConfig] = OMIT,
        adjuster: typing.Optional[AdjustConfig] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Synthesize speech from SSML-formatted input using a specified TTS model.

        This endpoint supports multi-speaker, multi-style speech synthesis based on structured SSML input.
        It can return audio in various formats (e.g., `raw`, `wav`, `mp3`), with optional enhancements and prosody adjustments.

        ### Supported Features
        - Multiple speakers via `<voice spk="...">`
        - Arbitrary text segmentation with sentence break markers (e.g., `eos="[uv_break]"`)
        - Streaming or full-response audio
        - Audio enhancement & pitch/speed adjustment via `EnhancerConfig` / `AdjustConfig`
        - Custom batch size & segment length control via `batch_size` / `spliter_thr`

        ### Parameters
        - `ssml` (str): SSML XML string containing structured speech content (required)
        - `format` (str): Output audio format. One of: `raw`, `wav`, `mp3` (default: `raw`)
        - `batch_size` (int): Batch size for internal TTS inference, must be > 0
        - `eos` (str): End-of-sentence token for segmentation (default: `[uv_break]`)
        - `model` (str): TTS model identifier to be used (default: `chat-tts`)
        - `spliter_thr` (int): Threshold to split long texts (default: 100, minimum: 50)
        - `enhancer` (EnhancerConfig): Optional audio enhancer settings
        - `adjuster` (AdjustConfig): Optional pitch/speed/volume control
        - `stream` (bool): If true, returns a streaming response; otherwise, file response

        ### Example SSML Input

        ```xml
        <speak version="0.1">
            <voice spk="mona">ChatTTS 用于合成多角色多情感的有声书示例</voice>
            <voice spk="mona">黛玉冷笑道：</voice>
            <voice spk="doubao" emotion="happy">我说呢，亏了绊住，不然，早就飞起来了。</voice>
            <voice spk="mona">宝玉道：</voice>
            <voice spk="mona">“只许和你玩，替你解闷。不过偶然到他那里，就说这些闲话。”</voice>
            <voice spk="doubao" emotion="angry">“好没意思的话！ 去不去，关我什么事儿？ 又没叫你替我解闷儿 ，还许你不理我呢”</voice>
            <voice spk="mona">说着，便赌气回房去了。</voice>
        </speak>
        ````

        The endpoint returns a synthesized audio file or stream based on the provided SSML and configuration.

        Parameters
        ----------
        ssml : str

        format : typing.Optional[AudioFormat]

        batch_size : typing.Optional[int]

        eos : typing.Optional[str]

        model : typing.Optional[str]

        spliter_thr : typing.Optional[int]

        enhancer : typing.Optional[EnhancerConfig]

        adjuster : typing.Optional[AdjustConfig]

        stream : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ssml.synthesize_ssml_api(
            ssml="ssml",
        )
        """
        _response = self._raw_client.synthesize_ssml_api(
            ssml=ssml,
            format=format,
            batch_size=batch_size,
            eos=eos,
            model=model,
            spliter_thr=spliter_thr,
            enhancer=enhancer,
            adjuster=adjuster,
            stream=stream,
            request_options=request_options,
        )
        return _response.data


class AsyncSsmlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSsmlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSsmlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSsmlClient
        """
        return self._raw_client

    async def synthesize_ssml_api(
        self,
        *,
        ssml: str,
        format: typing.Optional[AudioFormat] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        eos: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        spliter_thr: typing.Optional[int] = OMIT,
        enhancer: typing.Optional[EnhancerConfig] = OMIT,
        adjuster: typing.Optional[AdjustConfig] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Synthesize speech from SSML-formatted input using a specified TTS model.

        This endpoint supports multi-speaker, multi-style speech synthesis based on structured SSML input.
        It can return audio in various formats (e.g., `raw`, `wav`, `mp3`), with optional enhancements and prosody adjustments.

        ### Supported Features
        - Multiple speakers via `<voice spk="...">`
        - Arbitrary text segmentation with sentence break markers (e.g., `eos="[uv_break]"`)
        - Streaming or full-response audio
        - Audio enhancement & pitch/speed adjustment via `EnhancerConfig` / `AdjustConfig`
        - Custom batch size & segment length control via `batch_size` / `spliter_thr`

        ### Parameters
        - `ssml` (str): SSML XML string containing structured speech content (required)
        - `format` (str): Output audio format. One of: `raw`, `wav`, `mp3` (default: `raw`)
        - `batch_size` (int): Batch size for internal TTS inference, must be > 0
        - `eos` (str): End-of-sentence token for segmentation (default: `[uv_break]`)
        - `model` (str): TTS model identifier to be used (default: `chat-tts`)
        - `spliter_thr` (int): Threshold to split long texts (default: 100, minimum: 50)
        - `enhancer` (EnhancerConfig): Optional audio enhancer settings
        - `adjuster` (AdjustConfig): Optional pitch/speed/volume control
        - `stream` (bool): If true, returns a streaming response; otherwise, file response

        ### Example SSML Input

        ```xml
        <speak version="0.1">
            <voice spk="mona">ChatTTS 用于合成多角色多情感的有声书示例</voice>
            <voice spk="mona">黛玉冷笑道：</voice>
            <voice spk="doubao" emotion="happy">我说呢，亏了绊住，不然，早就飞起来了。</voice>
            <voice spk="mona">宝玉道：</voice>
            <voice spk="mona">“只许和你玩，替你解闷。不过偶然到他那里，就说这些闲话。”</voice>
            <voice spk="doubao" emotion="angry">“好没意思的话！ 去不去，关我什么事儿？ 又没叫你替我解闷儿 ，还许你不理我呢”</voice>
            <voice spk="mona">说着，便赌气回房去了。</voice>
        </speak>
        ````

        The endpoint returns a synthesized audio file or stream based on the provided SSML and configuration.

        Parameters
        ----------
        ssml : str

        format : typing.Optional[AudioFormat]

        batch_size : typing.Optional[int]

        eos : typing.Optional[str]

        model : typing.Optional[str]

        spliter_thr : typing.Optional[int]

        enhancer : typing.Optional[EnhancerConfig]

        adjuster : typing.Optional[AdjustConfig]

        stream : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ssml.synthesize_ssml_api(
                ssml="ssml",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.synthesize_ssml_api(
            ssml=ssml,
            format=format,
            batch_size=batch_size,
            eos=eos,
            model=model,
            spliter_thr=spliter_thr,
            enhancer=enhancer,
            adjuster=adjuster,
            stream=stream,
            request_options=request_options,
        )
        return _response.data
