

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.get_customer_invoice_by_id_response import GetCustomerInvoiceByIdResponse
from ..types.list_customer_invoices_response import ListCustomerInvoicesResponse
from .types.get_customer_invoices_request_sort_field import GetCustomerInvoicesRequestSortField
from .types.get_customer_invoices_request_sort_order import GetCustomerInvoicesRequestSortOrder
from pydantic import ValidationError


class RawCustomerInvoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[ListCustomerInvoicesResponse]:
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
        HttpResponse[ListCustomerInvoicesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "customerInvoices",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "customerId": customer_id,
                "jobId": job_id,
                "invoiceNumber": invoice_number,
                "dueBefore": serialize_datetime(due_before) if due_before is not None else None,
                "dueAfter": serialize_datetime(due_after) if due_after is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCustomerInvoicesResponse,
                    parse_obj_as(
                        type_=ListCustomerInvoicesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_customer_invoices_invoice_id(
        self, invoice_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetCustomerInvoiceByIdResponse]:
        """
        Returns a single invoice by ID with customer details and sections

        Parameters
        ----------
        invoice_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCustomerInvoiceByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"customerInvoices/{encode_path_param(invoice_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomerInvoiceByIdResponse,
                    parse_obj_as(
                        type_=GetCustomerInvoiceByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCustomerInvoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[ListCustomerInvoicesResponse]:
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
        AsyncHttpResponse[ListCustomerInvoicesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "customerInvoices",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "customerId": customer_id,
                "jobId": job_id,
                "invoiceNumber": invoice_number,
                "dueBefore": serialize_datetime(due_before) if due_before is not None else None,
                "dueAfter": serialize_datetime(due_after) if due_after is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCustomerInvoicesResponse,
                    parse_obj_as(
                        type_=ListCustomerInvoicesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_customer_invoices_invoice_id(
        self, invoice_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetCustomerInvoiceByIdResponse]:
        """
        Returns a single invoice by ID with customer details and sections

        Parameters
        ----------
        invoice_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCustomerInvoiceByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"customerInvoices/{encode_path_param(invoice_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomerInvoiceByIdResponse,
                    parse_obj_as(
                        type_=GetCustomerInvoiceByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
