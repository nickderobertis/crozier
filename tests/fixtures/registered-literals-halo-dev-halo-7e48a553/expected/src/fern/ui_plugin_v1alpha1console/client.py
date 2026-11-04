

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ui_plugin_provider_descriptor import UiPluginProviderDescriptor
from .raw_client import AsyncRawUiPluginV1Alpha1ConsoleClient, RawUiPluginV1Alpha1ConsoleClient


class UiPluginV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUiPluginV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUiPluginV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUiPluginV1Alpha1ConsoleClient
        """
        return self._raw_client

    def fetch_ui_plugin_css_bundle(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Merge CSS bundles of enabled plugins and the activated theme into one.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ui_plugin_v1alpha1console.fetch_ui_plugin_css_bundle()
        """
        _response = self._raw_client.fetch_ui_plugin_css_bundle(request_options=request_options)
        return _response.data

    def fetch_ui_plugin_js_bundle(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Merge JS bundles of enabled plugins and the activated theme into one.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ui_plugin_v1alpha1console.fetch_ui_plugin_js_bundle()
        """
        _response = self._raw_client.fetch_ui_plugin_js_bundle(request_options=request_options)
        return _response.data

    def fetch_ui_plugin_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UiPluginProviderDescriptor:
        """
        Fetch the currently enabled UI provider descriptor.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UiPluginProviderDescriptor
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ui_plugin_v1alpha1console.fetch_ui_plugin_providers()
        """
        _response = self._raw_client.fetch_ui_plugin_providers(request_options=request_options)
        return _response.data


class AsyncUiPluginV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUiPluginV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUiPluginV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUiPluginV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def fetch_ui_plugin_css_bundle(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Merge CSS bundles of enabled plugins and the activated theme into one.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.ui_plugin_v1alpha1console.fetch_ui_plugin_css_bundle()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_ui_plugin_css_bundle(request_options=request_options)
        return _response.data

    async def fetch_ui_plugin_js_bundle(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Merge JS bundles of enabled plugins and the activated theme into one.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.ui_plugin_v1alpha1console.fetch_ui_plugin_js_bundle()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_ui_plugin_js_bundle(request_options=request_options)
        return _response.data

    async def fetch_ui_plugin_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UiPluginProviderDescriptor:
        """
        Fetch the currently enabled UI provider descriptor.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UiPluginProviderDescriptor
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.ui_plugin_v1alpha1console.fetch_ui_plugin_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_ui_plugin_providers(request_options=request_options)
        return _response.data
