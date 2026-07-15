

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_credit_note_response import CreateCreditNoteResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.credit_note_allocations_item import CreditNoteAllocationsItem
from ..types.credit_note_status import CreditNoteStatus
from ..types.credit_note_type import CreditNoteType
from ..types.currency import Currency
from ..types.currency_rate import CurrencyRate
from ..types.delete_credit_note_response import DeleteCreditNoteResponse
from ..types.get_credit_note_response import GetCreditNoteResponse
from ..types.get_credit_notes_response import GetCreditNotesResponse
from ..types.invoice_line_item import InvoiceLineItem
from ..types.linked_customer import LinkedCustomer
from ..types.linked_ledger_account import LinkedLedgerAccount
from ..types.pass_through_query import PassThroughQuery
from ..types.row_version import RowVersion
from ..types.tax_inclusive import TaxInclusive
from ..types.update_credit_note_response import UpdateCreditNoteResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from .raw_client import AsyncRawCreditNotesClient, RawCreditNotesClient


OMIT = typing.cast(typing.Any, ...)


class CreditNotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCreditNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCreditNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCreditNotesClient
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
    ) -> GetCreditNotesResponse:
        """
        List Credit Notes

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
        GetCreditNotesResponse
            Credit Notes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.credit_notes.all_(
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
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        allocations: typing.Optional[typing.Sequence[CreditNoteAllocationsItem]] = OMIT,
        balance: typing.Optional[float] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        date_issued: typing.Optional[dt.datetime] = OMIT,
        date_paid: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        line_items: typing.Optional[typing.Sequence[InvoiceLineItem]] = OMIT,
        note: typing.Optional[str] = OMIT,
        number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        remaining_credit: typing.Optional[float] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[CreditNoteStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        type: typing.Optional[CreditNoteType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCreditNoteResponse:
        """
        Create Credit Note

        Parameters
        ----------
        total_amount : float
            Amount of transaction

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        allocations : typing.Optional[typing.Sequence[CreditNoteAllocationsItem]]

        balance : typing.Optional[float]
            The balance reflecting any payments made against the transaction.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        date_issued : typing.Optional[dt.datetime]
            Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD

        date_paid : typing.Optional[dt.datetime]
            Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD

        id : typing.Optional[str]
            Unique identifier representing the entity

        line_items : typing.Optional[typing.Sequence[InvoiceLineItem]]

        note : typing.Optional[str]
            Optional note to be associated with the credit note.

        number : typing.Optional[str]
            Credit note number.

        reference : typing.Optional[str]
            Optional reference message ie: Debit remittance detail.

        remaining_credit : typing.Optional[float]
            Indicates the total credit amount still available to apply towards the payment.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[CreditNoteStatus]
            Status of credit notes

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        terms : typing.Optional[str]
            Optional terms to be associated with the credit note.

        total_tax : typing.Optional[float]
            Total tax amount applied to this invoice.

        type : typing.Optional[CreditNoteType]
            Type of payment

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCreditNoteResponse
            Credit Note created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.credit_notes.add(
            total_amount=49.99,
        )
        """
        _response = self._raw_client.add(
            total_amount=total_amount,
            raw=raw,
            account=account,
            allocations=allocations,
            balance=balance,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            customer=customer,
            date_issued=date_issued,
            date_paid=date_paid,
            id=id,
            line_items=line_items,
            note=note,
            number=number,
            reference=reference,
            remaining_credit=remaining_credit,
            row_version=row_version,
            status=status,
            sub_total=sub_total,
            tax_code=tax_code,
            tax_inclusive=tax_inclusive,
            terms=terms,
            total_tax=total_tax,
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
    ) -> GetCreditNoteResponse:
        """
        Get Credit Note

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
        GetCreditNoteResponse
            Credit Note

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.credit_notes.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCreditNoteResponse:
        """
        Delete Credit Note

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
        DeleteCreditNoteResponse
            Credit Note deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.credit_notes.delete(
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
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        allocations: typing.Optional[typing.Sequence[CreditNoteAllocationsItem]] = OMIT,
        balance: typing.Optional[float] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        date_issued: typing.Optional[dt.datetime] = OMIT,
        date_paid: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        line_items: typing.Optional[typing.Sequence[InvoiceLineItem]] = OMIT,
        note: typing.Optional[str] = OMIT,
        number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        remaining_credit: typing.Optional[float] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[CreditNoteStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        type: typing.Optional[CreditNoteType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCreditNoteResponse:
        """
        Update Credit Note

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        total_amount : float
            Amount of transaction

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        allocations : typing.Optional[typing.Sequence[CreditNoteAllocationsItem]]

        balance : typing.Optional[float]
            The balance reflecting any payments made against the transaction.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        date_issued : typing.Optional[dt.datetime]
            Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD

        date_paid : typing.Optional[dt.datetime]
            Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD

        id : typing.Optional[str]
            Unique identifier representing the entity

        line_items : typing.Optional[typing.Sequence[InvoiceLineItem]]

        note : typing.Optional[str]
            Optional note to be associated with the credit note.

        number : typing.Optional[str]
            Credit note number.

        reference : typing.Optional[str]
            Optional reference message ie: Debit remittance detail.

        remaining_credit : typing.Optional[float]
            Indicates the total credit amount still available to apply towards the payment.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[CreditNoteStatus]
            Status of credit notes

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        terms : typing.Optional[str]
            Optional terms to be associated with the credit note.

        total_tax : typing.Optional[float]
            Total tax amount applied to this invoice.

        type : typing.Optional[CreditNoteType]
            Type of payment

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCreditNoteResponse
            Credit Note updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.credit_notes.update(
            id_="id",
            total_amount=49.99,
        )
        """
        _response = self._raw_client.update(
            id_,
            total_amount=total_amount,
            raw=raw,
            account=account,
            allocations=allocations,
            balance=balance,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            customer=customer,
            date_issued=date_issued,
            date_paid=date_paid,
            id=id,
            line_items=line_items,
            note=note,
            number=number,
            reference=reference,
            remaining_credit=remaining_credit,
            row_version=row_version,
            status=status,
            sub_total=sub_total,
            tax_code=tax_code,
            tax_inclusive=tax_inclusive,
            terms=terms,
            total_tax=total_tax,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data


class AsyncCreditNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCreditNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCreditNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCreditNotesClient
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
    ) -> GetCreditNotesResponse:
        """
        List Credit Notes

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
        GetCreditNotesResponse
            Credit Notes

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
            await client.credit_notes.all_(
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
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        allocations: typing.Optional[typing.Sequence[CreditNoteAllocationsItem]] = OMIT,
        balance: typing.Optional[float] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        date_issued: typing.Optional[dt.datetime] = OMIT,
        date_paid: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        line_items: typing.Optional[typing.Sequence[InvoiceLineItem]] = OMIT,
        note: typing.Optional[str] = OMIT,
        number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        remaining_credit: typing.Optional[float] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[CreditNoteStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        type: typing.Optional[CreditNoteType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCreditNoteResponse:
        """
        Create Credit Note

        Parameters
        ----------
        total_amount : float
            Amount of transaction

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        allocations : typing.Optional[typing.Sequence[CreditNoteAllocationsItem]]

        balance : typing.Optional[float]
            The balance reflecting any payments made against the transaction.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        date_issued : typing.Optional[dt.datetime]
            Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD

        date_paid : typing.Optional[dt.datetime]
            Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD

        id : typing.Optional[str]
            Unique identifier representing the entity

        line_items : typing.Optional[typing.Sequence[InvoiceLineItem]]

        note : typing.Optional[str]
            Optional note to be associated with the credit note.

        number : typing.Optional[str]
            Credit note number.

        reference : typing.Optional[str]
            Optional reference message ie: Debit remittance detail.

        remaining_credit : typing.Optional[float]
            Indicates the total credit amount still available to apply towards the payment.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[CreditNoteStatus]
            Status of credit notes

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        terms : typing.Optional[str]
            Optional terms to be associated with the credit note.

        total_tax : typing.Optional[float]
            Total tax amount applied to this invoice.

        type : typing.Optional[CreditNoteType]
            Type of payment

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCreditNoteResponse
            Credit Note created

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
            await client.credit_notes.add(
                total_amount=49.99,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            total_amount=total_amount,
            raw=raw,
            account=account,
            allocations=allocations,
            balance=balance,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            customer=customer,
            date_issued=date_issued,
            date_paid=date_paid,
            id=id,
            line_items=line_items,
            note=note,
            number=number,
            reference=reference,
            remaining_credit=remaining_credit,
            row_version=row_version,
            status=status,
            sub_total=sub_total,
            tax_code=tax_code,
            tax_inclusive=tax_inclusive,
            terms=terms,
            total_tax=total_tax,
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
    ) -> GetCreditNoteResponse:
        """
        Get Credit Note

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
        GetCreditNoteResponse
            Credit Note

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
            await client.credit_notes.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCreditNoteResponse:
        """
        Delete Credit Note

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
        DeleteCreditNoteResponse
            Credit Note deleted

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
            await client.credit_notes.delete(
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
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        allocations: typing.Optional[typing.Sequence[CreditNoteAllocationsItem]] = OMIT,
        balance: typing.Optional[float] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        date_issued: typing.Optional[dt.datetime] = OMIT,
        date_paid: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        line_items: typing.Optional[typing.Sequence[InvoiceLineItem]] = OMIT,
        note: typing.Optional[str] = OMIT,
        number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        remaining_credit: typing.Optional[float] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[CreditNoteStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        type: typing.Optional[CreditNoteType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCreditNoteResponse:
        """
        Update Credit Note

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        total_amount : float
            Amount of transaction

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        allocations : typing.Optional[typing.Sequence[CreditNoteAllocationsItem]]

        balance : typing.Optional[float]
            The balance reflecting any payments made against the transaction.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        date_issued : typing.Optional[dt.datetime]
            Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD

        date_paid : typing.Optional[dt.datetime]
            Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD

        id : typing.Optional[str]
            Unique identifier representing the entity

        line_items : typing.Optional[typing.Sequence[InvoiceLineItem]]

        note : typing.Optional[str]
            Optional note to be associated with the credit note.

        number : typing.Optional[str]
            Credit note number.

        reference : typing.Optional[str]
            Optional reference message ie: Debit remittance detail.

        remaining_credit : typing.Optional[float]
            Indicates the total credit amount still available to apply towards the payment.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[CreditNoteStatus]
            Status of credit notes

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        terms : typing.Optional[str]
            Optional terms to be associated with the credit note.

        total_tax : typing.Optional[float]
            Total tax amount applied to this invoice.

        type : typing.Optional[CreditNoteType]
            Type of payment

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCreditNoteResponse
            Credit Note updated

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
            await client.credit_notes.update(
                id_="id",
                total_amount=49.99,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            total_amount=total_amount,
            raw=raw,
            account=account,
            allocations=allocations,
            balance=balance,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            customer=customer,
            date_issued=date_issued,
            date_paid=date_paid,
            id=id,
            line_items=line_items,
            note=note,
            number=number,
            reference=reference,
            remaining_credit=remaining_credit,
            row_version=row_version,
            status=status,
            sub_total=sub_total,
            tax_code=tax_code,
            tax_inclusive=tax_inclusive,
            terms=terms,
            total_tax=total_tax,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data
