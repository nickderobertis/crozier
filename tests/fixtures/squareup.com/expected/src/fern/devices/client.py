

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_device_code_response import CreateDeviceCodeResponse
from ..types.device_code import DeviceCode
from ..types.get_device_code_response import GetDeviceCodeResponse
from ..types.list_device_codes_response import ListDeviceCodesResponse
from .raw_client import AsyncRawDevicesClient, RawDevicesClient


OMIT = typing.cast(typing.Any, ...)


class DevicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDevicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDevicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDevicesClient
        """
        return self._raw_client

    def list_device_codes(
        self,
        *,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        product_type: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDeviceCodesResponse:
        """
        Lists all DeviceCodes associated with the merchant.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.

        location_id : typing.Optional[str]
            If specified, only returns DeviceCodes of the specified location.
            Returns DeviceCodes of all locations if empty.

        product_type : typing.Optional[str]
            If specified, only returns DeviceCodes targeting the specified product type.
            Returns DeviceCodes of all product types if empty.

        status : typing.Optional[str]
            If specified, returns DeviceCodes with the specified statuses.
            Returns DeviceCodes of status `PAIRED` and `UNPAIRED` if empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDeviceCodesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.devices.list_device_codes()
        """
        _response = self._raw_client.list_device_codes(
            cursor=cursor,
            location_id=location_id,
            product_type=product_type,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def create_device_code(
        self, *, device_code: DeviceCode, idempotency_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateDeviceCodeResponse:
        """
        Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected
        terminal mode.

        Parameters
        ----------
        device_code : DeviceCode

        idempotency_key : str
            A unique string that identifies this CreateDeviceCode request. Keys can
            be any valid string but must be unique for every CreateDeviceCode request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDeviceCodeResponse
            Success

        Examples
        --------
        from fern import DeviceCode, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.devices.create_device_code(
            device_code=DeviceCode(
                product_type="product_type",
            ),
            idempotency_key="idempotency_key",
        )
        """
        _response = self._raw_client.create_device_code(
            device_code=device_code, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def get_device_code(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDeviceCodeResponse:
        """
        Retrieves DeviceCode with the associated ID.

        Parameters
        ----------
        id : str
            The unique identifier for the device code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceCodeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.devices.get_device_code(
            id="id",
        )
        """
        _response = self._raw_client.get_device_code(id, request_options=request_options)
        return _response.data


class AsyncDevicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDevicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDevicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDevicesClient
        """
        return self._raw_client

    async def list_device_codes(
        self,
        *,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        product_type: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDeviceCodesResponse:
        """
        Lists all DeviceCodes associated with the merchant.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.

        location_id : typing.Optional[str]
            If specified, only returns DeviceCodes of the specified location.
            Returns DeviceCodes of all locations if empty.

        product_type : typing.Optional[str]
            If specified, only returns DeviceCodes targeting the specified product type.
            Returns DeviceCodes of all product types if empty.

        status : typing.Optional[str]
            If specified, returns DeviceCodes with the specified statuses.
            Returns DeviceCodes of status `PAIRED` and `UNPAIRED` if empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDeviceCodesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.devices.list_device_codes()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_device_codes(
            cursor=cursor,
            location_id=location_id,
            product_type=product_type,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def create_device_code(
        self, *, device_code: DeviceCode, idempotency_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateDeviceCodeResponse:
        """
        Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected
        terminal mode.

        Parameters
        ----------
        device_code : DeviceCode

        idempotency_key : str
            A unique string that identifies this CreateDeviceCode request. Keys can
            be any valid string but must be unique for every CreateDeviceCode request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDeviceCodeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DeviceCode

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.devices.create_device_code(
                device_code=DeviceCode(
                    product_type="product_type",
                ),
                idempotency_key="idempotency_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_device_code(
            device_code=device_code, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def get_device_code(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDeviceCodeResponse:
        """
        Retrieves DeviceCode with the associated ID.

        Parameters
        ----------
        id : str
            The unique identifier for the device code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceCodeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.devices.get_device_code(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_code(id, request_options=request_options)
        return _response.data
