

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_payment_response import CreatePaymentResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.currency import Currency
from ..types.currency_rate import CurrencyRate
from ..types.delete_payment_response import DeletePaymentResponse
from ..types.downstream_id import DownstreamId
from ..types.get_payment_response import GetPaymentResponse
from ..types.get_payments_response import GetPaymentsResponse
from ..types.linked_customer import LinkedCustomer
from ..types.linked_ledger_account import LinkedLedgerAccount
from ..types.linked_supplier import LinkedSupplier
from ..types.pass_through_query import PassThroughQuery
from ..types.payment_allocations_item import PaymentAllocationsItem
from ..types.payment_status import PaymentStatus
from ..types.payment_type import PaymentType
from ..types.row_version import RowVersion
from ..types.update_payment_response import UpdatePaymentResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from .raw_client import AsyncRawPaymentsClient, RawPaymentsClient


OMIT = typing.cast(typing.Any, ...)


class PaymentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentsClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPaymentsResponse:
        """
        List Payments

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPaymentsResponse
            Payments

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.payments.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def add(
        self,
        *,
        total_amount: float,
        transaction_date: dt.datetime,
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        accounts_receivable_account_id: typing.Optional[str] = OMIT,
        accounts_receivable_account_type: typing.Optional[str] = OMIT,
        allocations: typing.Optional[typing.Sequence[PaymentAllocationsItem]] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        id: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        payment_method: typing.Optional[str] = OMIT,
        payment_method_id: typing.Optional[str] = OMIT,
        payment_method_reference: typing.Optional[str] = OMIT,
        reconciled: typing.Optional[bool] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[PaymentStatus] = OMIT,
        supplier: typing.Optional[LinkedSupplier] = OMIT,
        type: typing.Optional[PaymentType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatePaymentResponse:
        """
        Create Payment

        Parameters
        ----------
        total_amount : float
            Amount of payment

        transaction_date : dt.datetime
            Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        accounts_receivable_account_id : typing.Optional[str]
            Unique identifier for the account to allocate payment to.

        accounts_receivable_account_type : typing.Optional[str]
            Type of accounts receivable account.

        allocations : typing.Optional[typing.Sequence[PaymentAllocationsItem]]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        display_id : typing.Optional[str]
            Payment id to be displayed.

        downstream_id : typing.Optional[DownstreamId]

        id : typing.Optional[str]
            Unique identifier representing the entity

        note : typing.Optional[str]
            Optional note to be associated with the payment.

        payment_method : typing.Optional[str]
            Payment method name

        payment_method_id : typing.Optional[str]
            Unique identifier for the payment method.

        payment_method_reference : typing.Optional[str]
            Optional reference message returned by payment method on processing

        reconciled : typing.Optional[bool]
            Payment has been reconciled

        reference : typing.Optional[str]
            Optional payment reference message ie: Debit remittance detail.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[PaymentStatus]
            Status of payment

        supplier : typing.Optional[LinkedSupplier]

        type : typing.Optional[PaymentType]
            Type of payment

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePaymentResponse
            Payment created

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.payments.add(
            total_amount=49.99,
            transaction_date=datetime.datetime.fromisoformat(
                "2021-05-01 12:00:00+00:00",
            ),
        )
        """
        _response = self._raw_client.add(
            total_amount=total_amount,
            transaction_date=transaction_date,
            raw=raw,
            account=account,
            accounts_receivable_account_id=accounts_receivable_account_id,
            accounts_receivable_account_type=accounts_receivable_account_type,
            allocations=allocations,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            customer=customer,
            display_id=display_id,
            downstream_id=downstream_id,
            id=id,
            note=note,
            payment_method=payment_method,
            payment_method_id=payment_method_id,
            payment_method_reference=payment_method_reference,
            reconciled=reconciled,
            reference=reference,
            row_version=row_version,
            status=status,
            supplier=supplier,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPaymentResponse:
        """
        Get Payment

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPaymentResponse
            Payment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.payments.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePaymentResponse:
        """
        Delete Payment

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePaymentResponse
            Payment deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.payments.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        total_amount: float,
        transaction_date: dt.datetime,
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        accounts_receivable_account_id: typing.Optional[str] = OMIT,
        accounts_receivable_account_type: typing.Optional[str] = OMIT,
        allocations: typing.Optional[typing.Sequence[PaymentAllocationsItem]] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        id: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        payment_method: typing.Optional[str] = OMIT,
        payment_method_id: typing.Optional[str] = OMIT,
        payment_method_reference: typing.Optional[str] = OMIT,
        reconciled: typing.Optional[bool] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[PaymentStatus] = OMIT,
        supplier: typing.Optional[LinkedSupplier] = OMIT,
        type: typing.Optional[PaymentType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePaymentResponse:
        """
        Update Payment

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        total_amount : float
            Amount of payment

        transaction_date : dt.datetime
            Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        accounts_receivable_account_id : typing.Optional[str]
            Unique identifier for the account to allocate payment to.

        accounts_receivable_account_type : typing.Optional[str]
            Type of accounts receivable account.

        allocations : typing.Optional[typing.Sequence[PaymentAllocationsItem]]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        display_id : typing.Optional[str]
            Payment id to be displayed.

        downstream_id : typing.Optional[DownstreamId]

        id : typing.Optional[str]
            Unique identifier representing the entity

        note : typing.Optional[str]
            Optional note to be associated with the payment.

        payment_method : typing.Optional[str]
            Payment method name

        payment_method_id : typing.Optional[str]
            Unique identifier for the payment method.

        payment_method_reference : typing.Optional[str]
            Optional reference message returned by payment method on processing

        reconciled : typing.Optional[bool]
            Payment has been reconciled

        reference : typing.Optional[str]
            Optional payment reference message ie: Debit remittance detail.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[PaymentStatus]
            Status of payment

        supplier : typing.Optional[LinkedSupplier]

        type : typing.Optional[PaymentType]
            Type of payment

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePaymentResponse
            Payment Updated

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.payments.update(
            id_="id",
            total_amount=49.99,
            transaction_date=datetime.datetime.fromisoformat(
                "2021-05-01 12:00:00+00:00",
            ),
        )
        """
        _response = self._raw_client.update(
            id_,
            total_amount=total_amount,
            transaction_date=transaction_date,
            raw=raw,
            account=account,
            accounts_receivable_account_id=accounts_receivable_account_id,
            accounts_receivable_account_type=accounts_receivable_account_type,
            allocations=allocations,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            customer=customer,
            display_id=display_id,
            downstream_id=downstream_id,
            id=id,
            note=note,
            payment_method=payment_method,
            payment_method_id=payment_method_id,
            payment_method_reference=payment_method_reference,
            reconciled=reconciled,
            reference=reference,
            row_version=row_version,
            status=status,
            supplier=supplier,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data


class AsyncPaymentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentsClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPaymentsResponse:
        """
        List Payments

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPaymentsResponse
            Payments

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def add(
        self,
        *,
        total_amount: float,
        transaction_date: dt.datetime,
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        accounts_receivable_account_id: typing.Optional[str] = OMIT,
        accounts_receivable_account_type: typing.Optional[str] = OMIT,
        allocations: typing.Optional[typing.Sequence[PaymentAllocationsItem]] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        id: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        payment_method: typing.Optional[str] = OMIT,
        payment_method_id: typing.Optional[str] = OMIT,
        payment_method_reference: typing.Optional[str] = OMIT,
        reconciled: typing.Optional[bool] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[PaymentStatus] = OMIT,
        supplier: typing.Optional[LinkedSupplier] = OMIT,
        type: typing.Optional[PaymentType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatePaymentResponse:
        """
        Create Payment

        Parameters
        ----------
        total_amount : float
            Amount of payment

        transaction_date : dt.datetime
            Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        accounts_receivable_account_id : typing.Optional[str]
            Unique identifier for the account to allocate payment to.

        accounts_receivable_account_type : typing.Optional[str]
            Type of accounts receivable account.

        allocations : typing.Optional[typing.Sequence[PaymentAllocationsItem]]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        display_id : typing.Optional[str]
            Payment id to be displayed.

        downstream_id : typing.Optional[DownstreamId]

        id : typing.Optional[str]
            Unique identifier representing the entity

        note : typing.Optional[str]
            Optional note to be associated with the payment.

        payment_method : typing.Optional[str]
            Payment method name

        payment_method_id : typing.Optional[str]
            Unique identifier for the payment method.

        payment_method_reference : typing.Optional[str]
            Optional reference message returned by payment method on processing

        reconciled : typing.Optional[bool]
            Payment has been reconciled

        reference : typing.Optional[str]
            Optional payment reference message ie: Debit remittance detail.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[PaymentStatus]
            Status of payment

        supplier : typing.Optional[LinkedSupplier]

        type : typing.Optional[PaymentType]
            Type of payment

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePaymentResponse
            Payment created

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.add(
                total_amount=49.99,
                transaction_date=datetime.datetime.fromisoformat(
                    "2021-05-01 12:00:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            total_amount=total_amount,
            transaction_date=transaction_date,
            raw=raw,
            account=account,
            accounts_receivable_account_id=accounts_receivable_account_id,
            accounts_receivable_account_type=accounts_receivable_account_type,
            allocations=allocations,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            customer=customer,
            display_id=display_id,
            downstream_id=downstream_id,
            id=id,
            note=note,
            payment_method=payment_method,
            payment_method_id=payment_method_id,
            payment_method_reference=payment_method_reference,
            reconciled=reconciled,
            reference=reference,
            row_version=row_version,
            status=status,
            supplier=supplier,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPaymentResponse:
        """
        Get Payment

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPaymentResponse
            Payment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePaymentResponse:
        """
        Delete Payment

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePaymentResponse
            Payment deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def update(
        self,
        id_: str,
        *,
        total_amount: float,
        transaction_date: dt.datetime,
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        accounts_receivable_account_id: typing.Optional[str] = OMIT,
        accounts_receivable_account_type: typing.Optional[str] = OMIT,
        allocations: typing.Optional[typing.Sequence[PaymentAllocationsItem]] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        id: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        payment_method: typing.Optional[str] = OMIT,
        payment_method_id: typing.Optional[str] = OMIT,
        payment_method_reference: typing.Optional[str] = OMIT,
        reconciled: typing.Optional[bool] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[PaymentStatus] = OMIT,
        supplier: typing.Optional[LinkedSupplier] = OMIT,
        type: typing.Optional[PaymentType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePaymentResponse:
        """
        Update Payment

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        total_amount : float
            Amount of payment

        transaction_date : dt.datetime
            Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        accounts_receivable_account_id : typing.Optional[str]
            Unique identifier for the account to allocate payment to.

        accounts_receivable_account_type : typing.Optional[str]
            Type of accounts receivable account.

        allocations : typing.Optional[typing.Sequence[PaymentAllocationsItem]]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        display_id : typing.Optional[str]
            Payment id to be displayed.

        downstream_id : typing.Optional[DownstreamId]

        id : typing.Optional[str]
            Unique identifier representing the entity

        note : typing.Optional[str]
            Optional note to be associated with the payment.

        payment_method : typing.Optional[str]
            Payment method name

        payment_method_id : typing.Optional[str]
            Unique identifier for the payment method.

        payment_method_reference : typing.Optional[str]
            Optional reference message returned by payment method on processing

        reconciled : typing.Optional[bool]
            Payment has been reconciled

        reference : typing.Optional[str]
            Optional payment reference message ie: Debit remittance detail.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[PaymentStatus]
            Status of payment

        supplier : typing.Optional[LinkedSupplier]

        type : typing.Optional[PaymentType]
            Type of payment

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePaymentResponse
            Payment Updated

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.update(
                id_="id",
                total_amount=49.99,
                transaction_date=datetime.datetime.fromisoformat(
                    "2021-05-01 12:00:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            total_amount=total_amount,
            transaction_date=transaction_date,
            raw=raw,
            account=account,
            accounts_receivable_account_id=accounts_receivable_account_id,
            accounts_receivable_account_type=accounts_receivable_account_type,
            allocations=allocations,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            customer=customer,
            display_id=display_id,
            downstream_id=downstream_id,
            id=id,
            note=note,
            payment_method=payment_method,
            payment_method_id=payment_method_id,
            payment_method_reference=payment_method_reference,
            reconciled=reconciled,
            reference=reference,
            row_version=row_version,
            status=status,
            supplier=supplier,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data
