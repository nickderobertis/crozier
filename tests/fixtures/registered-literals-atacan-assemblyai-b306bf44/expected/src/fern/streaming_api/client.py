

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawStreamingApiClient, RawStreamingApiClient
from .types.generate_streaming_token_streaming_api_response import GenerateStreamingTokenStreamingApiResponse


class StreamingApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStreamingApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStreamingApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStreamingApiClient
        """
        return self._raw_client

    def generate_streaming_token(
        self,
        *,
        expires_in_seconds: int,
        max_session_duration_seconds: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateStreamingTokenStreamingApiResponse:
        """
        Generates a temporary authentication token for use with streaming services.

        Parameters
        ----------
        expires_in_seconds : int
            The desired expiration time for the token in seconds.

        max_session_duration_seconds : typing.Optional[int]
            The desired maximum duration for the session started using this token in seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateStreamingTokenStreamingApiResponse
            Successfully generated temporary token

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.streaming_api.generate_streaming_token(
            expires_in_seconds=60,
            max_session_duration_seconds=600,
        )
        """
        _response = self._raw_client.generate_streaming_token(
            expires_in_seconds=expires_in_seconds,
            max_session_duration_seconds=max_session_duration_seconds,
            request_options=request_options,
        )
        return _response.data


class AsyncStreamingApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStreamingApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStreamingApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStreamingApiClient
        """
        return self._raw_client

    async def generate_streaming_token(
        self,
        *,
        expires_in_seconds: int,
        max_session_duration_seconds: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateStreamingTokenStreamingApiResponse:
        """
        Generates a temporary authentication token for use with streaming services.

        Parameters
        ----------
        expires_in_seconds : int
            The desired expiration time for the token in seconds.

        max_session_duration_seconds : typing.Optional[int]
            The desired maximum duration for the session started using this token in seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateStreamingTokenStreamingApiResponse
            Successfully generated temporary token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.streaming_api.generate_streaming_token(
                expires_in_seconds=60,
                max_session_duration_seconds=600,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_streaming_token(
            expires_in_seconds=expires_in_seconds,
            max_session_duration_seconds=max_session_duration_seconds,
            request_options=request_options,
        )
        return _response.data
