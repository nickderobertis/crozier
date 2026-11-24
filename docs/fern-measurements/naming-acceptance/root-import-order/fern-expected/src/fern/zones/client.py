

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawZonesClient, RawZonesClient
from .types.list_zones_request_kind import ListZonesRequestKind


class ZonesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawZonesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawZonesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawZonesClient
        """
        return self._raw_client

    def list_zones(
        self,
        *,
        kind: typing.Optional[ListZonesRequestKind] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        kind : typing.Optional[ListZonesRequestKind]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The zones.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.zones.list_zones()
        """
        _response = self._raw_client.list_zones(kind=kind, request_options=request_options)
        return _response.data


class AsyncZonesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawZonesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawZonesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawZonesClient
        """
        return self._raw_client

    async def list_zones(
        self,
        *,
        kind: typing.Optional[ListZonesRequestKind] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        kind : typing.Optional[ListZonesRequestKind]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The zones.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.zones.list_zones()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_zones(kind=kind, request_options=request_options)
        return _response.data
