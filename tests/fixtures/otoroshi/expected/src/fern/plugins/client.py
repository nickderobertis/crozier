

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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

    def otoroshi_next_controllers_ng_plugins_controller_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugins.otoroshi_next_controllers_ng_plugins_controller_categories()
        """
        _response = self._raw_client.otoroshi_next_controllers_ng_plugins_controller_categories(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_ng_plugins_controller_steps(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugins.otoroshi_next_controllers_ng_plugins_controller_steps()
        """
        _response = self._raw_client.otoroshi_next_controllers_ng_plugins_controller_steps(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_ng_plugins_controller_plugins(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugins.otoroshi_next_controllers_ng_plugins_controller_plugins()
        """
        _response = self._raw_client.otoroshi_next_controllers_ng_plugins_controller_plugins(
            request_options=request_options
        )
        return _response.data


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

    async def otoroshi_next_controllers_ng_plugins_controller_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.plugins.otoroshi_next_controllers_ng_plugins_controller_categories()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_ng_plugins_controller_categories(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_ng_plugins_controller_steps(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.plugins.otoroshi_next_controllers_ng_plugins_controller_steps()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_ng_plugins_controller_steps(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_ng_plugins_controller_plugins(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.plugins.otoroshi_next_controllers_ng_plugins_controller_plugins()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_ng_plugins_controller_plugins(
            request_options=request_options
        )
        return _response.data
