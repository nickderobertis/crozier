

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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

    def get_benchling_app_manifest(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get app manifest

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apps.get_benchling_app_manifest(
            app_id="app_id",
        )
        """
        _response = self._raw_client.get_benchling_app_manifest(app_id, request_options=request_options)
        return _response.data

    def put_benchling_app_manifest(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Create or update from an app manifest

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apps.put_benchling_app_manifest(
            app_id="app_id",
        )
        """
        _response = self._raw_client.put_benchling_app_manifest(app_id, request_options=request_options)
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

    async def get_benchling_app_manifest(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get app manifest

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apps.get_benchling_app_manifest(
                app_id="app_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_benchling_app_manifest(app_id, request_options=request_options)
        return _response.data

    async def put_benchling_app_manifest(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Create or update from an app manifest

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apps.put_benchling_app_manifest(
                app_id="app_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_benchling_app_manifest(app_id, request_options=request_options)
        return _response.data
