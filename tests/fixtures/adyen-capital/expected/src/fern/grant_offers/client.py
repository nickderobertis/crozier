

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.grant_offer import GrantOffer
from ..types.grant_offers import GrantOffers
from .raw_client import AsyncRawGrantOffersClient, RawGrantOffersClient


class GrantOffersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGrantOffersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGrantOffersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGrantOffersClient
        """
        return self._raw_client

    def get_grant_offers(
        self, *, account_holder_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GrantOffers:
        """
        Returns a list of all [static offers](https://docs.adyen.com/capital/get-grant-offers/static-offers) available for `accountHolderId` specified as a query parameter. This also includes static offers created for financing amounts that the user selected from [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

        Parameters
        ----------
        account_holder_id : str
            The unique identifier of the account holder for which you want to get the available static offers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrantOffers
            OK - The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.grant_offers.get_grant_offers(
            account_holder_id="accountHolderId",
        )
        """
        _response = self._raw_client.get_grant_offers(
            account_holder_id=account_holder_id, request_options=request_options
        )
        return _response.data

    def get_grant_offers_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GrantOffer:
        """
        Returns the details of the specified static offer.

        Parameters
        ----------
        id : str
            The unique identifier of the static offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrantOffer
            OK - The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.grant_offers.get_grant_offers_id(
            id="id",
        )
        """
        _response = self._raw_client.get_grant_offers_id(id, request_options=request_options)
        return _response.data


class AsyncGrantOffersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGrantOffersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGrantOffersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGrantOffersClient
        """
        return self._raw_client

    async def get_grant_offers(
        self, *, account_holder_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GrantOffers:
        """
        Returns a list of all [static offers](https://docs.adyen.com/capital/get-grant-offers/static-offers) available for `accountHolderId` specified as a query parameter. This also includes static offers created for financing amounts that the user selected from [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

        Parameters
        ----------
        account_holder_id : str
            The unique identifier of the account holder for which you want to get the available static offers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrantOffers
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.grant_offers.get_grant_offers(
                account_holder_id="accountHolderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_grant_offers(
            account_holder_id=account_holder_id, request_options=request_options
        )
        return _response.data

    async def get_grant_offers_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GrantOffer:
        """
        Returns the details of the specified static offer.

        Parameters
        ----------
        id : str
            The unique identifier of the static offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrantOffer
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.grant_offers.get_grant_offers_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_grant_offers_id(id, request_options=request_options)
        return _response.data
