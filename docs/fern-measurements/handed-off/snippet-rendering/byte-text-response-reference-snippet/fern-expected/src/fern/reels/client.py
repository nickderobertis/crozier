

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawReelsClient, RawReelsClient


OMIT = typing.cast(typing.Any, ...)


class ReelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReelsClient
        """
        return self._raw_client

    def develop_reel(
        self, reel_id: str, pass_: int, *, scan: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        reel_id : str

        pass_ : int

        scan : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The developing log.
        """
        with self._raw_client.develop_reel(reel_id, pass_, scan=scan, request_options=request_options) as r:
            yield from r.data

    def annotate_reel(
        self, reel_id: str, *, notes: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        reel_id : str

        notes : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The stored notes' text.
        """
        _response = self._raw_client.annotate_reel(reel_id, notes=notes, request_options=request_options)
        return _response.data

    def get_reel_log(
        self,
        reel_id: str,
        *,
        tail: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        reel_id : str

        tail : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The developing log.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reels.get_reel_log(
            reel_id="reelId",
        )
        """
        with self._raw_client.get_reel_log(reel_id, tail=tail, request_options=request_options) as r:
            yield from r.data


class AsyncReelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReelsClient
        """
        return self._raw_client

    async def develop_reel(
        self, reel_id: str, pass_: int, *, scan: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        reel_id : str

        pass_ : int

        scan : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The developing log.
        """
        async with self._raw_client.develop_reel(reel_id, pass_, scan=scan, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def annotate_reel(
        self, reel_id: str, *, notes: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        reel_id : str

        notes : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The stored notes' text.
        """
        _response = await self._raw_client.annotate_reel(reel_id, notes=notes, request_options=request_options)
        return _response.data

    async def get_reel_log(
        self,
        reel_id: str,
        *,
        tail: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        reel_id : str

        tail : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The developing log.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reels.get_reel_log(
                reel_id="reelId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_reel_log(reel_id, tail=tail, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
