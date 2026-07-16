

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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


OMIT = typing.cast(typing.Any, ...)


class RawInvoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_invoices(
        self,
        *,
        location_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListInvoicesResponse]:
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
        HttpResponse[ListInvoicesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/invoices",
            method="GET",
            params={
                "location_id": location_id,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListInvoicesResponse,
                    parse_obj_as(
                        type_=ListInvoicesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_invoice(
        self,
        *,
        invoice: Invoice,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateInvoiceResponse]:
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
        HttpResponse[CreateInvoiceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/invoices",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "invoice": convert_and_respect_annotation_metadata(
                    object_=invoice, annotation=Invoice, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateInvoiceResponse,
                    parse_obj_as(
                        type_=CreateInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_invoices(
        self,
        *,
        query: InvoiceQuery,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchInvoicesResponse]:
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
        HttpResponse[SearchInvoicesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/invoices/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=InvoiceQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchInvoicesResponse,
                    parse_obj_as(
                        type_=SearchInvoicesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_invoice(
        self, invoice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetInvoiceResponse]:
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
        HttpResponse[GetInvoiceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/invoices/{jsonable_encoder(invoice_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetInvoiceResponse,
                    parse_obj_as(
                        type_=GetInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_invoice(
        self,
        invoice_id: str,
        *,
        invoice: Invoice,
        fields_to_clear: typing.Optional[typing.Sequence[str]] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateInvoiceResponse]:
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
        HttpResponse[UpdateInvoiceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/invoices/{jsonable_encoder(invoice_id)}",
            method="PUT",
            json={
                "fields_to_clear": fields_to_clear,
                "idempotency_key": idempotency_key,
                "invoice": convert_and_respect_annotation_metadata(
                    object_=invoice, annotation=Invoice, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateInvoiceResponse,
                    parse_obj_as(
                        type_=UpdateInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_invoice(
        self,
        invoice_id: str,
        *,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteInvoiceResponse]:
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
        HttpResponse[DeleteInvoiceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/invoices/{jsonable_encoder(invoice_id)}",
            method="DELETE",
            params={
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteInvoiceResponse,
                    parse_obj_as(
                        type_=DeleteInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_invoice(
        self, invoice_id: str, *, version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelInvoiceResponse]:
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
        HttpResponse[CancelInvoiceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/invoices/{jsonable_encoder(invoice_id)}/cancel",
            method="POST",
            json={
                "version": version,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelInvoiceResponse,
                    parse_obj_as(
                        type_=CancelInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def publish_invoice(
        self,
        invoice_id: str,
        *,
        version: int,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PublishInvoiceResponse]:
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
        HttpResponse[PublishInvoiceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/invoices/{jsonable_encoder(invoice_id)}/publish",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "version": version,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PublishInvoiceResponse,
                    parse_obj_as(
                        type_=PublishInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawInvoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_invoices(
        self,
        *,
        location_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListInvoicesResponse]:
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
        AsyncHttpResponse[ListInvoicesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/invoices",
            method="GET",
            params={
                "location_id": location_id,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListInvoicesResponse,
                    parse_obj_as(
                        type_=ListInvoicesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_invoice(
        self,
        *,
        invoice: Invoice,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateInvoiceResponse]:
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
        AsyncHttpResponse[CreateInvoiceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/invoices",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "invoice": convert_and_respect_annotation_metadata(
                    object_=invoice, annotation=Invoice, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateInvoiceResponse,
                    parse_obj_as(
                        type_=CreateInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_invoices(
        self,
        *,
        query: InvoiceQuery,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchInvoicesResponse]:
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
        AsyncHttpResponse[SearchInvoicesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/invoices/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=InvoiceQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchInvoicesResponse,
                    parse_obj_as(
                        type_=SearchInvoicesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_invoice(
        self, invoice_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetInvoiceResponse]:
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
        AsyncHttpResponse[GetInvoiceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/invoices/{jsonable_encoder(invoice_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetInvoiceResponse,
                    parse_obj_as(
                        type_=GetInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_invoice(
        self,
        invoice_id: str,
        *,
        invoice: Invoice,
        fields_to_clear: typing.Optional[typing.Sequence[str]] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateInvoiceResponse]:
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
        AsyncHttpResponse[UpdateInvoiceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/invoices/{jsonable_encoder(invoice_id)}",
            method="PUT",
            json={
                "fields_to_clear": fields_to_clear,
                "idempotency_key": idempotency_key,
                "invoice": convert_and_respect_annotation_metadata(
                    object_=invoice, annotation=Invoice, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateInvoiceResponse,
                    parse_obj_as(
                        type_=UpdateInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_invoice(
        self,
        invoice_id: str,
        *,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteInvoiceResponse]:
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
        AsyncHttpResponse[DeleteInvoiceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/invoices/{jsonable_encoder(invoice_id)}",
            method="DELETE",
            params={
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteInvoiceResponse,
                    parse_obj_as(
                        type_=DeleteInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_invoice(
        self, invoice_id: str, *, version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelInvoiceResponse]:
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
        AsyncHttpResponse[CancelInvoiceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/invoices/{jsonable_encoder(invoice_id)}/cancel",
            method="POST",
            json={
                "version": version,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelInvoiceResponse,
                    parse_obj_as(
                        type_=CancelInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def publish_invoice(
        self,
        invoice_id: str,
        *,
        version: int,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PublishInvoiceResponse]:
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
        AsyncHttpResponse[PublishInvoiceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/invoices/{jsonable_encoder(invoice_id)}/publish",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "version": version,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PublishInvoiceResponse,
                    parse_obj_as(
                        type_=PublishInvoiceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
