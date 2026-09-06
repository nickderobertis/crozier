

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_dealer_db_models_dealers_per_country import (
    ApiPagedResponseDealerDbModelsDealersPerCountry,
)
from .raw_client import AsyncRawDealerbycountryClient, RawDealerbycountryClient


class DealerbycountryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDealerbycountryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDealerbycountryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDealerbycountryClient
        """
        return self._raw_client

    def getcountries(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseDealerDbModelsDealersPerCountry:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseDealerDbModelsDealersPerCountry
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dealerbycountry.getcountries()
        """
        _response = self._raw_client.getcountries(limit=limit, offset=offset, request_options=request_options)
        return _response.data


class AsyncDealerbycountryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDealerbycountryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDealerbycountryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDealerbycountryClient
        """
        return self._raw_client

    async def getcountries(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseDealerDbModelsDealersPerCountry:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseDealerDbModelsDealersPerCountry
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dealerbycountry.getcountries()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcountries(limit=limit, offset=offset, request_options=request_options)
        return _response.data
