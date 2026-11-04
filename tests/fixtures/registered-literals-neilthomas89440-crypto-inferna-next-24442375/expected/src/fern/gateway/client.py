

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGatewayClient, RawGatewayClient


OMIT = typing.cast(typing.Any, ...)


class GatewayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGatewayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGatewayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGatewayClient
        """
        return self._raw_client

    def chat_completions(
        self,
        *,
        model: str,
        messages: typing.Sequence[typing.Any],
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        model : str

        messages : typing.Sequence[typing.Any]

        stream : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success (SSE stream when stream=true)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.gateway.chat_completions(
            model="model",
            messages=[],
        )
        """
        _response = self._raw_client.chat_completions(
            model=model, messages=messages, stream=stream, request_options=request_options
        )
        return _response.data

    def embeddings(
        self,
        *,
        model: str,
        input: str,
        encoding_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        model : str

        input : str

        encoding_format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.gateway.embeddings(
            model="model",
            input="input",
        )
        """
        _response = self._raw_client.embeddings(
            model=model, input=input, encoding_format=encoding_format, request_options=request_options
        )
        return _response.data

    def audio_transcriptions(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        model: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        model : typing.Optional[str]
            Required for application/octet-stream bodies

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success
        """
        _response = self._raw_client.audio_transcriptions(request=request, model=model, request_options=request_options)
        return _response.data

    def list_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.gateway.list_models()
        """
        _response = self._raw_client.list_models(request_options=request_options)
        return _response.data


class AsyncGatewayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGatewayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGatewayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGatewayClient
        """
        return self._raw_client

    async def chat_completions(
        self,
        *,
        model: str,
        messages: typing.Sequence[typing.Any],
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        model : str

        messages : typing.Sequence[typing.Any]

        stream : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success (SSE stream when stream=true)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.gateway.chat_completions(
                model="model",
                messages=[],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chat_completions(
            model=model, messages=messages, stream=stream, request_options=request_options
        )
        return _response.data

    async def embeddings(
        self,
        *,
        model: str,
        input: str,
        encoding_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        model : str

        input : str

        encoding_format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.gateway.embeddings(
                model="model",
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.embeddings(
            model=model, input=input, encoding_format=encoding_format, request_options=request_options
        )
        return _response.data

    async def audio_transcriptions(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        model: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        model : typing.Optional[str]
            Required for application/octet-stream bodies

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success
        """
        _response = await self._raw_client.audio_transcriptions(
            request=request, model=model, request_options=request_options
        )
        return _response.data

    async def list_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.gateway.list_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_models(request_options=request_options)
        return _response.data
