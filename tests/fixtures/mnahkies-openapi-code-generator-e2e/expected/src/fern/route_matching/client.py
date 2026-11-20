

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRouteMatchingClient, RawRouteMatchingClient


class RouteMatchingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRouteMatchingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRouteMatchingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRouteMatchingClient
        """
        return self._raw_client

    def get_by_fixed_field(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.route_matching.get_by_fixed_field()
        """
        _response = self._raw_client.get_by_fixed_field(request_options=request_options)
        return _response.data

    def get_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.route_matching.get_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_by_id(id, request_options=request_options)
        return _response.data


class AsyncRouteMatchingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRouteMatchingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRouteMatchingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRouteMatchingClient
        """
        return self._raw_client

    async def get_by_fixed_field(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.route_matching.get_by_fixed_field()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_fixed_field(request_options=request_options)
        return _response.data

    async def get_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.route_matching.get_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id(id, request_options=request_options)
        return _response.data
