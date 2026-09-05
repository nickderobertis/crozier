

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.endpoint_get_apps import EndpointGetApps
from ..types.endpoint_get_apps_id import EndpointGetAppsId
from .raw_client import AsyncRawAppsClient, RawAppsClient


class AppsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppsClient
        """
        return self._raw_client

    def get_apps(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetApps:
        """
        Fetch all Daniapps that are currently in production mode.

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetApps
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.apps.get_apps()
        """
        _response = self._raw_client.get_apps(offset=offset, limit=limit, request_options=request_options)
        return _response.data

    def get_apps_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetAppsId:
        """
        Fetch an array of Daniapps that are currently in production mode.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetAppsId
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.apps.get_apps_id(
            id="ID",
        )
        """
        _response = self._raw_client.get_apps_id(id, request_options=request_options)
        return _response.data


class AsyncAppsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppsClient
        """
        return self._raw_client

    async def get_apps(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetApps:
        """
        Fetch all Daniapps that are currently in production mode.

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetApps
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.apps.get_apps()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_apps(offset=offset, limit=limit, request_options=request_options)
        return _response.data

    async def get_apps_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetAppsId:
        """
        Fetch an array of Daniapps that are currently in production mode.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetAppsId
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.apps.get_apps_id(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_apps_id(id, request_options=request_options)
        return _response.data
