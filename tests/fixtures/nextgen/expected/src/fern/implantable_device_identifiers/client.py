

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok51 import Ok51
from ..types.ok52 import Ok52
from .raw_client import AsyncRawImplantableDeviceIdentifiersClient, RawImplantableDeviceIdentifiersClient


class ImplantableDeviceIdentifiersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImplantableDeviceIdentifiersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImplantableDeviceIdentifiersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImplantableDeviceIdentifiersClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_devices(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok51:
        """
        Returns a list of implantable devices for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose devices are being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok51
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.implantable_device_identifiers.base_url_persons_person_id_chart_devices(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_devices(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_devices_device_id(
        self, person_id: str, device_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok52:
        """
        Returns a single implantable device for the specified person id and device id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose device information is being retrieved

        device_id : str
            (Required) (Required) The device id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok52
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.implantable_device_identifiers.base_url_persons_person_id_chart_devices_device_id(
            person_id="personId",
            device_id="deviceId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_devices_device_id(
            person_id, device_id, request_options=request_options
        )
        return _response.data


class AsyncImplantableDeviceIdentifiersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImplantableDeviceIdentifiersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImplantableDeviceIdentifiersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImplantableDeviceIdentifiersClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_devices(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok51:
        """
        Returns a list of implantable devices for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose devices are being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok51
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.implantable_device_identifiers.base_url_persons_person_id_chart_devices(
                person_id="personId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_devices(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_devices_device_id(
        self, person_id: str, device_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok52:
        """
        Returns a single implantable device for the specified person id and device id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose device information is being retrieved

        device_id : str
            (Required) (Required) The device id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok52
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.implantable_device_identifiers.base_url_persons_person_id_chart_devices_device_id(
                person_id="personId",
                device_id="deviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_devices_device_id(
            person_id, device_id, request_options=request_options
        )
        return _response.data
