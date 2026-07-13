

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.transferwise_quote_temporary_create import TransferwiseQuoteTemporaryCreate
from ..types.transferwise_quote_temporary_read import TransferwiseQuoteTemporaryRead
from .raw_client import AsyncRawTransferwiseQuoteTemporaryClient, RawTransferwiseQuoteTemporaryClient


OMIT = typing.cast(typing.Any, ...)


class TransferwiseQuoteTemporaryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransferwiseQuoteTemporaryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransferwiseQuoteTemporaryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransferwiseQuoteTemporaryClient
        """
        return self._raw_client

    def create_transferwise_quote_temporary_for_user(
        self,
        user_id: int,
        *,
        currency_source: str,
        currency_target: str,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseQuoteTemporaryCreate:
        """
        Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

        Parameters
        ----------
        user_id : int


        currency_source : str
            The source currency.

        currency_target : str
            The target currency.

        amount_source : typing.Optional[Amount]
            The source amount. Required if target amount is left empty.

        amount_target : typing.Optional[Amount]
            The target amount. Required if source amount is left empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseQuoteTemporaryCreate
            Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

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
        client.transferwise_quote_temporary.create_transferwise_quote_temporary_for_user(
            user_id=1,
            currency_source="currency_source",
            currency_target="currency_target",
        )
        """
        _response = self._raw_client.create_transferwise_quote_temporary_for_user(
            user_id,
            currency_source=currency_source,
            currency_target=currency_target,
            amount_source=amount_source,
            amount_target=amount_target,
            request_options=request_options,
        )
        return _response.data

    def read_transferwise_quote_temporary_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransferwiseQuoteTemporaryRead:
        """
        Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseQuoteTemporaryRead
            Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

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
        client.transferwise_quote_temporary.read_transferwise_quote_temporary_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_transferwise_quote_temporary_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncTransferwiseQuoteTemporaryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransferwiseQuoteTemporaryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransferwiseQuoteTemporaryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransferwiseQuoteTemporaryClient
        """
        return self._raw_client

    async def create_transferwise_quote_temporary_for_user(
        self,
        user_id: int,
        *,
        currency_source: str,
        currency_target: str,
        amount_source: typing.Optional[Amount] = OMIT,
        amount_target: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferwiseQuoteTemporaryCreate:
        """
        Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

        Parameters
        ----------
        user_id : int


        currency_source : str
            The source currency.

        currency_target : str
            The target currency.

        amount_source : typing.Optional[Amount]
            The source amount. Required if target amount is left empty.

        amount_target : typing.Optional[Amount]
            The target amount. Required if source amount is left empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseQuoteTemporaryCreate
            Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

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
            await client.transferwise_quote_temporary.create_transferwise_quote_temporary_for_user(
                user_id=1,
                currency_source="currency_source",
                currency_target="currency_target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_transferwise_quote_temporary_for_user(
            user_id,
            currency_source=currency_source,
            currency_target=currency_target,
            amount_source=amount_source,
            amount_target=amount_target,
            request_options=request_options,
        )
        return _response.data

    async def read_transferwise_quote_temporary_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransferwiseQuoteTemporaryRead:
        """
        Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferwiseQuoteTemporaryRead
            Used to get temporary quotes from Transferwise. These cannot be used to initiate payments

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
            await client.transferwise_quote_temporary.read_transferwise_quote_temporary_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_transferwise_quote_temporary_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
