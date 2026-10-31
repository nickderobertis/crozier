

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDeviceInformationClient, RawDeviceInformationClient


class DeviceInformationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeviceInformationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeviceInformationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeviceInformationClient
        """
        return self._raw_client

    def get_status_ex(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getStatusEx

        Retrieves detailed informations about a connected device.

        The documented output may or may not be complete or differ from what the device actually reports.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.device_information.get_status_ex()
        """
        _response = self._raw_client.get_status_ex(request_options=request_options)
        return _response.data

    def get_debug_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getDebugInfo

        Retrieves debug information about a connected device.

        The documented output may or may not be complete or differ from what the device actually reports.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.device_information.get_debug_info()
        """
        _response = self._raw_client.get_debug_info(request_options=request_options)
        return _response.data


class AsyncDeviceInformationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeviceInformationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeviceInformationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeviceInformationClient
        """
        return self._raw_client

    async def get_status_ex(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getStatusEx

        Retrieves detailed informations about a connected device.

        The documented output may or may not be complete or differ from what the device actually reports.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.device_information.get_status_ex()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status_ex(request_options=request_options)
        return _response.data

    async def get_debug_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getDebugInfo

        Retrieves debug information about a connected device.

        The documented output may or may not be complete or differ from what the device actually reports.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.device_information.get_debug_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_debug_info(request_options=request_options)
        return _response.data
