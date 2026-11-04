

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSettingsLogSettingsClient, RawSettingsLogSettingsClient


class SettingsLogSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSettingsLogSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSettingsLogSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSettingsLogSettingsClient
        """
        return self._raw_client

    def download(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[bytes]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]

        """
        with self._raw_client.download(request_options=request_options) as r:
            yield from r.data


class AsyncSettingsLogSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSettingsLogSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSettingsLogSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSettingsLogSettingsClient
        """
        return self._raw_client

    async def download(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.AsyncIterator[bytes]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]

        """
        async with self._raw_client.download(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
