

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOpenapiClient, RawOpenapiClient


class OpenapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOpenapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOpenapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOpenapiClient
        """
        return self._raw_client

    def get_open_api_spec(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Returns the openapi specification file
        """
        with self._raw_client.get_open_api_spec(request_options=request_options) as r:
            yield from r.data


class AsyncOpenapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOpenapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOpenapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOpenapiClient
        """
        return self._raw_client

    async def get_open_api_spec(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Returns the openapi specification file
        """
        async with self._raw_client.get_open_api_spec(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
