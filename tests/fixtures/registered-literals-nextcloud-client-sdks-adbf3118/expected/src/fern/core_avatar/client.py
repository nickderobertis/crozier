

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCoreAvatarClient, RawCoreAvatarClient


class CoreAvatarClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreAvatarClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreAvatarClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreAvatarClient
        """
        return self._raw_client

    def get_avatar_dark(
        self, user_id: str, size: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        size : int
            Size of the avatar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Avatar returned
        """
        with self._raw_client.get_avatar_dark(user_id, size, request_options=request_options) as r:
            yield from r.data

    def get_avatar(
        self, user_id: str, size: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        size : int
            Size of the avatar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Avatar returned
        """
        with self._raw_client.get_avatar(user_id, size, request_options=request_options) as r:
            yield from r.data


class AsyncCoreAvatarClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreAvatarClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreAvatarClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreAvatarClient
        """
        return self._raw_client

    async def get_avatar_dark(
        self, user_id: str, size: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        size : int
            Size of the avatar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Avatar returned
        """
        async with self._raw_client.get_avatar_dark(user_id, size, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_avatar(
        self, user_id: str, size: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        size : int
            Size of the avatar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Avatar returned
        """
        async with self._raw_client.get_avatar(user_id, size, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
