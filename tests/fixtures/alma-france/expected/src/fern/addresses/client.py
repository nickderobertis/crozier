

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from .raw_client import AsyncRawAddressesClient, RawAddressesClient


OMIT = typing.cast(typing.Any, ...)


class AddressesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAddressesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAddressesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAddressesClient
        """
        return self._raw_client

    def createaddress(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        line1: typing.Optional[str] = OMIT,
        line2: typing.Optional[str] = OMIT,
        city: typing.Optional[str] = OMIT,
        postal_code: typing.Optional[str] = OMIT,
        country: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Address:
        """
        Parameters
        ----------
        id : typing.Optional[str]

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        line1 : typing.Optional[str]

        line2 : typing.Optional[str]

        city : typing.Optional[str]

        postal_code : typing.Optional[str]

        country : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Address
            Address created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.addresses.createaddress()
        """
        _response = self._raw_client.createaddress(
            id=id,
            first_name=first_name,
            last_name=last_name,
            line1=line1,
            line2=line2,
            city=city,
            postal_code=postal_code,
            country=country,
            request_options=request_options,
        )
        return _response.data


class AsyncAddressesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAddressesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAddressesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAddressesClient
        """
        return self._raw_client

    async def createaddress(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        line1: typing.Optional[str] = OMIT,
        line2: typing.Optional[str] = OMIT,
        city: typing.Optional[str] = OMIT,
        postal_code: typing.Optional[str] = OMIT,
        country: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Address:
        """
        Parameters
        ----------
        id : typing.Optional[str]

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        line1 : typing.Optional[str]

        line2 : typing.Optional[str]

        city : typing.Optional[str]

        postal_code : typing.Optional[str]

        country : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Address
            Address created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.addresses.createaddress()


        asyncio.run(main())
        """
        _response = await self._raw_client.createaddress(
            id=id,
            first_name=first_name,
            last_name=last_name,
            line1=line1,
            line2=line2,
            city=city,
            postal_code=postal_code,
            country=country,
            request_options=request_options,
        )
        return _response.data
