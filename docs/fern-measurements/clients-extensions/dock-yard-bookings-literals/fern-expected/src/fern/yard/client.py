

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawYardClient, RawYardClient
from .types.book_yard_request_slot import BookYardRequestSlot

if typing.TYPE_CHECKING:
    from .cranes.client import AsyncCranesClient, CranesClient

OMIT = typing.cast(typing.Any, ...)


class YardClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawYardClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._cranes: typing.Optional[CranesClient] = None

    @property
    def with_raw_response(self) -> RawYardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawYardClient
        """
        return self._raw_client

    def book(
        self,
        *,
        slot: BookYardRequestSlot,
        vessel: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        slot : BookYardRequestSlot

        vessel : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.yard.book(
            slot="morning",
        )
        """
        _response = self._raw_client.book(slot=slot, vessel=vessel, request_options=request_options)
        return _response.data

    @property
    def cranes(self):
        if self._cranes is None:
            from .cranes.client import CranesClient

            self._cranes = CranesClient(client_wrapper=self._client_wrapper)
        return self._cranes


class AsyncYardClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawYardClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._cranes: typing.Optional[AsyncCranesClient] = None

    @property
    def with_raw_response(self) -> AsyncRawYardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawYardClient
        """
        return self._raw_client

    async def book(
        self,
        *,
        slot: BookYardRequestSlot,
        vessel: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        slot : BookYardRequestSlot

        vessel : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.yard.book(
                slot="morning",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.book(slot=slot, vessel=vessel, request_options=request_options)
        return _response.data

    @property
    def cranes(self):
        if self._cranes is None:
            from .cranes.client import AsyncCranesClient

            self._cranes = AsyncCranesClient(client_wrapper=self._client_wrapper)
        return self._cranes
