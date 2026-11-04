

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPortraitsClient, RawPortraitsClient


class PortraitsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPortraitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPortraitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPortraitsClient
        """
        return self._raw_client

    def get_portrait(
        self, member_id: str, size: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        member_id : str

        size : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The portrait.
        """
        with self._raw_client.get_portrait(member_id, size, request_options=request_options) as r:
            yield from r.data

    def get_sepia_portrait(
        self, member_id: str, size: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        member_id : str

        size : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The portrait.
        """
        with self._raw_client.get_sepia_portrait(member_id, size, request_options=request_options) as r:
            yield from r.data

    def get_thumbnail(
        self, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        member_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The thumbnail.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.portraits.get_thumbnail(
            member_id="memberId",
        )
        """
        with self._raw_client.get_thumbnail(member_id, request_options=request_options) as r:
            yield from r.data


class AsyncPortraitsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPortraitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPortraitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPortraitsClient
        """
        return self._raw_client

    async def get_portrait(
        self, member_id: str, size: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        member_id : str

        size : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The portrait.
        """
        async with self._raw_client.get_portrait(member_id, size, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_sepia_portrait(
        self, member_id: str, size: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        member_id : str

        size : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The portrait.
        """
        async with self._raw_client.get_sepia_portrait(member_id, size, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_thumbnail(
        self, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        member_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The thumbnail.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.portraits.get_thumbnail(
                member_id="memberId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_thumbnail(member_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
