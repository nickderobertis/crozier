

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from .raw_client import AsyncRawProvisioningApiPreferencesClient, RawProvisioningApiPreferencesClient


class ProvisioningApiPreferencesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProvisioningApiPreferencesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProvisioningApiPreferencesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProvisioningApiPreferencesClient
        """
        return self._raw_client

    def set_preference(
        self,
        app_id: str,
        config_key: str,
        *,
        config_value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        app_id : str
            ID of the app

        config_key : str
            Key of the preference

        config_value : str
            New value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Preference updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_preferences.set_preference(
            app_id="appId",
            config_key="configKey",
            config_value="configValue",
        )
        """
        _response = self._raw_client.set_preference(
            app_id, config_key, config_value=config_value, request_options=request_options
        )
        return _response.data

    def delete_preference(
        self, app_id: str, config_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        app_id : str
            ID of the app

        config_key : str
            Key to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Preference deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_preferences.delete_preference(
            app_id="appId",
            config_key="configKey",
        )
        """
        _response = self._raw_client.delete_preference(app_id, config_key, request_options=request_options)
        return _response.data

    def set_multiple_preferences(
        self, app_id: str, *, configs: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        app_id : str
            ID of the app

        configs : str
            Key-value pairs of the preferences

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Preferences updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_preferences.set_multiple_preferences(
            app_id="appId",
            configs="configs",
        )
        """
        _response = self._raw_client.set_multiple_preferences(app_id, configs=configs, request_options=request_options)
        return _response.data

    def delete_multiple_preference(
        self, app_id: str, *, config_keys: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        app_id : str
            ID of the app

        config_keys : str
            Keys to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Preferences deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_preferences.delete_multiple_preference(
            app_id="appId",
            config_keys="configKeys",
        )
        """
        _response = self._raw_client.delete_multiple_preference(
            app_id, config_keys=config_keys, request_options=request_options
        )
        return _response.data


class AsyncProvisioningApiPreferencesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProvisioningApiPreferencesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProvisioningApiPreferencesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProvisioningApiPreferencesClient
        """
        return self._raw_client

    async def set_preference(
        self,
        app_id: str,
        config_key: str,
        *,
        config_value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        app_id : str
            ID of the app

        config_key : str
            Key of the preference

        config_value : str
            New value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Preference updated successfully

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
            await client.provisioning_api_preferences.set_preference(
                app_id="appId",
                config_key="configKey",
                config_value="configValue",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_preference(
            app_id, config_key, config_value=config_value, request_options=request_options
        )
        return _response.data

    async def delete_preference(
        self, app_id: str, config_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        app_id : str
            ID of the app

        config_key : str
            Key to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Preference deleted successfully

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
            await client.provisioning_api_preferences.delete_preference(
                app_id="appId",
                config_key="configKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_preference(app_id, config_key, request_options=request_options)
        return _response.data

    async def set_multiple_preferences(
        self, app_id: str, *, configs: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        app_id : str
            ID of the app

        configs : str
            Key-value pairs of the preferences

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Preferences updated successfully

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
            await client.provisioning_api_preferences.set_multiple_preferences(
                app_id="appId",
                configs="configs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_multiple_preferences(
            app_id, configs=configs, request_options=request_options
        )
        return _response.data

    async def delete_multiple_preference(
        self, app_id: str, *, config_keys: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        app_id : str
            ID of the app

        config_keys : str
            Keys to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Preferences deleted successfully

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
            await client.provisioning_api_preferences.delete_multiple_preference(
                app_id="appId",
                config_keys="configKeys",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_multiple_preference(
            app_id, config_keys=config_keys, request_options=request_options
        )
        return _response.data
