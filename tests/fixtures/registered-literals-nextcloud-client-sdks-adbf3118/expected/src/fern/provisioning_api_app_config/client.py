

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from ..types.provisioning_api_app_config_get_apps200response import ProvisioningApiAppConfigGetApps200Response
from ..types.provisioning_api_app_config_get_value200response import ProvisioningApiAppConfigGetValue200Response
from .raw_client import AsyncRawProvisioningApiAppConfigClient, RawProvisioningApiAppConfigClient


class ProvisioningApiAppConfigClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProvisioningApiAppConfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProvisioningApiAppConfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProvisioningApiAppConfigClient
        """
        return self._raw_client

    def get_apps(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiAppConfigGetApps200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiAppConfigGetApps200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_app_config.get_apps()
        """
        _response = self._raw_client.get_apps(request_options=request_options)
        return _response.data

    def get_keys(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiAppConfigGetApps200Response:
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
        ProvisioningApiAppConfigGetApps200Response
            Keys returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_app_config.get_keys(
            app="app",
        )
        """
        _response = self._raw_client.get_keys(app, request_options=request_options)
        return _response.data

    def get_value(
        self,
        app: str,
        key: str,
        *,
        default_value: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiAppConfigGetValue200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID if the app

        key : str
            Key

        default_value : typing.Optional[str]
            Default returned value if the value is empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiAppConfigGetValue200Response
            Value returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_app_config.get_value(
            app="app",
            key="key",
        )
        """
        _response = self._raw_client.get_value(app, key, default_value=default_value, request_options=request_options)
        return _response.data

    def set_value(
        self, app: str, key: str, *, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        app : str
            ID of the app

        key : str
            Key to update

        value : str
            New value for the key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Value updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_app_config.set_value(
            app="app",
            key="key",
            value="value",
        )
        """
        _response = self._raw_client.set_value(app, key, value=value, request_options=request_options)
        return _response.data

    def delete_key(
        self, app: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        key : str
            Key to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Key deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_app_config.delete_key(
            app="app",
            key="key",
        )
        """
        _response = self._raw_client.delete_key(app, key, request_options=request_options)
        return _response.data


class AsyncProvisioningApiAppConfigClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProvisioningApiAppConfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProvisioningApiAppConfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProvisioningApiAppConfigClient
        """
        return self._raw_client

    async def get_apps(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiAppConfigGetApps200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiAppConfigGetApps200Response


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
            await client.provisioning_api_app_config.get_apps()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_apps(request_options=request_options)
        return _response.data

    async def get_keys(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiAppConfigGetApps200Response:
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
        ProvisioningApiAppConfigGetApps200Response
            Keys returned

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
            await client.provisioning_api_app_config.get_keys(
                app="app",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_keys(app, request_options=request_options)
        return _response.data

    async def get_value(
        self,
        app: str,
        key: str,
        *,
        default_value: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiAppConfigGetValue200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID if the app

        key : str
            Key

        default_value : typing.Optional[str]
            Default returned value if the value is empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiAppConfigGetValue200Response
            Value returned

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
            await client.provisioning_api_app_config.get_value(
                app="app",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_value(
            app, key, default_value=default_value, request_options=request_options
        )
        return _response.data

    async def set_value(
        self, app: str, key: str, *, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        app : str
            ID of the app

        key : str
            Key to update

        value : str
            New value for the key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Value updated successfully

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
            await client.provisioning_api_app_config.set_value(
                app="app",
                key="key",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_value(app, key, value=value, request_options=request_options)
        return _response.data

    async def delete_key(
        self, app: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        key : str
            Key to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Key deleted successfully

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
            await client.provisioning_api_app_config.delete_key(
                app="app",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_key(app, key, request_options=request_options)
        return _response.data
