

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.stt_output_format import SttOutputFormat
from ..types.transcriptions_response import TranscriptionsResponse
from .raw_client import AsyncRawSttClient, RawSttClient


OMIT = typing.cast(typing.Any, ...)


class SttClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSttClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSttClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSttClient
        """
        return self._raw_client

    def transcribe(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        sample_len: typing.Optional[int] = OMIT,
        best_of: typing.Optional[int] = OMIT,
        beam_size: typing.Optional[int] = OMIT,
        patience: typing.Optional[int] = OMIT,
        length_penalty: typing.Optional[float] = OMIT,
        format: typing.Optional[SttOutputFormat] = OMIT,
        highlight_words: typing.Optional[bool] = OMIT,
        max_line_count: typing.Optional[int] = OMIT,
        max_line_width: typing.Optional[int] = OMIT,
        max_words_per_line: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranscriptionsResponse:
        """
        Transcribes audio into the input language.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        prompt : typing.Optional[str]

        prefix : typing.Optional[str]

        language : typing.Optional[str]

        temperature : typing.Optional[float]

        sample_len : typing.Optional[int]

        best_of : typing.Optional[int]

        beam_size : typing.Optional[int]

        patience : typing.Optional[int]

        length_penalty : typing.Optional[float]

        format : typing.Optional[SttOutputFormat]

        highlight_words : typing.Optional[bool]

        max_line_count : typing.Optional[int]

        max_line_width : typing.Optional[int]

        max_words_per_line : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptionsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.stt.transcribe()
        """
        _response = self._raw_client.transcribe(
            file=file,
            model=model,
            prompt=prompt,
            prefix=prefix,
            language=language,
            temperature=temperature,
            sample_len=sample_len,
            best_of=best_of,
            beam_size=beam_size,
            patience=patience,
            length_penalty=length_penalty,
            format=format,
            highlight_words=highlight_words,
            max_line_count=max_line_count,
            max_line_width=max_line_width,
            max_words_per_line=max_words_per_line,
            request_options=request_options,
        )
        return _response.data

    def transcribe_stream(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        sample_len: typing.Optional[int] = OMIT,
        best_of: typing.Optional[int] = OMIT,
        beam_size: typing.Optional[int] = OMIT,
        patience: typing.Optional[int] = OMIT,
        length_penalty: typing.Optional[float] = OMIT,
        format: typing.Optional[SttOutputFormat] = OMIT,
        highlight_words: typing.Optional[bool] = OMIT,
        max_line_count: typing.Optional[int] = OMIT,
        max_line_width: typing.Optional[int] = OMIT,
        max_words_per_line: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Transcribes audio into the input language in real-time.

        * Not implemented yet (WIP)

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        prompt : typing.Optional[str]

        prefix : typing.Optional[str]

        language : typing.Optional[str]

        temperature : typing.Optional[float]

        sample_len : typing.Optional[int]

        best_of : typing.Optional[int]

        beam_size : typing.Optional[int]

        patience : typing.Optional[int]

        length_penalty : typing.Optional[float]

        format : typing.Optional[SttOutputFormat]

        highlight_words : typing.Optional[bool]

        max_line_count : typing.Optional[int]

        max_line_width : typing.Optional[int]

        max_words_per_line : typing.Optional[int]

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
        client.stt.transcribe_stream()
        """
        _response = self._raw_client.transcribe_stream(
            file=file,
            model=model,
            prompt=prompt,
            prefix=prefix,
            language=language,
            temperature=temperature,
            sample_len=sample_len,
            best_of=best_of,
            beam_size=beam_size,
            patience=patience,
            length_penalty=length_penalty,
            format=format,
            highlight_words=highlight_words,
            max_line_count=max_line_count,
            max_line_width=max_line_width,
            max_words_per_line=max_words_per_line,
            request_options=request_options,
        )
        return _response.data


class AsyncSttClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSttClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSttClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSttClient
        """
        return self._raw_client

    async def transcribe(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        sample_len: typing.Optional[int] = OMIT,
        best_of: typing.Optional[int] = OMIT,
        beam_size: typing.Optional[int] = OMIT,
        patience: typing.Optional[int] = OMIT,
        length_penalty: typing.Optional[float] = OMIT,
        format: typing.Optional[SttOutputFormat] = OMIT,
        highlight_words: typing.Optional[bool] = OMIT,
        max_line_count: typing.Optional[int] = OMIT,
        max_line_width: typing.Optional[int] = OMIT,
        max_words_per_line: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranscriptionsResponse:
        """
        Transcribes audio into the input language.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        prompt : typing.Optional[str]

        prefix : typing.Optional[str]

        language : typing.Optional[str]

        temperature : typing.Optional[float]

        sample_len : typing.Optional[int]

        best_of : typing.Optional[int]

        beam_size : typing.Optional[int]

        patience : typing.Optional[int]

        length_penalty : typing.Optional[float]

        format : typing.Optional[SttOutputFormat]

        highlight_words : typing.Optional[bool]

        max_line_count : typing.Optional[int]

        max_line_width : typing.Optional[int]

        max_words_per_line : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptionsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.stt.transcribe()


        asyncio.run(main())
        """
        _response = await self._raw_client.transcribe(
            file=file,
            model=model,
            prompt=prompt,
            prefix=prefix,
            language=language,
            temperature=temperature,
            sample_len=sample_len,
            best_of=best_of,
            beam_size=beam_size,
            patience=patience,
            length_penalty=length_penalty,
            format=format,
            highlight_words=highlight_words,
            max_line_count=max_line_count,
            max_line_width=max_line_width,
            max_words_per_line=max_words_per_line,
            request_options=request_options,
        )
        return _response.data

    async def transcribe_stream(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        sample_len: typing.Optional[int] = OMIT,
        best_of: typing.Optional[int] = OMIT,
        beam_size: typing.Optional[int] = OMIT,
        patience: typing.Optional[int] = OMIT,
        length_penalty: typing.Optional[float] = OMIT,
        format: typing.Optional[SttOutputFormat] = OMIT,
        highlight_words: typing.Optional[bool] = OMIT,
        max_line_count: typing.Optional[int] = OMIT,
        max_line_width: typing.Optional[int] = OMIT,
        max_words_per_line: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Transcribes audio into the input language in real-time.

        * Not implemented yet (WIP)

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        prompt : typing.Optional[str]

        prefix : typing.Optional[str]

        language : typing.Optional[str]

        temperature : typing.Optional[float]

        sample_len : typing.Optional[int]

        best_of : typing.Optional[int]

        beam_size : typing.Optional[int]

        patience : typing.Optional[int]

        length_penalty : typing.Optional[float]

        format : typing.Optional[SttOutputFormat]

        highlight_words : typing.Optional[bool]

        max_line_count : typing.Optional[int]

        max_line_width : typing.Optional[int]

        max_words_per_line : typing.Optional[int]

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
            await client.stt.transcribe_stream()


        asyncio.run(main())
        """
        _response = await self._raw_client.transcribe_stream(
            file=file,
            model=model,
            prompt=prompt,
            prefix=prefix,
            language=language,
            temperature=temperature,
            sample_len=sample_len,
            best_of=best_of,
            beam_size=beam_size,
            patience=patience,
            length_penalty=length_penalty,
            format=format,
            highlight_words=highlight_words,
            max_line_count=max_line_count,
            max_line_width=max_line_width,
            max_words_per_line=max_words_per_line,
            request_options=request_options,
        )
        return _response.data
