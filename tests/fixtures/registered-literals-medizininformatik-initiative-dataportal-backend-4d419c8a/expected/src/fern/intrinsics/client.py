

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.settings_info import SettingsInfo
from ..types.system_info import SystemInfo
from .raw_client import AsyncRawIntrinsicsClient, RawIntrinsicsClient


class IntrinsicsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIntrinsicsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIntrinsicsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIntrinsicsClient
        """
        return self._raw_client

    def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful health information.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.intrinsics.get_health()
        """
        _response = self._raw_client.get_health(request_options=request_options)
        return _response.data

    def get_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemInfo:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemInfo
            Successful build information.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.intrinsics.get_info()
        """
        _response = self._raw_client.get_info(request_options=request_options)
        return _response.data

    def get_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> SettingsInfo:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsInfo
            Successful health information.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.intrinsics.get_settings()
        """
        _response = self._raw_client.get_settings(request_options=request_options)
        return _response.data


class AsyncIntrinsicsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIntrinsicsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIntrinsicsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIntrinsicsClient
        """
        return self._raw_client

    async def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful health information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.intrinsics.get_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_health(request_options=request_options)
        return _response.data

    async def get_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemInfo:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemInfo
            Successful build information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.intrinsics.get_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_info(request_options=request_options)
        return _response.data

    async def get_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> SettingsInfo:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsInfo
            Successful health information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.intrinsics.get_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_settings(request_options=request_options)
        return _response.data
