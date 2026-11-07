

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_navigation_get_apps_navigation200response import CoreNavigationGetAppsNavigation200Response
from .raw_client import AsyncRawCoreNavigationClient, RawCoreNavigationClient


class CoreNavigationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreNavigationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreNavigationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreNavigationClient
        """
        return self._raw_client

    def get_apps_navigation(
        self, *, absolute: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreNavigationGetAppsNavigation200Response:
        """
        Parameters
        ----------
        absolute : typing.Optional[int]
            Rewrite URLs to absolute ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreNavigationGetAppsNavigation200Response
            Apps navigation returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_navigation.get_apps_navigation()
        """
        _response = self._raw_client.get_apps_navigation(absolute=absolute, request_options=request_options)
        return _response.data

    def get_settings_navigation(
        self, *, absolute: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreNavigationGetAppsNavigation200Response:
        """
        Parameters
        ----------
        absolute : typing.Optional[int]
            Rewrite URLs to absolute ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreNavigationGetAppsNavigation200Response
            Apps navigation returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_navigation.get_settings_navigation()
        """
        _response = self._raw_client.get_settings_navigation(absolute=absolute, request_options=request_options)
        return _response.data


class AsyncCoreNavigationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreNavigationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreNavigationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreNavigationClient
        """
        return self._raw_client

    async def get_apps_navigation(
        self, *, absolute: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreNavigationGetAppsNavigation200Response:
        """
        Parameters
        ----------
        absolute : typing.Optional[int]
            Rewrite URLs to absolute ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreNavigationGetAppsNavigation200Response
            Apps navigation returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_navigation.get_apps_navigation()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_apps_navigation(absolute=absolute, request_options=request_options)
        return _response.data

    async def get_settings_navigation(
        self, *, absolute: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreNavigationGetAppsNavigation200Response:
        """
        Parameters
        ----------
        absolute : typing.Optional[int]
            Rewrite URLs to absolute ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreNavigationGetAppsNavigation200Response
            Apps navigation returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_navigation.get_settings_navigation()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_settings_navigation(absolute=absolute, request_options=request_options)
        return _response.data
