

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_persons_response_body import ListPersonsResponseBody
from ..types.merchant import Merchant
from ..types.person import Person
from .raw_client import AsyncRawMerchantsClient, RawMerchantsClient


class MerchantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMerchantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMerchantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMerchantsClient
        """
        return self._raw_client

    def get_merchant(self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None) -> Merchant:
        """
        Returns a Merchant for a valid Merchant code.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Merchant
            Returns a Merchant for a valid identifier.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.merchants.get_merchant(
            merchant_code="MK10CL2A",
        )
        """
        _response = self._raw_client.get_merchant(merchant_code, request_options=request_options)
        return _response.data

    def list_persons(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListPersonsResponseBody:
        """
        Returns the Persons related to a Merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPersonsResponseBody
            Returns a list of Persons for a valid Merchant identifier.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.merchants.list_persons(
            merchant_code="MK10CL2A",
        )
        """
        _response = self._raw_client.list_persons(merchant_code, request_options=request_options)
        return _response.data

    def get_person(
        self, merchant_code: str, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Person:
        """
        Returns a single Person related to a Merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        person_id : str
            Person ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Person
            Returns a Person for a valid identifier.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.merchants.get_person(
            merchant_code="MK10CL2A",
            person_id="pers_5AKFHN2KSK8D3TS79DJE3P3A2Z",
        )
        """
        _response = self._raw_client.get_person(merchant_code, person_id, request_options=request_options)
        return _response.data


class AsyncMerchantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMerchantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMerchantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMerchantsClient
        """
        return self._raw_client

    async def get_merchant(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Merchant:
        """
        Returns a Merchant for a valid Merchant code.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Merchant
            Returns a Merchant for a valid identifier.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.merchants.get_merchant(
                merchant_code="MK10CL2A",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_merchant(merchant_code, request_options=request_options)
        return _response.data

    async def list_persons(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListPersonsResponseBody:
        """
        Returns the Persons related to a Merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPersonsResponseBody
            Returns a list of Persons for a valid Merchant identifier.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.merchants.list_persons(
                merchant_code="MK10CL2A",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_persons(merchant_code, request_options=request_options)
        return _response.data

    async def get_person(
        self, merchant_code: str, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Person:
        """
        Returns a single Person related to a Merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        person_id : str
            Person ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Person
            Returns a Person for a valid identifier.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.merchants.get_person(
                merchant_code="MK10CL2A",
                person_id="pers_5AKFHN2KSK8D3TS79DJE3P3A2Z",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_person(merchant_code, person_id, request_options=request_options)
        return _response.data
