

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bank_switch_service_netherlands_incoming_payment_read import (
    BankSwitchServiceNetherlandsIncomingPaymentRead,
)
from .raw_client import AsyncRawSwitchServicePaymentClient, RawSwitchServicePaymentClient


class SwitchServicePaymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSwitchServicePaymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSwitchServicePaymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSwitchServicePaymentClient
        """
        return self._raw_client

    def read_switch_service_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankSwitchServiceNetherlandsIncomingPaymentRead:
        """
        An incoming payment made towards an account of an external bank and redirected to a bunq account via switch service.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankSwitchServiceNetherlandsIncomingPaymentRead
            An incoming payment made towards an account of an external bank and redirected to a bunq account via switch service.

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
        client.switch_service_payment.read_switch_service_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_switch_service_payment_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncSwitchServicePaymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSwitchServicePaymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSwitchServicePaymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSwitchServicePaymentClient
        """
        return self._raw_client

    async def read_switch_service_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankSwitchServiceNetherlandsIncomingPaymentRead:
        """
        An incoming payment made towards an account of an external bank and redirected to a bunq account via switch service.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankSwitchServiceNetherlandsIncomingPaymentRead
            An incoming payment made towards an account of an external bank and redirected to a bunq account via switch service.

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
            await client.switch_service_payment.read_switch_service_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_switch_service_payment_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data
