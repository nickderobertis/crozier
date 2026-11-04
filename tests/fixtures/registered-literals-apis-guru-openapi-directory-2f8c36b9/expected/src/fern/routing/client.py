

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.route import Route
from ..types.routing_file import RoutingFile
from .raw_client import AsyncRawRoutingClient, RawRoutingClient


OMIT = typing.cast(typing.Any, ...)


class RoutingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoutingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoutingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoutingClient
        """
        return self._raw_client

    def get_routing_file(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RoutingFile:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization_id : typing.Optional[str]
            organizationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoutingFile
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.routing.get_routing_file(
            id4n="id4n",
        )
        """
        _response = self._raw_client.get_routing_file(
            id4n, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def update_routing_file(
        self,
        id4n: str,
        *,
        routing: RoutingFile,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id4n : str
            id4n

        routing : RoutingFile

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, Route, RoutingFile

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.routing.update_routing_file(
            id4n="id4n",
            routing=RoutingFile(
                routes=[
                    Route(
                        params={"key": "value"},
                        public=True,
                        type="type",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.update_routing_file(
            id4n, routing=routing, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def get_route(
        self,
        id4n: str,
        type: str,
        *,
        private_routes: typing.Optional[bool] = None,
        public_routes: typing.Optional[bool] = None,
        interpolate: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Route:
        """
        Parameters
        ----------
        id4n : str
            id4n

        type : str
            The type of route you want to have

        private_routes : typing.Optional[bool]
            privateRoutes

        public_routes : typing.Optional[bool]
            publicRoutes

        interpolate : typing.Optional[bool]
            interpolate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Route
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.routing.get_route(
            id4n="id4n",
            type="type",
        )
        """
        _response = self._raw_client.get_route(
            id4n,
            type,
            private_routes=private_routes,
            public_routes=public_routes,
            interpolate=interpolate,
            request_options=request_options,
        )
        return _response.data

    def get_all_routes(
        self,
        id4n: str,
        type: str,
        *,
        organization_id: typing.Optional[str] = None,
        interpolate: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Route]:
        """
        Parameters
        ----------
        id4n : str
            id4n

        type : str
            The type of route you want to have

        organization_id : typing.Optional[str]
            organizationId

        interpolate : typing.Optional[bool]
            interpolate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Route]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.routing.get_all_routes(
            id4n="id4n",
            type="type",
        )
        """
        _response = self._raw_client.get_all_routes(
            id4n, type, organization_id=organization_id, interpolate=interpolate, request_options=request_options
        )
        return _response.data


class AsyncRoutingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoutingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoutingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoutingClient
        """
        return self._raw_client

    async def get_routing_file(
        self,
        id4n: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RoutingFile:
        """
        Parameters
        ----------
        id4n : str
            id4n

        organization_id : typing.Optional[str]
            organizationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoutingFile
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.routing.get_routing_file(
                id4n="id4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_routing_file(
            id4n, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def update_routing_file(
        self,
        id4n: str,
        *,
        routing: RoutingFile,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id4n : str
            id4n

        routing : RoutingFile

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Route, RoutingFile

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.routing.update_routing_file(
                id4n="id4n",
                routing=RoutingFile(
                    routes=[
                        Route(
                            params={"key": "value"},
                            public=True,
                            type="type",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_routing_file(
            id4n, routing=routing, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def get_route(
        self,
        id4n: str,
        type: str,
        *,
        private_routes: typing.Optional[bool] = None,
        public_routes: typing.Optional[bool] = None,
        interpolate: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Route:
        """
        Parameters
        ----------
        id4n : str
            id4n

        type : str
            The type of route you want to have

        private_routes : typing.Optional[bool]
            privateRoutes

        public_routes : typing.Optional[bool]
            publicRoutes

        interpolate : typing.Optional[bool]
            interpolate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Route
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.routing.get_route(
                id4n="id4n",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_route(
            id4n,
            type,
            private_routes=private_routes,
            public_routes=public_routes,
            interpolate=interpolate,
            request_options=request_options,
        )
        return _response.data

    async def get_all_routes(
        self,
        id4n: str,
        type: str,
        *,
        organization_id: typing.Optional[str] = None,
        interpolate: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Route]:
        """
        Parameters
        ----------
        id4n : str
            id4n

        type : str
            The type of route you want to have

        organization_id : typing.Optional[str]
            organizationId

        interpolate : typing.Optional[bool]
            interpolate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Route]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.routing.get_all_routes(
                id4n="id4n",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_routes(
            id4n, type, organization_id=organization_id, interpolate=interpolate, request_options=request_options
        )
        return _response.data
