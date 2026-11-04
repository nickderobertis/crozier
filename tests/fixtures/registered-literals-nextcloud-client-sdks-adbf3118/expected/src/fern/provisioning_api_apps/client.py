

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from ..types.provisioning_api_apps_get_app_info200response import ProvisioningApiAppsGetAppInfo200Response
from ..types.provisioning_api_apps_get_apps200response import ProvisioningApiAppsGetApps200Response
from .raw_client import AsyncRawProvisioningApiAppsClient, RawProvisioningApiAppsClient


class ProvisioningApiAppsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProvisioningApiAppsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProvisioningApiAppsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProvisioningApiAppsClient
        """
        return self._raw_client

    def get_apps(
        self, *, filter: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiAppsGetApps200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        filter : typing.Optional[str]
            Filter for enabled or disabled apps

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiAppsGetApps200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_apps.get_apps()
        """
        _response = self._raw_client.get_apps(filter=filter, request_options=request_options)
        return _response.data

    def get_app_info(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiAppsGetAppInfo200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiAppsGetAppInfo200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_apps.get_app_info(
            app="app",
        )
        """
        _response = self._raw_client.get_app_info(app, request_options=request_options)
        return _response.data

    def enable(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_apps.enable(
            app="app",
        )
        """
        _response = self._raw_client.enable(app, request_options=request_options)
        return _response.data

    def disable(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_apps.disable(
            app="app",
        )
        """
        _response = self._raw_client.disable(app, request_options=request_options)
        return _response.data


class AsyncProvisioningApiAppsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProvisioningApiAppsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProvisioningApiAppsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProvisioningApiAppsClient
        """
        return self._raw_client

    async def get_apps(
        self, *, filter: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiAppsGetApps200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        filter : typing.Optional[str]
            Filter for enabled or disabled apps

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiAppsGetApps200Response


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
            await client.provisioning_api_apps.get_apps()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_apps(filter=filter, request_options=request_options)
        return _response.data

    async def get_app_info(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiAppsGetAppInfo200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiAppsGetAppInfo200Response


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
            await client.provisioning_api_apps.get_app_info(
                app="app",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_app_info(app, request_options=request_options)
        return _response.data

    async def enable(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


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
            await client.provisioning_api_apps.enable(
                app="app",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable(app, request_options=request_options)
        return _response.data

    async def disable(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


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
            await client.provisioning_api_apps.disable(
                app="app",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable(app, request_options=request_options)
        return _response.data
