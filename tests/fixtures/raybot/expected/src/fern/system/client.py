

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.system_info import SystemInfo
from ..types.system_status import SystemStatus
from .raw_client import AsyncRawSystemClient, RawSystemClient


class SystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemClient
        """
        return self._raw_client

    def get_system_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemInfo:
        """
        Get the system information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemInfo
            The system information

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_system_info()
        """
        _response = self._raw_client.get_system_info(request_options=request_options)
        return _response.data

    def get_system_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemStatus:
        """
        Get the system status

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemStatus
            The system status

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_system_status()
        """
        _response = self._raw_client.get_system_status(request_options=request_options)
        return _response.data

    def reboot_system(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Reboot the system.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.reboot_system()
        """
        _response = self._raw_client.reboot_system(request_options=request_options)
        return _response.data

    def stop_emergency(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Stop all motors and cancel all running, queued and processing commands

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.stop_emergency()
        """
        _response = self._raw_client.stop_emergency(request_options=request_options)
        return _response.data


class AsyncSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemClient
        """
        return self._raw_client

    async def get_system_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemInfo:
        """
        Get the system information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemInfo
            The system information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.get_system_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_info(request_options=request_options)
        return _response.data

    async def get_system_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemStatus:
        """
        Get the system status

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemStatus
            The system status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.get_system_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_status(request_options=request_options)
        return _response.data

    async def reboot_system(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Reboot the system.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.reboot_system()


        asyncio.run(main())
        """
        _response = await self._raw_client.reboot_system(request_options=request_options)
        return _response.data

    async def stop_emergency(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Stop all motors and cancel all running, queued and processing commands

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.stop_emergency()


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_emergency(request_options=request_options)
        return _response.data
