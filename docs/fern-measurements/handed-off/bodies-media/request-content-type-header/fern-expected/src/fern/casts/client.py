

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cast_order import CastOrder
from ..types.recast_order import RecastOrder
from .raw_client import AsyncRawCastsClient, RawCastsClient


OMIT = typing.cast(typing.Any, ...)


class CastsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCastsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCastsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCastsClient
        """
        return self._raw_client

    def order_cast(self, *, request: CastOrder, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : CastOrder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import CastOrder_Bell, FernApi

        client = FernApi()
        client.casts.order_cast(
            request=CastOrder_Bell(
                weight_kg=1.1,
            ),
        )
        """
        _response = self._raw_client.order_cast(request=request, request_options=request_options)
        return _response.data

    def order_recast(self, *, request: RecastOrder, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : RecastOrder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, RecastOrder_Bell

        client = FernApi()
        client.casts.order_recast(
            request=RecastOrder_Bell(
                weight_kg=1.1,
            ),
        )
        """
        _response = self._raw_client.order_recast(request=request, request_options=request_options)
        return _response.data


class AsyncCastsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCastsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCastsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCastsClient
        """
        return self._raw_client

    async def order_cast(self, *, request: CastOrder, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : CastOrder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CastOrder_Bell

        client = AsyncFernApi()


        async def main() -> None:
            await client.casts.order_cast(
                request=CastOrder_Bell(
                    weight_kg=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.order_cast(request=request, request_options=request_options)
        return _response.data

    async def order_recast(
        self, *, request: RecastOrder, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : RecastOrder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RecastOrder_Bell

        client = AsyncFernApi()


        async def main() -> None:
            await client.casts.order_recast(
                request=RecastOrder_Bell(
                    weight_kg=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.order_recast(request=request, request_options=request_options)
        return _response.data
