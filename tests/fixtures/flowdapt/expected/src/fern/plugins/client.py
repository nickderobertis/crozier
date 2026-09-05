

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1alpha1plugin import V1Alpha1Plugin
from ..types.v1alpha1plugin_files import V1Alpha1PluginFiles
from .raw_client import AsyncRawPluginsClient, RawPluginsClient


class PluginsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPluginsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPluginsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPluginsClient
        """
        return self._raw_client

    def get_plugin(
        self, plugin_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1Plugin:
        """
        Parameters
        ----------
        plugin_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1Plugin
            Plugin info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugins.get_plugin(
            plugin_name="plugin_name",
        )
        """
        _response = self._raw_client.get_plugin(plugin_name, request_options=request_options)
        return _response.data

    def list_plugins(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[V1Alpha1Plugin]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Alpha1Plugin]
            List of Plugins

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugins.list_plugins()
        """
        _response = self._raw_client.list_plugins(request_options=request_options)
        return _response.data

    def list_plugin_files(
        self, plugin_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1PluginFiles:
        """
        Parameters
        ----------
        plugin_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1PluginFiles
            List of files

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugins.list_plugin_files(
            plugin_name="plugin_name",
        )
        """
        _response = self._raw_client.list_plugin_files(plugin_name, request_options=request_options)
        return _response.data

    def get_plugin_file(
        self, plugin_name: str, file_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        plugin_name : str

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The file requested

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.plugins.get_plugin_file(
            plugin_name="plugin_name",
            file_name="file_name",
        )
        """
        with self._raw_client.get_plugin_file(plugin_name, file_name, request_options=request_options) as r:
            yield from r.data


class AsyncPluginsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPluginsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPluginsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPluginsClient
        """
        return self._raw_client

    async def get_plugin(
        self, plugin_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1Plugin:
        """
        Parameters
        ----------
        plugin_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1Plugin
            Plugin info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugins.get_plugin(
                plugin_name="plugin_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_plugin(plugin_name, request_options=request_options)
        return _response.data

    async def list_plugins(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Alpha1Plugin]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Alpha1Plugin]
            List of Plugins

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugins.list_plugins()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_plugins(request_options=request_options)
        return _response.data

    async def list_plugin_files(
        self, plugin_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1PluginFiles:
        """
        Parameters
        ----------
        plugin_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1PluginFiles
            List of files

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugins.list_plugin_files(
                plugin_name="plugin_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_plugin_files(plugin_name, request_options=request_options)
        return _response.data

    async def get_plugin_file(
        self, plugin_name: str, file_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        plugin_name : str

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The file requested

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plugins.get_plugin_file(
                plugin_name="plugin_name",
                file_name="file_name",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_plugin_file(plugin_name, file_name, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
