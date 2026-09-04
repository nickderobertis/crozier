

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.calculated_grant_offer import CalculatedGrantOffer
from ..types.financing_type import FinancingType
from ..types.get_dynamic_offers_response import GetDynamicOffersResponse
from ..types.grant_offer import GrantOffer
from .raw_client import AsyncRawDynamicOffersClient, RawDynamicOffersClient


OMIT = typing.cast(typing.Any, ...)


class DynamicOffersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDynamicOffersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDynamicOffersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDynamicOffersClient
        """
        return self._raw_client

    def get_dynamic_offers(
        self,
        *,
        account_holder_id: str,
        financing_type: typing.Optional[FinancingType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDynamicOffersResponse:
        """
        Returns a list of all [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/) available for `accountHolderId` specified as a query parameter.

        Parameters
        ----------
        account_holder_id : str
            The unique identifier of the account holder that the dynamic offer is for.

        financing_type : typing.Optional[FinancingType]
            The type of financing that the offer is for. If the value is not specified, returns all available types.

            Possible values: **businessFinancing**

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDynamicOffersResponse
            OK - The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dynamic_offers.get_dynamic_offers(
            account_holder_id="accountHolderId",
        )
        """
        _response = self._raw_client.get_dynamic_offers(
            account_holder_id=account_holder_id, financing_type=financing_type, request_options=request_options
        )
        return _response.data

    def post_dynamic_offers_id_calculate(
        self, id: str, *, amount: Amount, request_options: typing.Optional[RequestOptions] = None
    ) -> CalculatedGrantOffer:
        """
        Calculates a preliminary offer for the financing amount that the user selected from a [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/). The preliminary offer is for informational purposes only and cannot be used to initiate a grant.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 120 requests per minute.

        - Test environments: 120 requests per minute.

        Parameters
        ----------
        id : str
            The unique identifier of the dynamic offer from which the user selected the financing amount.

        amount : Amount
            The financing amount that the user selected from a dynamic offer. Adyen uses this amount to calculate a preliminary offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalculatedGrantOffer
            OK - The request has succeeded.

        Examples
        --------
        from fern import Amount, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dynamic_offers.post_dynamic_offers_id_calculate(
            id="id",
            amount=Amount(
                currency="currency",
                value=1000000,
            ),
        )
        """
        _response = self._raw_client.post_dynamic_offers_id_calculate(
            id, amount=amount, request_options=request_options
        )
        return _response.data

    def post_dynamic_offers_id_grant_offer(
        self, id: str, *, amount: Amount, request_options: typing.Optional[RequestOptions] = None
    ) -> GrantOffer:
        """
        Creates a static offer for the financing amount that the user selected from the [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

        Requests to this endpoint are subject to rate limits:

        - Live environments: 30 requests per minute.

        - Test environments: 30 requests per minute.

        Parameters
        ----------
        id : str
            The unique identifier of the dynamic offer from which the user selected the financing amount.

        amount : Amount
            The financing amount that the user selected from the dynamic offer. Adyen uses this amount to create a static offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrantOffer
            OK - The request has succeeded.

        Examples
        --------
        from fern import Amount, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dynamic_offers.post_dynamic_offers_id_grant_offer(
            id="id",
            amount=Amount(
                currency="currency",
                value=1000000,
            ),
        )
        """
        _response = self._raw_client.post_dynamic_offers_id_grant_offer(
            id, amount=amount, request_options=request_options
        )
        return _response.data


class AsyncDynamicOffersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDynamicOffersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDynamicOffersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDynamicOffersClient
        """
        return self._raw_client

    async def get_dynamic_offers(
        self,
        *,
        account_holder_id: str,
        financing_type: typing.Optional[FinancingType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDynamicOffersResponse:
        """
        Returns a list of all [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/) available for `accountHolderId` specified as a query parameter.

        Parameters
        ----------
        account_holder_id : str
            The unique identifier of the account holder that the dynamic offer is for.

        financing_type : typing.Optional[FinancingType]
            The type of financing that the offer is for. If the value is not specified, returns all available types.

            Possible values: **businessFinancing**

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDynamicOffersResponse
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dynamic_offers.get_dynamic_offers(
                account_holder_id="accountHolderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dynamic_offers(
            account_holder_id=account_holder_id, financing_type=financing_type, request_options=request_options
        )
        return _response.data

    async def post_dynamic_offers_id_calculate(
        self, id: str, *, amount: Amount, request_options: typing.Optional[RequestOptions] = None
    ) -> CalculatedGrantOffer:
        """
        Calculates a preliminary offer for the financing amount that the user selected from a [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/). The preliminary offer is for informational purposes only and cannot be used to initiate a grant.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 120 requests per minute.

        - Test environments: 120 requests per minute.

        Parameters
        ----------
        id : str
            The unique identifier of the dynamic offer from which the user selected the financing amount.

        amount : Amount
            The financing amount that the user selected from a dynamic offer. Adyen uses this amount to calculate a preliminary offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalculatedGrantOffer
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dynamic_offers.post_dynamic_offers_id_calculate(
                id="id",
                amount=Amount(
                    currency="currency",
                    value=1000000,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_dynamic_offers_id_calculate(
            id, amount=amount, request_options=request_options
        )
        return _response.data

    async def post_dynamic_offers_id_grant_offer(
        self, id: str, *, amount: Amount, request_options: typing.Optional[RequestOptions] = None
    ) -> GrantOffer:
        """
        Creates a static offer for the financing amount that the user selected from the [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

        Requests to this endpoint are subject to rate limits:

        - Live environments: 30 requests per minute.

        - Test environments: 30 requests per minute.

        Parameters
        ----------
        id : str
            The unique identifier of the dynamic offer from which the user selected the financing amount.

        amount : Amount
            The financing amount that the user selected from the dynamic offer. Adyen uses this amount to create a static offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrantOffer
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dynamic_offers.post_dynamic_offers_id_grant_offer(
                id="id",
                amount=Amount(
                    currency="currency",
                    value=1000000,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_dynamic_offers_id_grant_offer(
            id, amount=amount, request_options=request_options
        )
        return _response.data
