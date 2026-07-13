

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.confirmation_of_funds_create import ConfirmationOfFundsCreate
from ..types.pointer import Pointer
from .raw_client import AsyncRawConfirmationOfFundsClient, RawConfirmationOfFundsClient


OMIT = typing.cast(typing.Any, ...)


class ConfirmationOfFundsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConfirmationOfFundsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConfirmationOfFundsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConfirmationOfFundsClient
        """
        return self._raw_client

    def create_confirmation_of_funds_for_user(
        self,
        user_id: int,
        *,
        amount: Amount,
        pointer_iban: Pointer,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConfirmationOfFundsCreate:
        """
        Used to confirm availability of funds on an account.

        Parameters
        ----------
        user_id : int


        amount : Amount
            The amount we want to check for.

        pointer_iban : Pointer
            The pointer (IBAN) of the account we're querying.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfirmationOfFundsCreate
            Used to confirm availability of funds on an account.

        Examples
        --------
        from fern import Amount, FernApi, Pointer

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.confirmation_of_funds.create_confirmation_of_funds_for_user(
            user_id=1,
            amount=Amount(),
            pointer_iban=Pointer(),
        )
        """
        _response = self._raw_client.create_confirmation_of_funds_for_user(
            user_id, amount=amount, pointer_iban=pointer_iban, request_options=request_options
        )
        return _response.data


class AsyncConfirmationOfFundsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConfirmationOfFundsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConfirmationOfFundsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConfirmationOfFundsClient
        """
        return self._raw_client

    async def create_confirmation_of_funds_for_user(
        self,
        user_id: int,
        *,
        amount: Amount,
        pointer_iban: Pointer,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConfirmationOfFundsCreate:
        """
        Used to confirm availability of funds on an account.

        Parameters
        ----------
        user_id : int


        amount : Amount
            The amount we want to check for.

        pointer_iban : Pointer
            The pointer (IBAN) of the account we're querying.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfirmationOfFundsCreate
            Used to confirm availability of funds on an account.

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi, Pointer

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.confirmation_of_funds.create_confirmation_of_funds_for_user(
                user_id=1,
                amount=Amount(),
                pointer_iban=Pointer(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_confirmation_of_funds_for_user(
            user_id, amount=amount, pointer_iban=pointer_iban, request_options=request_options
        )
        return _response.data
