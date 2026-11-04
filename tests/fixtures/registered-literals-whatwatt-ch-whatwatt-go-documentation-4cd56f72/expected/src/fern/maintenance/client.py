

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMaintenanceClient, RawMaintenanceClient


OMIT = typing.cast(typing.Any, ...)


class MaintenanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMaintenanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMaintenanceClient
        """
        return self._raw_client

    def reboot_device(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Triggers a manual device reboot. Most configuration changes do not require a reboot.

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

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.maintenance.reboot_device()
        """
        _response = self._raw_client.reboot_device(request_options=request_options)
        return _response.data

    def upload_firmware(self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Upload a firmware .bin file. After successful verification, the device will reboot automatically.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Upload accepted; device will reboot after successful update
        """
        _response = self._raw_client.upload_firmware(file=file, request_options=request_options)
        return _response.data

    def factory_reset(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Restores factory defaults. This operation may take a moment and the device will reboot.

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

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.maintenance.factory_reset()
        """
        _response = self._raw_client.factory_reset(request_options=request_options)
        return _response.data


class AsyncMaintenanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMaintenanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMaintenanceClient
        """
        return self._raw_client

    async def reboot_device(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Triggers a manual device reboot. Most configuration changes do not require a reboot.

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

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.maintenance.reboot_device()


        asyncio.run(main())
        """
        _response = await self._raw_client.reboot_device(request_options=request_options)
        return _response.data

    async def upload_firmware(self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Upload a firmware .bin file. After successful verification, the device will reboot automatically.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Upload accepted; device will reboot after successful update
        """
        _response = await self._raw_client.upload_firmware(file=file, request_options=request_options)
        return _response.data

    async def factory_reset(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Restores factory defaults. This operation may take a moment and the device will reboot.

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

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.maintenance.factory_reset()


        asyncio.run(main())
        """
        _response = await self._raw_client.factory_reset(request_options=request_options)
        return _response.data
