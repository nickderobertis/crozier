

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawXttsClient, RawXttsClient


OMIT = typing.cast(typing.Any, ...)


class XttsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawXttsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawXttsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawXttsClient
        """
        return self._raw_client

    def speakers(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

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
        client.xtts.speakers()
        """
        _response = self._raw_client.speakers(request_options=request_options)
        return _response.data

    def tts_to_audio(
        self,
        *,
        text: str,
        speaker_wav: str,
        language: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        text : str

        speaker_wav : str

        language : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.xtts.tts_to_audio(
            text="text",
            speaker_wav="speaker_wav",
        )
        """
        _response = self._raw_client.tts_to_audio(
            text=text, speaker_wav=speaker_wav, language=language, request_options=request_options
        )
        return _response.data

    def tts_stream(
        self,
        *,
        text: str,
        speaker_wav: str,
        language: typing.Optional[str] = None,
        no_cache: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        text : str

        speaker_wav : str

        language : typing.Optional[str]

        no_cache : typing.Optional[bool]

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
        client.xtts.tts_stream(
            text="text",
            speaker_wav="speaker_wav",
        )
        """
        _response = self._raw_client.tts_stream(
            text=text, speaker_wav=speaker_wav, language=language, no_cache=no_cache, request_options=request_options
        )
        return _response.data

    def set_tts_settings(
        self,
        *,
        stream_chunk_size: int,
        temperature: float,
        speed: float,
        length_penalty: float,
        repetition_penalty: float,
        top_p: float,
        top_k: int,
        enable_text_splitting: bool,
        batch_size: typing.Optional[int] = OMIT,
        eos: typing.Optional[str] = OMIT,
        infer_seed: typing.Optional[int] = OMIT,
        use_decoder: typing.Optional[bool] = OMIT,
        prompt1: typing.Optional[str] = OMIT,
        prompt2: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        spliter_threshold: typing.Optional[int] = OMIT,
        style: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        stream_chunk_size : int

        temperature : float

        speed : float

        length_penalty : float

        repetition_penalty : float

        top_p : float

        top_k : int

        enable_text_splitting : bool

        batch_size : typing.Optional[int]

        eos : typing.Optional[str]

        infer_seed : typing.Optional[int]

        use_decoder : typing.Optional[bool]

        prompt1 : typing.Optional[str]

        prompt2 : typing.Optional[str]

        prefix : typing.Optional[str]

        spliter_threshold : typing.Optional[int]

        style : typing.Optional[str]

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
        client.xtts.set_tts_settings(
            stream_chunk_size=1,
            temperature=1.1,
            speed=1.1,
            length_penalty=1.1,
            repetition_penalty=1.1,
            top_p=1.1,
            top_k=1,
            enable_text_splitting=True,
        )
        """
        _response = self._raw_client.set_tts_settings(
            stream_chunk_size=stream_chunk_size,
            temperature=temperature,
            speed=speed,
            length_penalty=length_penalty,
            repetition_penalty=repetition_penalty,
            top_p=top_p,
            top_k=top_k,
            enable_text_splitting=enable_text_splitting,
            batch_size=batch_size,
            eos=eos,
            infer_seed=infer_seed,
            use_decoder=use_decoder,
            prompt1=prompt1,
            prompt2=prompt2,
            prefix=prefix,
            spliter_threshold=spliter_threshold,
            style=style,
            request_options=request_options,
        )
        return _response.data


class AsyncXttsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawXttsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawXttsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawXttsClient
        """
        return self._raw_client

    async def speakers(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

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
            await client.xtts.speakers()


        asyncio.run(main())
        """
        _response = await self._raw_client.speakers(request_options=request_options)
        return _response.data

    async def tts_to_audio(
        self,
        *,
        text: str,
        speaker_wav: str,
        language: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        text : str

        speaker_wav : str

        language : typing.Optional[str]

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
            await client.xtts.tts_to_audio(
                text="text",
                speaker_wav="speaker_wav",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tts_to_audio(
            text=text, speaker_wav=speaker_wav, language=language, request_options=request_options
        )
        return _response.data

    async def tts_stream(
        self,
        *,
        text: str,
        speaker_wav: str,
        language: typing.Optional[str] = None,
        no_cache: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        text : str

        speaker_wav : str

        language : typing.Optional[str]

        no_cache : typing.Optional[bool]

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
            await client.xtts.tts_stream(
                text="text",
                speaker_wav="speaker_wav",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tts_stream(
            text=text, speaker_wav=speaker_wav, language=language, no_cache=no_cache, request_options=request_options
        )
        return _response.data

    async def set_tts_settings(
        self,
        *,
        stream_chunk_size: int,
        temperature: float,
        speed: float,
        length_penalty: float,
        repetition_penalty: float,
        top_p: float,
        top_k: int,
        enable_text_splitting: bool,
        batch_size: typing.Optional[int] = OMIT,
        eos: typing.Optional[str] = OMIT,
        infer_seed: typing.Optional[int] = OMIT,
        use_decoder: typing.Optional[bool] = OMIT,
        prompt1: typing.Optional[str] = OMIT,
        prompt2: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        spliter_threshold: typing.Optional[int] = OMIT,
        style: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        stream_chunk_size : int

        temperature : float

        speed : float

        length_penalty : float

        repetition_penalty : float

        top_p : float

        top_k : int

        enable_text_splitting : bool

        batch_size : typing.Optional[int]

        eos : typing.Optional[str]

        infer_seed : typing.Optional[int]

        use_decoder : typing.Optional[bool]

        prompt1 : typing.Optional[str]

        prompt2 : typing.Optional[str]

        prefix : typing.Optional[str]

        spliter_threshold : typing.Optional[int]

        style : typing.Optional[str]

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
            await client.xtts.set_tts_settings(
                stream_chunk_size=1,
                temperature=1.1,
                speed=1.1,
                length_penalty=1.1,
                repetition_penalty=1.1,
                top_p=1.1,
                top_k=1,
                enable_text_splitting=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_tts_settings(
            stream_chunk_size=stream_chunk_size,
            temperature=temperature,
            speed=speed,
            length_penalty=length_penalty,
            repetition_penalty=repetition_penalty,
            top_p=top_p,
            top_k=top_k,
            enable_text_splitting=enable_text_splitting,
            batch_size=batch_size,
            eos=eos,
            infer_seed=infer_seed,
            use_decoder=use_decoder,
            prompt1=prompt1,
            prompt2=prompt2,
            prefix=prefix,
            spliter_threshold=spliter_threshold,
            style=style,
            request_options=request_options,
        )
        return _response.data
