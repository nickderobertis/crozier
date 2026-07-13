

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.billing_contract_subscription_listing import BillingContractSubscriptionListing
from .raw_client import AsyncRawBillingContractSubscriptionClient, RawBillingContractSubscriptionClient


class BillingContractSubscriptionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBillingContractSubscriptionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBillingContractSubscriptionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBillingContractSubscriptionClient
        """
        return self._raw_client

    def list_all_billing_contract_subscription_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BillingContractSubscriptionListing]:
        """
        Get all subscription billing contract for the authenticated user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BillingContractSubscriptionListing]
            Show the subscription billing contract for the authenticated user.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.billing_contract_subscription.list_all_billing_contract_subscription_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_billing_contract_subscription_for_user(
            user_id, request_options=request_options
        )
        return _response.data


class AsyncBillingContractSubscriptionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBillingContractSubscriptionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBillingContractSubscriptionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBillingContractSubscriptionClient
        """
        return self._raw_client

    async def list_all_billing_contract_subscription_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BillingContractSubscriptionListing]:
        """
        Get all subscription billing contract for the authenticated user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BillingContractSubscriptionListing]
            Show the subscription billing contract for the authenticated user.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.billing_contract_subscription.list_all_billing_contract_subscription_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_billing_contract_subscription_for_user(
            user_id, request_options=request_options
        )
        return _response.data
