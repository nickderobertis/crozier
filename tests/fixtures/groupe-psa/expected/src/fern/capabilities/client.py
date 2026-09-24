

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.vehicle_capabilities import VehicleCapabilities
from ..types.vehicle_extension_type_item import VehicleExtensionTypeItem
from .raw_client import AsyncRawCapabilitiesClient, RawCapabilitiesClient


class CapabilitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCapabilitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCapabilitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCapabilitiesClient
        """
        return self._raw_client

    def get_vehicles_capabilities(
        self,
        vin: str,
        *,
        locale: typing.Optional[str] = None,
        extension: typing.Optional[
            typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VehicleCapabilities:
        """
        Returns vehicle'scharacteristics & capabilities

        Parameters
        ----------
        vin : str
            Results will only be related to this Vehicle Identification Number.

        locale : typing.Optional[str]
            Locale is used for rendering text according to language and country for. It should match the  REGEX \\w(-\\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).

        extension : typing.Optional[typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]]
            Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 3)```.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VehicleCapabilities
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.capabilities.get_vehicles_capabilities(
            vin="VF3ABCDE0FG123456",
        )
        """
        _response = self._raw_client.get_vehicles_capabilities(
            vin, locale=locale, extension=extension, request_options=request_options
        )
        return _response.data


class AsyncCapabilitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCapabilitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCapabilitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCapabilitiesClient
        """
        return self._raw_client

    async def get_vehicles_capabilities(
        self,
        vin: str,
        *,
        locale: typing.Optional[str] = None,
        extension: typing.Optional[
            typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VehicleCapabilities:
        """
        Returns vehicle'scharacteristics & capabilities

        Parameters
        ----------
        vin : str
            Results will only be related to this Vehicle Identification Number.

        locale : typing.Optional[str]
            Locale is used for rendering text according to language and country for. It should match the  REGEX \\w(-\\w)?. For more details about possible standard values, please refer to [locals list](https://en.wikipedia.org/wiki/Language_localisation).

        extension : typing.Optional[typing.Union[VehicleExtensionTypeItem, typing.Sequence[VehicleExtensionTypeItem]]]
            Additional data set that will be included in embedded field```(the number of elements in this array must be between 1 and 3)```.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VehicleCapabilities
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.capabilities.get_vehicles_capabilities(
                vin="VF3ABCDE0FG123456",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vehicles_capabilities(
            vin, locale=locale, extension=extension, request_options=request_options
        )
        return _response.data
