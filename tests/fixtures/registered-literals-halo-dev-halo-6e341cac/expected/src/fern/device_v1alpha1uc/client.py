

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_device import UserDevice
from .raw_client import AsyncRawDeviceV1Alpha1UcClient, RawDeviceV1Alpha1UcClient


class DeviceV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeviceV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeviceV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeviceV1Alpha1UcClient
        """
        return self._raw_client

    def list_devices(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[UserDevice]:
        """
        List all user devices

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserDevice]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.device_v1alpha1uc.list_devices()
        """
        _response = self._raw_client.list_devices(request_options=request_options)
        return _response.data

    def revoke_device(self, device_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revoke a own device

        Parameters
        ----------
        device_id : str
            Device ID

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
        client.device_v1alpha1uc.revoke_device(
            device_id="deviceId",
        )
        """
        _response = self._raw_client.revoke_device(device_id, request_options=request_options)
        return _response.data


class AsyncDeviceV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeviceV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeviceV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeviceV1Alpha1UcClient
        """
        return self._raw_client

    async def list_devices(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[UserDevice]:
        """
        List all user devices

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserDevice]
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
            await client.device_v1alpha1uc.list_devices()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_devices(request_options=request_options)
        return _response.data

    async def revoke_device(self, device_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revoke a own device

        Parameters
        ----------
        device_id : str
            Device ID

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
            await client.device_v1alpha1uc.revoke_device(
                device_id="deviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_device(device_id, request_options=request_options)
        return _response.data
