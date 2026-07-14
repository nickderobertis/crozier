

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.limits import Limits
from ..types.system_info import SystemInfo
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
        This operation retrieves information about the running registry system, such as the version
        of the software and when it was built.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemInfo
            On success, returns the system information.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_system_info()
        """
        _response = self._raw_client.get_system_info(request_options=request_options)
        return _response.data

    def get_resource_limits(self, *, request_options: typing.Optional[RequestOptions] = None) -> Limits:
        """
        This operation retrieves the list of limitations on used resources, that are applied on the current instance of Registry.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Limits
            On success, returns resource limits

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_resource_limits()
        """
        _response = self._raw_client.get_resource_limits(request_options=request_options)
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
        This operation retrieves information about the running registry system, such as the version
        of the software and when it was built.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemInfo
            On success, returns the system information.

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

    async def get_resource_limits(self, *, request_options: typing.Optional[RequestOptions] = None) -> Limits:
        """
        This operation retrieves the list of limitations on used resources, that are applied on the current instance of Registry.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Limits
            On success, returns resource limits

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.get_resource_limits()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_resource_limits(request_options=request_options)
        return _response.data
