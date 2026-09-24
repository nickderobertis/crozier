

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_customer_invoice_by_id_response import GetCustomerInvoiceByIdResponse
from ..types.list_customer_invoices_response import ListCustomerInvoicesResponse
from .raw_client import AsyncRawCustomerInvoicesClient, RawCustomerInvoicesClient
from .types.get_customer_invoices_request_sort_field import GetCustomerInvoicesRequestSortField
from .types.get_customer_invoices_request_sort_order import GetCustomerInvoicesRequestSortOrder


class CustomerInvoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomerInvoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomerInvoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomerInvoicesClient
        """
        return self._raw_client

    def get_customer_invoices(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetCustomerInvoicesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetCustomerInvoicesRequestSortField] = None,
        customer_id: typing.Optional[float] = None,
        job_id: typing.Optional[float] = None,
        invoice_number: typing.Optional[str] = None,
        due_before: typing.Optional[dt.datetime] = None,
        due_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomerInvoicesResponse:
        """
        Returns a list of invoices. The list can be filtered by customer, job, invoice number, and due dates.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetCustomerInvoicesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetCustomerInvoicesRequestSortField]

        customer_id : typing.Optional[float]
            Filter by customer ID

        job_id : typing.Optional[float]
            Filter by job ID

        invoice_number : typing.Optional[str]
            Search by invoiceNumber

        due_before : typing.Optional[dt.datetime]
            Filter invoices due before this datetime

        due_after : typing.Optional[dt.datetime]
            Filter invoices due after this datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomerInvoicesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customer_invoices.get_customer_invoices()
        """
        _response = self._raw_client.get_customer_invoices(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            customer_id=customer_id,
            job_id=job_id,
            invoice_number=invoice_number,
            due_before=due_before,
            due_after=due_after,
            request_options=request_options,
        )
        return _response.data

    def get_customer_invoices_invoice_id(
        self, invoice_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerInvoiceByIdResponse:
        """
        Returns a single invoice by ID with customer details and sections

        Parameters
        ----------
        invoice_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerInvoiceByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customer_invoices.get_customer_invoices_invoice_id(
            invoice_id=1.1,
        )
        """
        _response = self._raw_client.get_customer_invoices_invoice_id(invoice_id, request_options=request_options)
        return _response.data


class AsyncCustomerInvoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomerInvoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomerInvoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomerInvoicesClient
        """
        return self._raw_client

    async def get_customer_invoices(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetCustomerInvoicesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetCustomerInvoicesRequestSortField] = None,
        customer_id: typing.Optional[float] = None,
        job_id: typing.Optional[float] = None,
        invoice_number: typing.Optional[str] = None,
        due_before: typing.Optional[dt.datetime] = None,
        due_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomerInvoicesResponse:
        """
        Returns a list of invoices. The list can be filtered by customer, job, invoice number, and due dates.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetCustomerInvoicesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetCustomerInvoicesRequestSortField]

        customer_id : typing.Optional[float]
            Filter by customer ID

        job_id : typing.Optional[float]
            Filter by job ID

        invoice_number : typing.Optional[str]
            Search by invoiceNumber

        due_before : typing.Optional[dt.datetime]
            Filter invoices due before this datetime

        due_after : typing.Optional[dt.datetime]
            Filter invoices due after this datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomerInvoicesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_invoices.get_customer_invoices()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customer_invoices(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            customer_id=customer_id,
            job_id=job_id,
            invoice_number=invoice_number,
            due_before=due_before,
            due_after=due_after,
            request_options=request_options,
        )
        return _response.data

    async def get_customer_invoices_invoice_id(
        self, invoice_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerInvoiceByIdResponse:
        """
        Returns a single invoice by ID with customer details and sections

        Parameters
        ----------
        invoice_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerInvoiceByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_invoices.get_customer_invoices_invoice_id(
                invoice_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customer_invoices_invoice_id(invoice_id, request_options=request_options)
        return _response.data
