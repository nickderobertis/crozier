

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCoreGuestAvatarClient, RawCoreGuestAvatarClient


class CoreGuestAvatarClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreGuestAvatarClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreGuestAvatarClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreGuestAvatarClient
        """
        return self._raw_client

    def get_avatar_dark(
        self, guest_name: str, size: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        guest_name : str
            The guest name, e.g. "Albert"

        size : str
            The desired avatar size, e.g. 64 for 64x64px

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Custom avatar returned
        """
        with self._raw_client.get_avatar_dark(guest_name, size, request_options=request_options) as r:
            yield from r.data

    def get_avatar(
        self,
        guest_name: str,
        size: str,
        *,
        dark_theme: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        guest_name : str
            The guest name, e.g. "Albert"

        size : str
            The desired avatar size, e.g. 64 for 64x64px

        dark_theme : typing.Optional[int]
            Return dark avatar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Custom avatar returned
        """
        with self._raw_client.get_avatar(guest_name, size, dark_theme=dark_theme, request_options=request_options) as r:
            yield from r.data


class AsyncCoreGuestAvatarClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreGuestAvatarClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreGuestAvatarClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreGuestAvatarClient
        """
        return self._raw_client

    async def get_avatar_dark(
        self, guest_name: str, size: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        guest_name : str
            The guest name, e.g. "Albert"

        size : str
            The desired avatar size, e.g. 64 for 64x64px

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Custom avatar returned
        """
        async with self._raw_client.get_avatar_dark(guest_name, size, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_avatar(
        self,
        guest_name: str,
        size: str,
        *,
        dark_theme: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        guest_name : str
            The guest name, e.g. "Albert"

        size : str
            The desired avatar size, e.g. 64 for 64x64px

        dark_theme : typing.Optional[int]
            Return dark avatar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Custom avatar returned
        """
        async with self._raw_client.get_avatar(
            guest_name, size, dark_theme=dark_theme, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
