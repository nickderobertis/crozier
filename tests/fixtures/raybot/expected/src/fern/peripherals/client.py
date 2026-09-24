

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.serial_port_list_response import SerialPortListResponse
from .raw_client import AsyncRawPeripheralsClient, RawPeripheralsClient


class PeripheralsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPeripheralsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPeripheralsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPeripheralsClient
        """
        return self._raw_client

    def list_available_serial_ports(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SerialPortListResponse:
        """
        List all available serial ports

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SerialPortListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.peripherals.list_available_serial_ports()
        """
        _response = self._raw_client.list_available_serial_ports(request_options=request_options)
        return _response.data


class AsyncPeripheralsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPeripheralsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPeripheralsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPeripheralsClient
        """
        return self._raw_client

    async def list_available_serial_ports(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SerialPortListResponse:
        """
        List all available serial ports

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SerialPortListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.peripherals.list_available_serial_ports()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_available_serial_ports(request_options=request_options)
        return _response.data
