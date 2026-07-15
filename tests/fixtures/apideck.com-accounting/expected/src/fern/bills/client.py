

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bill_line_item import BillLineItem
from ..types.bill_status import BillStatus
from ..types.bills_sort import BillsSort
from ..types.create_bill_response import CreateBillResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.currency import Currency
from ..types.currency_rate import CurrencyRate
from ..types.delete_bill_response import DeleteBillResponse
from ..types.downstream_id import DownstreamId
from ..types.get_bill_response import GetBillResponse
from ..types.get_bills_response import GetBillsResponse
from ..types.id import Id
from ..types.linked_ledger_account import LinkedLedgerAccount
from ..types.linked_supplier import LinkedSupplier
from ..types.pass_through_query import PassThroughQuery
from ..types.row_version import RowVersion
from ..types.tax_inclusive import TaxInclusive
from ..types.update_bill_response import UpdateBillResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from .raw_client import AsyncRawBillsClient, RawBillsClient


OMIT = typing.cast(typing.Any, ...)


class BillsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBillsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBillsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBillsClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[BillsSort] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetBillsResponse:
        """
        List Bills

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[BillsSort]
            Apply sorting

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBillsResponse
            Bills

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.bills.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            sort=sort,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        balance: typing.Optional[float] = OMIT,
        bill_date: typing.Optional[dt.date] = OMIT,
        bill_number: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        deposit: typing.Optional[float] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        due_date: typing.Optional[dt.date] = OMIT,
        id: typing.Optional[Id] = OMIT,
        ledger_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        line_items: typing.Optional[typing.Sequence[BillLineItem]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        paid_date: typing.Optional[dt.date] = OMIT,
        po_number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[BillStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        supplier: typing.Optional[LinkedSupplier] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total: typing.Optional[float] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateBillResponse:
        """
        Create Bill

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        balance : typing.Optional[float]
            Balance of bill due.

        bill_date : typing.Optional[dt.date]
            Date bill was issued - YYYY-MM-DD.

        bill_number : typing.Optional[str]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        deposit : typing.Optional[float]
            Amount of deposit made to this bill.

        downstream_id : typing.Optional[DownstreamId]

        due_date : typing.Optional[dt.date]
            The due date is the date on which a payment is scheduled to be received by the supplier - YYYY-MM-DD.

        id : typing.Optional[Id]

        ledger_account : typing.Optional[LinkedLedgerAccount]

        line_items : typing.Optional[typing.Sequence[BillLineItem]]

        notes : typing.Optional[str]

        paid_date : typing.Optional[dt.date]
            The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD.

        po_number : typing.Optional[str]
            A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.

        reference : typing.Optional[str]
            Optional bill reference.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[BillStatus]
            Invoice status

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        supplier : typing.Optional[LinkedSupplier]

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        terms : typing.Optional[str]
            Terms of payment.

        total : typing.Optional[float]
            Total amount of bill, including tax.

        total_tax : typing.Optional[float]
            Total tax amount applied to this bill.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBillResponse
            Bill created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.bills.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            balance=balance,
            bill_date=bill_date,
            bill_number=bill_number,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            deposit=deposit,
            downstream_id=downstream_id,
            due_date=due_date,
            id=id,
            ledger_account=ledger_account,
            line_items=line_items,
            notes=notes,
            paid_date=paid_date,
            po_number=po_number,
            reference=reference,
            row_version=row_version,
            status=status,
            sub_total=sub_total,
            supplier=supplier,
            tax_code=tax_code,
            tax_inclusive=tax_inclusive,
            terms=terms,
            total=total,
            total_tax=total_tax,
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
    ) -> GetBillResponse:
        """
        Get Bill

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
        GetBillResponse
            Bill

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.bills.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteBillResponse:
        """
        Delete Bill

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
        DeleteBillResponse
            Bill deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.bills.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        balance: typing.Optional[float] = OMIT,
        bill_date: typing.Optional[dt.date] = OMIT,
        bill_number: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        deposit: typing.Optional[float] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        due_date: typing.Optional[dt.date] = OMIT,
        id: typing.Optional[Id] = OMIT,
        ledger_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        line_items: typing.Optional[typing.Sequence[BillLineItem]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        paid_date: typing.Optional[dt.date] = OMIT,
        po_number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[BillStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        supplier: typing.Optional[LinkedSupplier] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total: typing.Optional[float] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateBillResponse:
        """
        Update Bill

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        balance : typing.Optional[float]
            Balance of bill due.

        bill_date : typing.Optional[dt.date]
            Date bill was issued - YYYY-MM-DD.

        bill_number : typing.Optional[str]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        deposit : typing.Optional[float]
            Amount of deposit made to this bill.

        downstream_id : typing.Optional[DownstreamId]

        due_date : typing.Optional[dt.date]
            The due date is the date on which a payment is scheduled to be received by the supplier - YYYY-MM-DD.

        id : typing.Optional[Id]

        ledger_account : typing.Optional[LinkedLedgerAccount]

        line_items : typing.Optional[typing.Sequence[BillLineItem]]

        notes : typing.Optional[str]

        paid_date : typing.Optional[dt.date]
            The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD.

        po_number : typing.Optional[str]
            A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.

        reference : typing.Optional[str]
            Optional bill reference.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[BillStatus]
            Invoice status

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        supplier : typing.Optional[LinkedSupplier]

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        terms : typing.Optional[str]
            Terms of payment.

        total : typing.Optional[float]
            Total amount of bill, including tax.

        total_tax : typing.Optional[float]
            Total tax amount applied to this bill.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateBillResponse
            Bill Updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.bills.update(
            id_="id",
        )
        """
        _response = self._raw_client.update(
            id_,
            raw=raw,
            balance=balance,
            bill_date=bill_date,
            bill_number=bill_number,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            deposit=deposit,
            downstream_id=downstream_id,
            due_date=due_date,
            id=id,
            ledger_account=ledger_account,
            line_items=line_items,
            notes=notes,
            paid_date=paid_date,
            po_number=po_number,
            reference=reference,
            row_version=row_version,
            status=status,
            sub_total=sub_total,
            supplier=supplier,
            tax_code=tax_code,
            tax_inclusive=tax_inclusive,
            terms=terms,
            total=total,
            total_tax=total_tax,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data


class AsyncBillsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBillsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBillsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBillsClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[BillsSort] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetBillsResponse:
        """
        List Bills

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[BillsSort]
            Apply sorting

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBillsResponse
            Bills

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
            await client.bills.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            sort=sort,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        balance: typing.Optional[float] = OMIT,
        bill_date: typing.Optional[dt.date] = OMIT,
        bill_number: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        deposit: typing.Optional[float] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        due_date: typing.Optional[dt.date] = OMIT,
        id: typing.Optional[Id] = OMIT,
        ledger_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        line_items: typing.Optional[typing.Sequence[BillLineItem]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        paid_date: typing.Optional[dt.date] = OMIT,
        po_number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[BillStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        supplier: typing.Optional[LinkedSupplier] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total: typing.Optional[float] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateBillResponse:
        """
        Create Bill

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        balance : typing.Optional[float]
            Balance of bill due.

        bill_date : typing.Optional[dt.date]
            Date bill was issued - YYYY-MM-DD.

        bill_number : typing.Optional[str]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        deposit : typing.Optional[float]
            Amount of deposit made to this bill.

        downstream_id : typing.Optional[DownstreamId]

        due_date : typing.Optional[dt.date]
            The due date is the date on which a payment is scheduled to be received by the supplier - YYYY-MM-DD.

        id : typing.Optional[Id]

        ledger_account : typing.Optional[LinkedLedgerAccount]

        line_items : typing.Optional[typing.Sequence[BillLineItem]]

        notes : typing.Optional[str]

        paid_date : typing.Optional[dt.date]
            The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD.

        po_number : typing.Optional[str]
            A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.

        reference : typing.Optional[str]
            Optional bill reference.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[BillStatus]
            Invoice status

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        supplier : typing.Optional[LinkedSupplier]

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        terms : typing.Optional[str]
            Terms of payment.

        total : typing.Optional[float]
            Total amount of bill, including tax.

        total_tax : typing.Optional[float]
            Total tax amount applied to this bill.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBillResponse
            Bill created

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
            await client.bills.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            balance=balance,
            bill_date=bill_date,
            bill_number=bill_number,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            deposit=deposit,
            downstream_id=downstream_id,
            due_date=due_date,
            id=id,
            ledger_account=ledger_account,
            line_items=line_items,
            notes=notes,
            paid_date=paid_date,
            po_number=po_number,
            reference=reference,
            row_version=row_version,
            status=status,
            sub_total=sub_total,
            supplier=supplier,
            tax_code=tax_code,
            tax_inclusive=tax_inclusive,
            terms=terms,
            total=total,
            total_tax=total_tax,
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
    ) -> GetBillResponse:
        """
        Get Bill

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
        GetBillResponse
            Bill

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
            await client.bills.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteBillResponse:
        """
        Delete Bill

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
        DeleteBillResponse
            Bill deleted

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
            await client.bills.delete(
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
        raw: typing.Optional[bool] = None,
        balance: typing.Optional[float] = OMIT,
        bill_date: typing.Optional[dt.date] = OMIT,
        bill_number: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        deposit: typing.Optional[float] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        due_date: typing.Optional[dt.date] = OMIT,
        id: typing.Optional[Id] = OMIT,
        ledger_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        line_items: typing.Optional[typing.Sequence[BillLineItem]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        paid_date: typing.Optional[dt.date] = OMIT,
        po_number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[BillStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        supplier: typing.Optional[LinkedSupplier] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total: typing.Optional[float] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateBillResponse:
        """
        Update Bill

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        balance : typing.Optional[float]
            Balance of bill due.

        bill_date : typing.Optional[dt.date]
            Date bill was issued - YYYY-MM-DD.

        bill_number : typing.Optional[str]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        deposit : typing.Optional[float]
            Amount of deposit made to this bill.

        downstream_id : typing.Optional[DownstreamId]

        due_date : typing.Optional[dt.date]
            The due date is the date on which a payment is scheduled to be received by the supplier - YYYY-MM-DD.

        id : typing.Optional[Id]

        ledger_account : typing.Optional[LinkedLedgerAccount]

        line_items : typing.Optional[typing.Sequence[BillLineItem]]

        notes : typing.Optional[str]

        paid_date : typing.Optional[dt.date]
            The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD.

        po_number : typing.Optional[str]
            A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.

        reference : typing.Optional[str]
            Optional bill reference.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[BillStatus]
            Invoice status

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        supplier : typing.Optional[LinkedSupplier]

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        terms : typing.Optional[str]
            Terms of payment.

        total : typing.Optional[float]
            Total amount of bill, including tax.

        total_tax : typing.Optional[float]
            Total tax amount applied to this bill.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateBillResponse
            Bill Updated

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
            await client.bills.update(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            raw=raw,
            balance=balance,
            bill_date=bill_date,
            bill_number=bill_number,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            deposit=deposit,
            downstream_id=downstream_id,
            due_date=due_date,
            id=id,
            ledger_account=ledger_account,
            line_items=line_items,
            notes=notes,
            paid_date=paid_date,
            po_number=po_number,
            reference=reference,
            row_version=row_version,
            status=status,
            sub_total=sub_total,
            supplier=supplier,
            tax_code=tax_code,
            tax_inclusive=tax_inclusive,
            terms=terms,
            total=total,
            total_tax=total_tax,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data
