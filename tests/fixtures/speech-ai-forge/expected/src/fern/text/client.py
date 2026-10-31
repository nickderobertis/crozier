

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.base_response import BaseResponse
from ..types.tn_config import TnConfig
from .raw_client import AsyncRawTextClient, RawTextClient
from .types.text_normalize_request_pipe_id import TextNormalizeRequestPipeId


OMIT = typing.cast(typing.Any, ...)


class TextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTextClient
        """
        return self._raw_client

    def refiner_prompt_post(
        self,
        *,
        text: str,
        prompt: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        repetition_penalty: typing.Optional[float] = OMIT,
        max_new_token: typing.Optional[int] = OMIT,
        spliter_threshold: typing.Optional[int] = OMIT,
        normalize: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        **DeprecationWarning**

        This endpoint is deprecated and will be removed in the future.

        Requirements:
        - `chattts` model

        Parameters
        ----------
        text : str

        prompt : typing.Optional[str]

        seed : typing.Optional[int]

        top_p : typing.Optional[float]

        top_k : typing.Optional[int]

        temperature : typing.Optional[float]

        repetition_penalty : typing.Optional[float]

        max_new_token : typing.Optional[int]

        spliter_threshold : typing.Optional[int]

        normalize : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.text.refiner_prompt_post(
            text="text",
        )
        """
        _response = self._raw_client.refiner_prompt_post(
            text=text,
            prompt=prompt,
            seed=seed,
            top_p=top_p,
            top_k=top_k,
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            max_new_token=max_new_token,
            spliter_threshold=spliter_threshold,
            normalize=normalize,
            request_options=request_options,
        )
        return _response.data

    def text_normalize_post(
        self,
        *,
        text: str,
        pipe_id: typing.Optional[TextNormalizeRequestPipeId] = OMIT,
        config: typing.Optional[TnConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Normalize raw input text using a selected Text Normalization (TN) pipeline.

        This endpoint supports different TN implementations to perform text normalization
        (e.g., expanding numbers, abbreviations, adding pauses or prosodic markers for TTS, etc.).

        ### Parameters

        - `text` (str): The raw text to normalize.
        - `pipe_id` (str): The TN pipeline to use. Available options:
          - `base`
          - `chat-tts`
          - `cosy-voice`
          - `fish-speech`
          - `f5-tts`
          - `index-tts`
          - `spark-tts`
        - `config` (TNConfig, optional): Optional configuration to customize TN behavior for specific pipelines.

        ### Returns

        A normalized version of the input text, suitable for use in speech synthesis or downstream NLP tasks.

        Parameters
        ----------
        text : str

        pipe_id : typing.Optional[TextNormalizeRequestPipeId]

        config : typing.Optional[TnConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.text.text_normalize_post(
            text="text",
        )
        """
        _response = self._raw_client.text_normalize_post(
            text=text, pipe_id=pipe_id, config=config, request_options=request_options
        )
        return _response.data


class AsyncTextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTextClient
        """
        return self._raw_client

    async def refiner_prompt_post(
        self,
        *,
        text: str,
        prompt: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        repetition_penalty: typing.Optional[float] = OMIT,
        max_new_token: typing.Optional[int] = OMIT,
        spliter_threshold: typing.Optional[int] = OMIT,
        normalize: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        **DeprecationWarning**

        This endpoint is deprecated and will be removed in the future.

        Requirements:
        - `chattts` model

        Parameters
        ----------
        text : str

        prompt : typing.Optional[str]

        seed : typing.Optional[int]

        top_p : typing.Optional[float]

        top_k : typing.Optional[int]

        temperature : typing.Optional[float]

        repetition_penalty : typing.Optional[float]

        max_new_token : typing.Optional[int]

        spliter_threshold : typing.Optional[int]

        normalize : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.text.refiner_prompt_post(
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refiner_prompt_post(
            text=text,
            prompt=prompt,
            seed=seed,
            top_p=top_p,
            top_k=top_k,
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            max_new_token=max_new_token,
            spliter_threshold=spliter_threshold,
            normalize=normalize,
            request_options=request_options,
        )
        return _response.data

    async def text_normalize_post(
        self,
        *,
        text: str,
        pipe_id: typing.Optional[TextNormalizeRequestPipeId] = OMIT,
        config: typing.Optional[TnConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Normalize raw input text using a selected Text Normalization (TN) pipeline.

        This endpoint supports different TN implementations to perform text normalization
        (e.g., expanding numbers, abbreviations, adding pauses or prosodic markers for TTS, etc.).

        ### Parameters

        - `text` (str): The raw text to normalize.
        - `pipe_id` (str): The TN pipeline to use. Available options:
          - `base`
          - `chat-tts`
          - `cosy-voice`
          - `fish-speech`
          - `f5-tts`
          - `index-tts`
          - `spark-tts`
        - `config` (TNConfig, optional): Optional configuration to customize TN behavior for specific pipelines.

        ### Returns

        A normalized version of the input text, suitable for use in speech synthesis or downstream NLP tasks.

        Parameters
        ----------
        text : str

        pipe_id : typing.Optional[TextNormalizeRequestPipeId]

        config : typing.Optional[TnConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.text.text_normalize_post(
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.text_normalize_post(
            text=text, pipe_id=pipe_id, config=config, request_options=request_options
        )
        return _response.data
