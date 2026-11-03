

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRoutesClient, RawRoutesClient
from .types.plan_routes_response import PlanRoutesResponse


OMIT = typing.cast(typing.Any, ...)


class RoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoutesClient
        """
        return self._raw_client

    def plan_routes(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> PlanRoutesResponse:
        """
        An array body's schema-level example.

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlanRoutesResponse
            Planned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.routes.plan_routes(
            request=["Mount's Bay", "Carrick Roads"],
        )
        """
        _response = self._raw_client.plan_routes(request=request, request_options=request_options)
        return _response.data


class AsyncRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoutesClient
        """
        return self._raw_client

    async def plan_routes(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> PlanRoutesResponse:
        """
        An array body's schema-level example.

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlanRoutesResponse
            Planned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.routes.plan_routes(
                request=["Mount's Bay", "Carrick Roads"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.plan_routes(request=request, request_options=request_options)
        return _response.data
