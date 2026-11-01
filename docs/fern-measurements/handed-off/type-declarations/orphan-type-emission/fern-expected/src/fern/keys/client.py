

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.key_mode import KeyMode
from .raw_client import AsyncRawKeysClient, RawKeysClient


OMIT = typing.cast(typing.Any, ...)


class KeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKeysClient
        """
        return self._raw_client

    def create_key(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KeyMode:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyMode
            The key
        """
        _response = self._raw_client.create_key(request=request, request_options=request_options)
        return _response.data


class AsyncKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKeysClient
        """
        return self._raw_client

    async def create_key(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KeyMode:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyMode
            The key
        """
        _response = await self._raw_client.create_key(request=request, request_options=request_options)
        return _response.data
