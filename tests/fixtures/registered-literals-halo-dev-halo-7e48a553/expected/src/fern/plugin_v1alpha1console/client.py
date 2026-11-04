

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_map import ConfigMap
from ..types.plugin import Plugin
from ..types.plugin_list import PluginList
from ..types.setting import Setting
from .raw_client import AsyncRawPluginV1Alpha1ConsoleClient, RawPluginV1Alpha1ConsoleClient
from .types.install_plugin_request_source import InstallPluginRequestSource
from .types.upgrade_plugin_request_source import UpgradePluginRequestSource


OMIT = typing.cast(typing.Any, ...)


class PluginV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPluginV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPluginV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPluginV1Alpha1ConsoleClient
        """
        return self._raw_client

    def list_plugins(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PluginList:
        """
        List plugins using query criteria and sort params

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword of plugin display name or description

        enabled : typing.Optional[bool]
            Whether the plugin is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PluginList
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.list_plugins()
        """
        _response = self._raw_client.list_plugins(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            keyword=keyword,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def fetch_css_bundle(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Compatibility alias for the UI plugin CSS bundle.

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
        client.plugin_v1alpha1console.fetch_css_bundle()
        """
        _response = self._raw_client.fetch_css_bundle(request_options=request_options)
        return _response.data

    def fetch_js_bundle(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Compatibility alias for the UI plugin JS bundle.

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
        client.plugin_v1alpha1console.fetch_js_bundle()
        """
        _response = self._raw_client.fetch_js_bundle(request_options=request_options)
        return _response.data

    def install_plugin_from_uri(self, *, uri: str, request_options: typing.Optional[RequestOptions] = None) -> Plugin:
        """
        Install a plugin from uri.

        Parameters
        ----------
        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.install_plugin_from_uri(
            uri="uri",
        )
        """
        _response = self._raw_client.install_plugin_from_uri(uri=uri, request_options=request_options)
        return _response.data

    def install_plugin(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        preset_name: typing.Optional[str] = OMIT,
        source: typing.Optional[InstallPluginRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Plugin:
        """
        Install a plugin by uploading a Jar file.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        preset_name : typing.Optional[str]
            Plugin preset name. Halo finds the plugin from plugin presets.

        source : typing.Optional[InstallPluginRequestSource]
            Install source. Defaults to file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.install_plugin()
        """
        _response = self._raw_client.install_plugin(
            file=file, preset_name=preset_name, source=source, request_options=request_options
        )
        return _response.data

    def fetch_plugin_json_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Fetch converted json config of plugin by configured configMapName.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose JSON config will be fetched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.fetch_plugin_json_config(
            name="name",
        )
        """
        _response = self._raw_client.fetch_plugin_json_config(name, request_options=request_options)
        return _response.data

    def update_plugin_json_config(
        self,
        name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the config of plugin setting.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose JSON config will be updated.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.update_plugin_json_config(
            name="name",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_plugin_json_config(name, request=request, request_options=request_options)
        return _response.data

    def change_plugin_running_state(
        self,
        name: str,
        *,
        enable: bool,
        async_: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Plugin:
        """
        Change the running state of a plugin by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose running state will be changed.

        enable : bool
            Whether the plugin should be enabled.

        async_ : typing.Optional[bool]
            Whether to change the state asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.change_plugin_running_state(
            name="name",
            enable=True,
        )
        """
        _response = self._raw_client.change_plugin_running_state(
            name, enable=enable, async_=async_, request_options=request_options
        )
        return _response.data

    def reload_plugin(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Plugin:
        """
        Reload a plugin by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of the plugin to reload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.reload_plugin(
            name="name",
        )
        """
        _response = self._raw_client.reload_plugin(name, request_options=request_options)
        return _response.data

    def reset_plugin_config(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ConfigMap:
        """
        Reset the configMap of plugin setting.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose setting config will be reset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigMap
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.reset_plugin_config(
            name="name",
        )
        """
        _response = self._raw_client.reset_plugin_config(name, request_options=request_options)
        return _response.data

    def fetch_plugin_setting(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Setting:
        """
        Fetch setting of plugin.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose setting will be fetched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Setting
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.fetch_plugin_setting(
            name="name",
        )
        """
        _response = self._raw_client.fetch_plugin_setting(name, request_options=request_options)
        return _response.data

    def upgrade_plugin(
        self,
        name: str,
        *,
        file: typing.Optional[core.File] = OMIT,
        preset_name: typing.Optional[str] = OMIT,
        source: typing.Optional[UpgradePluginRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Plugin:
        """
        Upgrade a plugin by uploading a Jar file

        Parameters
        ----------
        name : str
            metadata.name of the plugin to upgrade.

        file : typing.Optional[core.File]
            See core.File for more documentation

        preset_name : typing.Optional[str]
            Plugin preset name. Halo finds the plugin from plugin presets.

        source : typing.Optional[UpgradePluginRequestSource]
            Install source. Defaults to file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.upgrade_plugin(
            name="name",
        )
        """
        _response = self._raw_client.upgrade_plugin(
            name, file=file, preset_name=preset_name, source=source, request_options=request_options
        )
        return _response.data

    def upgrade_plugin_from_uri(
        self, name: str, *, uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Plugin:
        """
        Upgrade a plugin from uri.

        Parameters
        ----------
        name : str
            metadata.name of the plugin to upgrade.

        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin_v1alpha1console.upgrade_plugin_from_uri(
            name="name",
            uri="uri",
        )
        """
        _response = self._raw_client.upgrade_plugin_from_uri(name, uri=uri, request_options=request_options)
        return _response.data


class AsyncPluginV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPluginV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPluginV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPluginV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def list_plugins(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PluginList:
        """
        List plugins using query criteria and sort params

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword of plugin display name or description

        enabled : typing.Optional[bool]
            Whether the plugin is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PluginList
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
            await client.plugin_v1alpha1console.list_plugins()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_plugins(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            keyword=keyword,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def fetch_css_bundle(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Compatibility alias for the UI plugin CSS bundle.

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
            await client.plugin_v1alpha1console.fetch_css_bundle()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_css_bundle(request_options=request_options)
        return _response.data

    async def fetch_js_bundle(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Compatibility alias for the UI plugin JS bundle.

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
            await client.plugin_v1alpha1console.fetch_js_bundle()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_js_bundle(request_options=request_options)
        return _response.data

    async def install_plugin_from_uri(
        self, *, uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Plugin:
        """
        Install a plugin from uri.

        Parameters
        ----------
        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
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
            await client.plugin_v1alpha1console.install_plugin_from_uri(
                uri="uri",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.install_plugin_from_uri(uri=uri, request_options=request_options)
        return _response.data

    async def install_plugin(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        preset_name: typing.Optional[str] = OMIT,
        source: typing.Optional[InstallPluginRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Plugin:
        """
        Install a plugin by uploading a Jar file.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        preset_name : typing.Optional[str]
            Plugin preset name. Halo finds the plugin from plugin presets.

        source : typing.Optional[InstallPluginRequestSource]
            Install source. Defaults to file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
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
            await client.plugin_v1alpha1console.install_plugin()


        asyncio.run(main())
        """
        _response = await self._raw_client.install_plugin(
            file=file, preset_name=preset_name, source=source, request_options=request_options
        )
        return _response.data

    async def fetch_plugin_json_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Fetch converted json config of plugin by configured configMapName.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose JSON config will be fetched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.plugin_v1alpha1console.fetch_plugin_json_config(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_plugin_json_config(name, request_options=request_options)
        return _response.data

    async def update_plugin_json_config(
        self,
        name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the config of plugin setting.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose JSON config will be updated.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.plugin_v1alpha1console.update_plugin_json_config(
                name="name",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_plugin_json_config(
            name, request=request, request_options=request_options
        )
        return _response.data

    async def change_plugin_running_state(
        self,
        name: str,
        *,
        enable: bool,
        async_: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Plugin:
        """
        Change the running state of a plugin by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose running state will be changed.

        enable : bool
            Whether the plugin should be enabled.

        async_ : typing.Optional[bool]
            Whether to change the state asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
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
            await client.plugin_v1alpha1console.change_plugin_running_state(
                name="name",
                enable=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_plugin_running_state(
            name, enable=enable, async_=async_, request_options=request_options
        )
        return _response.data

    async def reload_plugin(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Plugin:
        """
        Reload a plugin by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of the plugin to reload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
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
            await client.plugin_v1alpha1console.reload_plugin(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reload_plugin(name, request_options=request_options)
        return _response.data

    async def reset_plugin_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigMap:
        """
        Reset the configMap of plugin setting.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose setting config will be reset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigMap
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
            await client.plugin_v1alpha1console.reset_plugin_config(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_plugin_config(name, request_options=request_options)
        return _response.data

    async def fetch_plugin_setting(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Setting:
        """
        Fetch setting of plugin.

        Parameters
        ----------
        name : str
            metadata.name of the plugin whose setting will be fetched.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Setting
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
            await client.plugin_v1alpha1console.fetch_plugin_setting(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_plugin_setting(name, request_options=request_options)
        return _response.data

    async def upgrade_plugin(
        self,
        name: str,
        *,
        file: typing.Optional[core.File] = OMIT,
        preset_name: typing.Optional[str] = OMIT,
        source: typing.Optional[UpgradePluginRequestSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Plugin:
        """
        Upgrade a plugin by uploading a Jar file

        Parameters
        ----------
        name : str
            metadata.name of the plugin to upgrade.

        file : typing.Optional[core.File]
            See core.File for more documentation

        preset_name : typing.Optional[str]
            Plugin preset name. Halo finds the plugin from plugin presets.

        source : typing.Optional[UpgradePluginRequestSource]
            Install source. Defaults to file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
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
            await client.plugin_v1alpha1console.upgrade_plugin(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upgrade_plugin(
            name, file=file, preset_name=preset_name, source=source, request_options=request_options
        )
        return _response.data

    async def upgrade_plugin_from_uri(
        self, name: str, *, uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Plugin:
        """
        Upgrade a plugin from uri.

        Parameters
        ----------
        name : str
            metadata.name of the plugin to upgrade.

        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plugin
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
            await client.plugin_v1alpha1console.upgrade_plugin_from_uri(
                name="name",
                uri="uri",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upgrade_plugin_from_uri(name, uri=uri, request_options=request_options)
        return _response.data
