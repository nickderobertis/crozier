

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_statement_payment import ExportStatementPayment
from ..types.export_statement_payment_create import ExportStatementPaymentCreate
from ..types.export_statement_payment_read import ExportStatementPaymentRead
from .raw_client import AsyncRawStatementClient, RawStatementClient


OMIT = typing.cast(typing.Any, ...)


class StatementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatementClient
        """
        return self._raw_client

    def create_statement_for_user_monetary_account_event(
        self,
        user_id: int,
        monetary_account_id: int,
        event_id: int,
        *,
        request: ExportStatementPayment,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementPaymentCreate:
        """
        Used to create a statement export of a single payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        event_id : int


        request : ExportStatementPayment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementPaymentCreate
            Used to create a statement export of a single payment.

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
        client.statement.create_statement_for_user_monetary_account_event(
            user_id=1,
            monetary_account_id=1,
            event_id=1,
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_statement_for_user_monetary_account_event(
            user_id, monetary_account_id, event_id, request=request, request_options=request_options
        )
        return _response.data

    def read_statement_for_user_monetary_account_event(
        self,
        user_id: int,
        monetary_account_id: int,
        event_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementPaymentRead:
        """
        Used to create a statement export of a single payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        event_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementPaymentRead
            Used to create a statement export of a single payment.

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
        client.statement.read_statement_for_user_monetary_account_event(
            user_id=1,
            monetary_account_id=1,
            event_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_statement_for_user_monetary_account_event(
            user_id, monetary_account_id, event_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncStatementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatementClient
        """
        return self._raw_client

    async def create_statement_for_user_monetary_account_event(
        self,
        user_id: int,
        monetary_account_id: int,
        event_id: int,
        *,
        request: ExportStatementPayment,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementPaymentCreate:
        """
        Used to create a statement export of a single payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        event_id : int


        request : ExportStatementPayment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementPaymentCreate
            Used to create a statement export of a single payment.

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
            await client.statement.create_statement_for_user_monetary_account_event(
                user_id=1,
                monetary_account_id=1,
                event_id=1,
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_statement_for_user_monetary_account_event(
            user_id, monetary_account_id, event_id, request=request, request_options=request_options
        )
        return _response.data

    async def read_statement_for_user_monetary_account_event(
        self,
        user_id: int,
        monetary_account_id: int,
        event_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementPaymentRead:
        """
        Used to create a statement export of a single payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        event_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementPaymentRead
            Used to create a statement export of a single payment.

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
            await client.statement.read_statement_for_user_monetary_account_event(
                user_id=1,
                monetary_account_id=1,
                event_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_statement_for_user_monetary_account_event(
            user_id, monetary_account_id, event_id, item_id, request_options=request_options
        )
        return _response.data
