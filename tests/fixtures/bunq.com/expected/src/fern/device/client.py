

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.device_listing import DeviceListing
from ..types.device_read import DeviceRead
from .raw_client import AsyncRawDeviceClient, RawDeviceClient


class DeviceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeviceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeviceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeviceClient
        """
        return self._raw_client

    def list_all_device(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[DeviceListing]:
        """
        Get a collection of Devices. A Device is either a DevicePhone or a DeviceServer.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeviceListing]
            Used to get a Device or a listing of Devices. Creating a DeviceServer should happen via /device-server

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.device.list_all_device()
        """
        _response = self._raw_client.list_all_device(request_options=request_options)
        return _response.data

    def read_device(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> DeviceRead:
        """
        Get a single Device. A Device is either a DevicePhone or a DeviceServer.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceRead
            Used to get a Device or a listing of Devices. Creating a DeviceServer should happen via /device-server

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.device.read_device(
            item_id=1,
        )
        """
        _response = self._raw_client.read_device(item_id, request_options=request_options)
        return _response.data


class AsyncDeviceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeviceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeviceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeviceClient
        """
        return self._raw_client

    async def list_all_device(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeviceListing]:
        """
        Get a collection of Devices. A Device is either a DevicePhone or a DeviceServer.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeviceListing]
            Used to get a Device or a listing of Devices. Creating a DeviceServer should happen via /device-server

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.device.list_all_device()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_device(request_options=request_options)
        return _response.data

    async def read_device(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> DeviceRead:
        """
        Get a single Device. A Device is either a DevicePhone or a DeviceServer.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceRead
            Used to get a Device or a listing of Devices. Creating a DeviceServer should happen via /device-server

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.device.read_device(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_device(item_id, request_options=request_options)
        return _response.data
