

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cancel_invoice_response import CancelInvoiceResponse
from ..types.create_invoice_response import CreateInvoiceResponse
from ..types.delete_invoice_response import DeleteInvoiceResponse
from ..types.get_invoice_response import GetInvoiceResponse
from ..types.invoice import Invoice
from ..types.invoice_query import InvoiceQuery
from ..types.list_invoices_response import ListInvoicesResponse
from ..types.publish_invoice_response import PublishInvoiceResponse
from ..types.search_invoices_response import SearchInvoicesResponse
from ..types.update_invoice_response import UpdateInvoiceResponse
from .raw_client import AsyncRawInvoicesClient, RawInvoicesClient


OMIT = typing.cast(typing.Any, ...)


class InvoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInvoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInvoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInvoicesClient
        """
        return self._raw_client

    def list_invoices(
        self,
        *,
        location_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListInvoicesResponse:
        """
        Returns a list of invoices for a given location. The response
        is paginated. If truncated, the response includes a `cursor` that you
        use in a subsequent request to retrieve the next set of invoices.

        Parameters
        ----------
        location_id : str
            The ID of the location for which to list invoices.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of invoices to return (200 is the maximum `limit`).
            If not provided, the server uses a default limit of 100 invoices.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListInvoicesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.invoices.list_invoices(
            location_id="location_id",
        )
        """
        _response = self._raw_client.list_invoices(
            location_id=location_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    def create_invoice(
        self,
        *,
        invoice: Invoice,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateInvoiceResponse:
        """
        Creates a draft [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice)
        for an order created using the Orders API.

        A draft invoice remains in your account and no action is taken.
        You must publish the invoice before Square can process it (send it to the customer's email address or charge the customer’s card on file).

        Parameters
        ----------
        invoice : Invoice

        idempotency_key : typing.Optional[str]
            A unique string that identifies the `CreateInvoice` request. If you do not
            provide `idempotency_key` (or provide an empty string as the value), the endpoint
            treats each request as independent.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateInvoiceResponse
            Success

        Examples
        --------
        from fern import FernApi, Invoice

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.invoices.create_invoice(
            invoice=Invoice(),
        )
        """
        _response = self._raw_client.create_invoice(
            invoice=invoice, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def search_invoices(
        self,
        *,
        query: InvoiceQuery,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchInvoicesResponse:
        """
        Searches for invoices from a location specified in
        the filter. You can optionally specify customers in the filter for whom to
        retrieve invoices. In the current implementation, you can only specify one location and
        optionally one customer.

        The response is paginated. If truncated, the response includes a `cursor`
        that you use in a subsequent request to retrieve the next set of invoices.

        Parameters
        ----------
        query : InvoiceQuery

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of invoices to return (200 is the maximum `limit`).
            If not provided, the server uses a default limit of 100 invoices.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchInvoicesResponse
            Success

        Examples
        --------
        from fern import FernApi, InvoiceFilter, InvoiceQuery

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.invoices.search_invoices(
            query=InvoiceQuery(
                filter=InvoiceFilter(
                    location_ids=["location_ids"],
                ),
            ),
        )
        """
        _response = self._raw_client.search_invoices(
            query=query, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    def get_invoice(
        self, invoice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetInvoiceResponse:
        """
        Retrieves an invoice by invoice ID.

        Parameters
        ----------
        invoice_id : str
            The ID of the invoice to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetInvoiceResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.invoices.get_invoice(
            invoice_id="invoice_id",
        )
        """
        _response = self._raw_client.get_invoice(invoice_id, request_options=request_options)
        return _response.data

    def update_invoice(
        self,
        invoice_id: str,
        *,
        invoice: Invoice,
        fields_to_clear: typing.Optional[typing.Sequence[str]] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateInvoiceResponse:
        """
        Updates an invoice by modifying fields, clearing fields, or both. For most updates, you can use a sparse
        `Invoice` object to add fields or change values and use the `fields_to_clear` field to specify fields to clear.
        However, some restrictions apply. For example, you cannot change the `order_id` or `location_id` field and you
        must provide the complete `custom_fields` list to update a custom field. Published invoices have additional restrictions.

        Parameters
        ----------
        invoice_id : str
            The ID of the invoice to update.

        invoice : Invoice

        fields_to_clear : typing.Optional[typing.Sequence[str]]
            The list of fields to clear.
            For examples, see [Update an invoice](https://developer.squareup.com/docs/invoices-api/overview#update-an-invoice).

        idempotency_key : typing.Optional[str]
            A unique string that identifies the `UpdateInvoice` request. If you do not
            provide `idempotency_key` (or provide an empty string as the value), the endpoint
            treats each request as independent.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateInvoiceResponse
            Success

        Examples
        --------
        from fern import FernApi, Invoice

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.invoices.update_invoice(
            invoice_id="invoice_id",
            invoice=Invoice(),
        )
        """
        _response = self._raw_client.update_invoice(
            invoice_id,
            invoice=invoice,
            fields_to_clear=fields_to_clear,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )
        return _response.data

    def delete_invoice(
        self,
        invoice_id: str,
        *,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteInvoiceResponse:
        """
        Deletes the specified invoice. When an invoice is deleted, the
        associated order status changes to CANCELED. You can only delete a draft
        invoice (you cannot delete a published invoice, including one that is scheduled for processing).

        Parameters
        ----------
        invoice_id : str
            The ID of the invoice to delete.

        version : typing.Optional[int]
            The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to delete.
            If you do not know the version, you can call [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or
            [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteInvoiceResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.invoices.delete_invoice(
            invoice_id="invoice_id",
        )
        """
        _response = self._raw_client.delete_invoice(invoice_id, version=version, request_options=request_options)
        return _response.data

    def cancel_invoice(
        self, invoice_id: str, *, version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelInvoiceResponse:
        """
        Cancels an invoice. The seller cannot collect payments for
        the canceled invoice.

        You cannot cancel an invoice in the `DRAFT` state or in a terminal state: `PAID`, `REFUNDED`, `CANCELED`, or `FAILED`.

        Parameters
        ----------
        invoice_id : str
            The ID of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel.

        version : int
            The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel.
            If you do not know the version, you can call
            [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelInvoiceResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.invoices.cancel_invoice(
            invoice_id="invoice_id",
            version=1,
        )
        """
        _response = self._raw_client.cancel_invoice(invoice_id, version=version, request_options=request_options)
        return _response.data

    def publish_invoice(
        self,
        invoice_id: str,
        *,
        version: int,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublishInvoiceResponse:
        """
        Publishes the specified draft invoice.

        After an invoice is published, Square
        follows up based on the invoice configuration. For example, Square
        sends the invoice to the customer's email address, charges the customer's card on file, or does
        nothing. Square also makes the invoice available on a Square-hosted invoice page.

        The invoice `status` also changes from `DRAFT` to a status
        based on the invoice configuration. For example, the status changes to `UNPAID` if
        Square emails the invoice or `PARTIALLY_PAID` if Square charge a card on file for a portion of the
        invoice amount.

        Parameters
        ----------
        invoice_id : str
            The ID of the invoice to publish.

        version : int
            The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to publish.
            This must match the current version of the invoice; otherwise, the request is rejected.

        idempotency_key : typing.Optional[str]
            A unique string that identifies the `PublishInvoice` request. If you do not
            provide `idempotency_key` (or provide an empty string as the value), the endpoint
            treats each request as independent.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishInvoiceResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.invoices.publish_invoice(
            invoice_id="invoice_id",
            version=1,
        )
        """
        _response = self._raw_client.publish_invoice(
            invoice_id, version=version, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data


class AsyncInvoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInvoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInvoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInvoicesClient
        """
        return self._raw_client

    async def list_invoices(
        self,
        *,
        location_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListInvoicesResponse:
        """
        Returns a list of invoices for a given location. The response
        is paginated. If truncated, the response includes a `cursor` that you
        use in a subsequent request to retrieve the next set of invoices.

        Parameters
        ----------
        location_id : str
            The ID of the location for which to list invoices.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of invoices to return (200 is the maximum `limit`).
            If not provided, the server uses a default limit of 100 invoices.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListInvoicesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.list_invoices(
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_invoices(
            location_id=location_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_invoice(
        self,
        *,
        invoice: Invoice,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateInvoiceResponse:
        """
        Creates a draft [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice)
        for an order created using the Orders API.

        A draft invoice remains in your account and no action is taken.
        You must publish the invoice before Square can process it (send it to the customer's email address or charge the customer’s card on file).

        Parameters
        ----------
        invoice : Invoice

        idempotency_key : typing.Optional[str]
            A unique string that identifies the `CreateInvoice` request. If you do not
            provide `idempotency_key` (or provide an empty string as the value), the endpoint
            treats each request as independent.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateInvoiceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Invoice

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.create_invoice(
                invoice=Invoice(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_invoice(
            invoice=invoice, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def search_invoices(
        self,
        *,
        query: InvoiceQuery,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchInvoicesResponse:
        """
        Searches for invoices from a location specified in
        the filter. You can optionally specify customers in the filter for whom to
        retrieve invoices. In the current implementation, you can only specify one location and
        optionally one customer.

        The response is paginated. If truncated, the response includes a `cursor`
        that you use in a subsequent request to retrieve the next set of invoices.

        Parameters
        ----------
        query : InvoiceQuery

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of invoices to return (200 is the maximum `limit`).
            If not provided, the server uses a default limit of 100 invoices.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchInvoicesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, InvoiceFilter, InvoiceQuery

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.search_invoices(
                query=InvoiceQuery(
                    filter=InvoiceFilter(
                        location_ids=["location_ids"],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_invoices(
            query=query, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_invoice(
        self, invoice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetInvoiceResponse:
        """
        Retrieves an invoice by invoice ID.

        Parameters
        ----------
        invoice_id : str
            The ID of the invoice to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetInvoiceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.get_invoice(
                invoice_id="invoice_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_invoice(invoice_id, request_options=request_options)
        return _response.data

    async def update_invoice(
        self,
        invoice_id: str,
        *,
        invoice: Invoice,
        fields_to_clear: typing.Optional[typing.Sequence[str]] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateInvoiceResponse:
        """
        Updates an invoice by modifying fields, clearing fields, or both. For most updates, you can use a sparse
        `Invoice` object to add fields or change values and use the `fields_to_clear` field to specify fields to clear.
        However, some restrictions apply. For example, you cannot change the `order_id` or `location_id` field and you
        must provide the complete `custom_fields` list to update a custom field. Published invoices have additional restrictions.

        Parameters
        ----------
        invoice_id : str
            The ID of the invoice to update.

        invoice : Invoice

        fields_to_clear : typing.Optional[typing.Sequence[str]]
            The list of fields to clear.
            For examples, see [Update an invoice](https://developer.squareup.com/docs/invoices-api/overview#update-an-invoice).

        idempotency_key : typing.Optional[str]
            A unique string that identifies the `UpdateInvoice` request. If you do not
            provide `idempotency_key` (or provide an empty string as the value), the endpoint
            treats each request as independent.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateInvoiceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Invoice

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.update_invoice(
                invoice_id="invoice_id",
                invoice=Invoice(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_invoice(
            invoice_id,
            invoice=invoice,
            fields_to_clear=fields_to_clear,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )
        return _response.data

    async def delete_invoice(
        self,
        invoice_id: str,
        *,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteInvoiceResponse:
        """
        Deletes the specified invoice. When an invoice is deleted, the
        associated order status changes to CANCELED. You can only delete a draft
        invoice (you cannot delete a published invoice, including one that is scheduled for processing).

        Parameters
        ----------
        invoice_id : str
            The ID of the invoice to delete.

        version : typing.Optional[int]
            The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to delete.
            If you do not know the version, you can call [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or
            [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteInvoiceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.delete_invoice(
                invoice_id="invoice_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_invoice(invoice_id, version=version, request_options=request_options)
        return _response.data

    async def cancel_invoice(
        self, invoice_id: str, *, version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelInvoiceResponse:
        """
        Cancels an invoice. The seller cannot collect payments for
        the canceled invoice.

        You cannot cancel an invoice in the `DRAFT` state or in a terminal state: `PAID`, `REFUNDED`, `CANCELED`, or `FAILED`.

        Parameters
        ----------
        invoice_id : str
            The ID of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel.

        version : int
            The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel.
            If you do not know the version, you can call
            [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelInvoiceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.cancel_invoice(
                invoice_id="invoice_id",
                version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_invoice(invoice_id, version=version, request_options=request_options)
        return _response.data

    async def publish_invoice(
        self,
        invoice_id: str,
        *,
        version: int,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublishInvoiceResponse:
        """
        Publishes the specified draft invoice.

        After an invoice is published, Square
        follows up based on the invoice configuration. For example, Square
        sends the invoice to the customer's email address, charges the customer's card on file, or does
        nothing. Square also makes the invoice available on a Square-hosted invoice page.

        The invoice `status` also changes from `DRAFT` to a status
        based on the invoice configuration. For example, the status changes to `UNPAID` if
        Square emails the invoice or `PARTIALLY_PAID` if Square charge a card on file for a portion of the
        invoice amount.

        Parameters
        ----------
        invoice_id : str
            The ID of the invoice to publish.

        version : int
            The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to publish.
            This must match the current version of the invoice; otherwise, the request is rejected.

        idempotency_key : typing.Optional[str]
            A unique string that identifies the `PublishInvoice` request. If you do not
            provide `idempotency_key` (or provide an empty string as the value), the endpoint
            treats each request as independent.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishInvoiceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.publish_invoice(
                invoice_id="invoice_id",
                version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_invoice(
            invoice_id, version=version, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data
