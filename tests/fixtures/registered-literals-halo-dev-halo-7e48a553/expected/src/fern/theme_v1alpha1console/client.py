

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_map import ConfigMap
from ..types.setting import Setting
from ..types.theme import Theme
from ..types.theme_list import ThemeList
from .raw_client import AsyncRawThemeV1Alpha1ConsoleClient, RawThemeV1Alpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class ThemeV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawThemeV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawThemeV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawThemeV1Alpha1ConsoleClient
        """
        return self._raw_client

    def list_themes(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        uninstalled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThemeList:
        """
        List themes.

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

        uninstalled : typing.Optional[bool]
            Whether to list uninstalled themes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThemeList
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theme_v1alpha1console.list_themes()
        """
        _response = self._raw_client.list_themes(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            uninstalled=uninstalled,
            request_options=request_options,
        )
        return _response.data

    def fetch_activated_theme(self, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Fetch the activated theme.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theme_v1alpha1console.fetch_activated_theme()
        """
        _response = self._raw_client.fetch_activated_theme(request_options=request_options)
        return _response.data

    def install_theme_from_uri(self, *, uri: str, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Install a theme from uri.

        Parameters
        ----------
        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theme_v1alpha1console.install_theme_from_uri(
            uri="uri",
        )
        """
        _response = self._raw_client.install_theme_from_uri(uri=uri, request_options=request_options)
        return _response.data

    def install_theme(self, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Install a theme by uploading a zip file.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theme_v1alpha1console.install_theme()
        """
        _response = self._raw_client.install_theme(request_options=request_options)
        return _response.data

    def activate_theme(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Activate a theme by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of the theme to activate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theme_v1alpha1console.activate_theme(
            name="name",
        )
        """
        _response = self._raw_client.activate_theme(name, request_options=request_options)
        return _response.data

    def invalidate_cache(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidate theme template cache.

        Parameters
        ----------
        name : str
            metadata.name of the theme whose template cache will be invalidated.

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
        client.theme_v1alpha1console.invalidate_cache(
            name="name",
        )
        """
        _response = self._raw_client.invalidate_cache(name, request_options=request_options)
        return _response.data

    def fetch_theme_json_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Fetch converted json config of theme by configured configMapName.

        Parameters
        ----------
        name : str
            metadata.name of the theme whose JSON config will be fetched.

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
        client.theme_v1alpha1console.fetch_theme_json_config(
            name="name",
        )
        """
        _response = self._raw_client.fetch_theme_json_config(name, request_options=request_options)
        return _response.data

    def update_theme_json_config(
        self,
        name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the configMap of theme setting.

        Parameters
        ----------
        name : str
            metadata.name of the theme whose JSON config will be updated.

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
        client.theme_v1alpha1console.update_theme_json_config(
            name="name",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_theme_json_config(name, request=request, request_options=request_options)
        return _response.data

    def reload(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Reload theme setting.

        Parameters
        ----------
        name : str
            metadata.name of the theme to reload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theme_v1alpha1console.reload(
            name="name",
        )
        """
        _response = self._raw_client.reload(name, request_options=request_options)
        return _response.data

    def reset_theme_config(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ConfigMap:
        """
        Reset the configMap of theme setting.

        Parameters
        ----------
        name : str
            metadata.name of the theme whose setting config will be reset.

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
        client.theme_v1alpha1console.reset_theme_config(
            name="name",
        )
        """
        _response = self._raw_client.reset_theme_config(name, request_options=request_options)
        return _response.data

    def fetch_theme_setting(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Setting:
        """
        Fetch setting of theme.

        Parameters
        ----------
        name : str
            metadata.name of the theme whose setting will be fetched.

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
        client.theme_v1alpha1console.fetch_theme_setting(
            name="name",
        )
        """
        _response = self._raw_client.fetch_theme_setting(name, request_options=request_options)
        return _response.data

    def upgrade_theme(
        self, name: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Theme:
        """
        Upgrade theme

        Parameters
        ----------
        name : str
            metadata.name of the theme to upgrade.

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theme_v1alpha1console.upgrade_theme(
            name="name",
        )
        """
        _response = self._raw_client.upgrade_theme(name, file=file, request_options=request_options)
        return _response.data

    def upgrade_theme_from_uri(
        self, name: str, *, uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Theme:
        """
        Upgrade a theme from uri.

        Parameters
        ----------
        name : str
            metadata.name of the theme to upgrade.

        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theme_v1alpha1console.upgrade_theme_from_uri(
            name="name",
            uri="uri",
        )
        """
        _response = self._raw_client.upgrade_theme_from_uri(name, uri=uri, request_options=request_options)
        return _response.data


class AsyncThemeV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawThemeV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawThemeV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawThemeV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def list_themes(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        uninstalled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThemeList:
        """
        List themes.

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

        uninstalled : typing.Optional[bool]
            Whether to list uninstalled themes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThemeList
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
            await client.theme_v1alpha1console.list_themes()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_themes(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            uninstalled=uninstalled,
            request_options=request_options,
        )
        return _response.data

    async def fetch_activated_theme(self, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Fetch the activated theme.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
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
            await client.theme_v1alpha1console.fetch_activated_theme()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_activated_theme(request_options=request_options)
        return _response.data

    async def install_theme_from_uri(
        self, *, uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Theme:
        """
        Install a theme from uri.

        Parameters
        ----------
        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
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
            await client.theme_v1alpha1console.install_theme_from_uri(
                uri="uri",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.install_theme_from_uri(uri=uri, request_options=request_options)
        return _response.data

    async def install_theme(self, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Install a theme by uploading a zip file.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
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
            await client.theme_v1alpha1console.install_theme()


        asyncio.run(main())
        """
        _response = await self._raw_client.install_theme(request_options=request_options)
        return _response.data

    async def activate_theme(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Activate a theme by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of the theme to activate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
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
            await client.theme_v1alpha1console.activate_theme(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.activate_theme(name, request_options=request_options)
        return _response.data

    async def invalidate_cache(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidate theme template cache.

        Parameters
        ----------
        name : str
            metadata.name of the theme whose template cache will be invalidated.

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
            await client.theme_v1alpha1console.invalidate_cache(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invalidate_cache(name, request_options=request_options)
        return _response.data

    async def fetch_theme_json_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Fetch converted json config of theme by configured configMapName.

        Parameters
        ----------
        name : str
            metadata.name of the theme whose JSON config will be fetched.

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
            await client.theme_v1alpha1console.fetch_theme_json_config(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_theme_json_config(name, request_options=request_options)
        return _response.data

    async def update_theme_json_config(
        self,
        name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the configMap of theme setting.

        Parameters
        ----------
        name : str
            metadata.name of the theme whose JSON config will be updated.

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
            await client.theme_v1alpha1console.update_theme_json_config(
                name="name",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_theme_json_config(
            name, request=request, request_options=request_options
        )
        return _response.data

    async def reload(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Reload theme setting.

        Parameters
        ----------
        name : str
            metadata.name of the theme to reload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
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
            await client.theme_v1alpha1console.reload(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reload(name, request_options=request_options)
        return _response.data

    async def reset_theme_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigMap:
        """
        Reset the configMap of theme setting.

        Parameters
        ----------
        name : str
            metadata.name of the theme whose setting config will be reset.

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
            await client.theme_v1alpha1console.reset_theme_config(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_theme_config(name, request_options=request_options)
        return _response.data

    async def fetch_theme_setting(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Setting:
        """
        Fetch setting of theme.

        Parameters
        ----------
        name : str
            metadata.name of the theme whose setting will be fetched.

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
            await client.theme_v1alpha1console.fetch_theme_setting(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_theme_setting(name, request_options=request_options)
        return _response.data

    async def upgrade_theme(
        self, name: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Theme:
        """
        Upgrade theme

        Parameters
        ----------
        name : str
            metadata.name of the theme to upgrade.

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
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
            await client.theme_v1alpha1console.upgrade_theme(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upgrade_theme(name, file=file, request_options=request_options)
        return _response.data

    async def upgrade_theme_from_uri(
        self, name: str, *, uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Theme:
        """
        Upgrade a theme from uri.

        Parameters
        ----------
        name : str
            metadata.name of the theme to upgrade.

        uri : str
            remote URI of the theme ZIP file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
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
            await client.theme_v1alpha1console.upgrade_theme_from_uri(
                name="name",
                uri="uri",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upgrade_theme_from_uri(name, uri=uri, request_options=request_options)
        return _response.data
