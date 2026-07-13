

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.payment_auto_allocate_definition_listing import PaymentAutoAllocateDefinitionListing
from .raw_client import AsyncRawDefinitionClient, RawDefinitionClient


class DefinitionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDefinitionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDefinitionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDefinitionClient
        """
        return self._raw_client

    def list_all_definition_for_user_monetary_account_payment_auto_allocate(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_auto_allocate_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PaymentAutoAllocateDefinitionListing]:
        """
        List all the definitions in a payment auto allocate.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_auto_allocate_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentAutoAllocateDefinitionListing]
            List all the definitions in a payment auto allocate.

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
        client.definition.list_all_definition_for_user_monetary_account_payment_auto_allocate(
            user_id=1,
            monetary_account_id=1,
            payment_auto_allocate_id=1,
        )
        """
        _response = self._raw_client.list_all_definition_for_user_monetary_account_payment_auto_allocate(
            user_id, monetary_account_id, payment_auto_allocate_id, request_options=request_options
        )
        return _response.data


class AsyncDefinitionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDefinitionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDefinitionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDefinitionClient
        """
        return self._raw_client

    async def list_all_definition_for_user_monetary_account_payment_auto_allocate(
        self,
        user_id: int,
        monetary_account_id: int,
        payment_auto_allocate_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PaymentAutoAllocateDefinitionListing]:
        """
        List all the definitions in a payment auto allocate.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment_auto_allocate_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentAutoAllocateDefinitionListing]
            List all the definitions in a payment auto allocate.

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
            await client.definition.list_all_definition_for_user_monetary_account_payment_auto_allocate(
                user_id=1,
                monetary_account_id=1,
                payment_auto_allocate_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_definition_for_user_monetary_account_payment_auto_allocate(
            user_id, monetary_account_id, payment_auto_allocate_id, request_options=request_options
        )
        return _response.data
