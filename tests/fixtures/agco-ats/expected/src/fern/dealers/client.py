

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_dealer_db_models_dealer import ApiPagedResponseDealerDbModelsDealer
from ..types.dealer_db_models_dealer import DealerDbModelsDealer
from .raw_client import AsyncRawDealersClient, RawDealersClient


class DealersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDealersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDealersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDealersClient
        """
        return self._raw_client

    def getdealers(
        self,
        *,
        brand: typing.Optional[str] = None,
        shipping_country: typing.Optional[str] = None,
        dealer_name: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseDealerDbModelsDealer:
        """
        No Documentation Found.

        Parameters
        ----------
        brand : typing.Optional[str]
            The brand to filter by.

        shipping_country : typing.Optional[str]
            The country to filter by.

        dealer_name : typing.Optional[str]
            The partial Dealer Name to filter by. Wildcard supported (*).

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseDealerDbModelsDealer
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dealers.getdealers()
        """
        _response = self._raw_client.getdealers(
            brand=brand,
            shipping_country=shipping_country,
            dealer_name=dealer_name,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def getdealerbydealercode(
        self, dealer_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DealerDbModelsDealer:
        """
        No Documentation Found.

        Parameters
        ----------
        dealer_code : str
            The Dealer Code to Search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DealerDbModelsDealer
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dealers.getdealerbydealercode(
            dealer_code="DealerCode",
        )
        """
        _response = self._raw_client.getdealerbydealercode(dealer_code, request_options=request_options)
        return _response.data


class AsyncDealersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDealersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDealersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDealersClient
        """
        return self._raw_client

    async def getdealers(
        self,
        *,
        brand: typing.Optional[str] = None,
        shipping_country: typing.Optional[str] = None,
        dealer_name: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseDealerDbModelsDealer:
        """
        No Documentation Found.

        Parameters
        ----------
        brand : typing.Optional[str]
            The brand to filter by.

        shipping_country : typing.Optional[str]
            The country to filter by.

        dealer_name : typing.Optional[str]
            The partial Dealer Name to filter by. Wildcard supported (*).

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseDealerDbModelsDealer
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dealers.getdealers()


        asyncio.run(main())
        """
        _response = await self._raw_client.getdealers(
            brand=brand,
            shipping_country=shipping_country,
            dealer_name=dealer_name,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def getdealerbydealercode(
        self, dealer_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DealerDbModelsDealer:
        """
        No Documentation Found.

        Parameters
        ----------
        dealer_code : str
            The Dealer Code to Search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DealerDbModelsDealer
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dealers.getdealerbydealercode(
                dealer_code="DealerCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getdealerbydealercode(dealer_code, request_options=request_options)
        return _response.data
