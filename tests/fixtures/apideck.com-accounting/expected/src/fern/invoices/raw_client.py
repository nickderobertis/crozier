

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.address import Address
from ..types.bad_request_response import BadRequestResponse
from ..types.create_invoice_response import CreateInvoiceResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.currency import Currency
from ..types.currency_rate import CurrencyRate
from ..types.delete_invoice_response import DeleteInvoiceResponse
from ..types.downstream_id import DownstreamId
from ..types.get_invoice_response import GetInvoiceResponse
from ..types.get_invoices_response import GetInvoicesResponse
from ..types.id import Id
from ..types.invoice_line_item import InvoiceLineItem
from ..types.invoice_status import InvoiceStatus
from ..types.invoice_type import InvoiceType
from ..types.invoices_sort import InvoicesSort
from ..types.linked_customer import LinkedCustomer
from ..types.not_found_response import NotFoundResponse
from ..types.pass_through_query import PassThroughQuery
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.row_version import RowVersion
from ..types.tax_inclusive import TaxInclusive
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_invoice_response import UpdateInvoiceResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInvoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[InvoicesSort] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetInvoicesResponse]:
        """
        List Invoices

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[InvoicesSort]
            Apply sorting

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetInvoicesResponse]
            Invoices
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/invoices",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=InvoicesSort, direction="write"
                ),
                "pass_through": convert_and_respect_annotation_metadata(
                    object_=pass_through, annotation=PassThroughQuery, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetInvoicesResponse,
                    parse_obj_as(
                        type_=GetInvoicesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        balance: typing.Optional[float] = OMIT,
        billing_address: typing.Optional[Address] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        customer_memo: typing.Optional[str] = OMIT,
        deposit: typing.Optional[float] = OMIT,
        discount_amount: typing.Optional[float] = OMIT,
        discount_percentage: typing.Optional[float] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        due_date: typing.Optional[dt.date] = OMIT,
        id: typing.Optional[Id] = OMIT,
        invoice_date: typing.Optional[dt.date] = OMIT,
        invoice_sent: typing.Optional[bool] = OMIT,
        line_items: typing.Optional[typing.Sequence[InvoiceLineItem]] = OMIT,
        number: typing.Optional[str] = OMIT,
        po_number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        shipping_address: typing.Optional[Address] = OMIT,
        source_document_url: typing.Optional[str] = OMIT,
        status: typing.Optional[InvoiceStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total: typing.Optional[float] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        type: typing.Optional[InvoiceType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateInvoiceResponse]:
        """
        Create Invoice

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        balance : typing.Optional[float]
            Balance of invoice due.

        billing_address : typing.Optional[Address]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        customer_memo : typing.Optional[str]
            Customer memo

        deposit : typing.Optional[float]
            Amount of deposit made to this invoice.

        discount_amount : typing.Optional[float]
            Discount amount applied to this invoice.

        discount_percentage : typing.Optional[float]
            Discount percentage applied to this invoice.

        downstream_id : typing.Optional[DownstreamId]

        due_date : typing.Optional[dt.date]
            The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.

        id : typing.Optional[Id]

        invoice_date : typing.Optional[dt.date]
            Date invoice was issued - YYYY-MM-DD.

        invoice_sent : typing.Optional[bool]
            Invoice sent to contact/customer.

        line_items : typing.Optional[typing.Sequence[InvoiceLineItem]]

        number : typing.Optional[str]
            Invoice number.

        po_number : typing.Optional[str]
            A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.

        reference : typing.Optional[str]
            Optional invoice reference.

        row_version : typing.Optional[RowVersion]

        shipping_address : typing.Optional[Address]

        source_document_url : typing.Optional[str]
            URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.

        status : typing.Optional[InvoiceStatus]
            Invoice status

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        template_id : typing.Optional[str]
            Optional invoice template

        terms : typing.Optional[str]
            Terms of payment.

        total : typing.Optional[float]
            Total amount of invoice, including tax.

        total_tax : typing.Optional[float]
            Total tax amount applied to this invoice.

        type : typing.Optional[InvoiceType]
            Invoice type

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateInvoiceResponse]
            Invoice created
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/invoices",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "balance": balance,
                "billing_address": convert_and_respect_annotation_metadata(
                    object_=billing_address, annotation=Address, direction="write"
                ),
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "customer_memo": customer_memo,
                "deposit": deposit,
                "discount_amount": discount_amount,
                "discount_percentage": discount_percentage,
                "downstream_id": downstream_id,
                "due_date": due_date,
                "id": id,
                "invoice_date": invoice_date,
                "invoice_sent": invoice_sent,
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[InvoiceLineItem], direction="write"
                ),
                "number": number,
                "po_number": po_number,
                "reference": reference,
                "row_version": row_version,
                "shipping_address": convert_and_respect_annotation_metadata(
                    object_=shipping_address, annotation=Address, direction="write"
                ),
                "source_document_url": source_document_url,
                "status": status,
                "sub_total": sub_total,
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "template_id": template_id,
                "terms": terms,
                "total": total,
                "total_tax": total_tax,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetInvoiceResponse]:
        """
        Get Invoice

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
        HttpResponse[GetInvoiceResponse]
            Invoice
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/invoices/{encode_path_param(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteInvoiceResponse]:
        """
        Delete Invoice

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
        HttpResponse[DeleteInvoiceResponse]
            Invoice deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/invoices/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        balance: typing.Optional[float] = OMIT,
        billing_address: typing.Optional[Address] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        customer_memo: typing.Optional[str] = OMIT,
        deposit: typing.Optional[float] = OMIT,
        discount_amount: typing.Optional[float] = OMIT,
        discount_percentage: typing.Optional[float] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        due_date: typing.Optional[dt.date] = OMIT,
        id: typing.Optional[Id] = OMIT,
        invoice_date: typing.Optional[dt.date] = OMIT,
        invoice_sent: typing.Optional[bool] = OMIT,
        line_items: typing.Optional[typing.Sequence[InvoiceLineItem]] = OMIT,
        number: typing.Optional[str] = OMIT,
        po_number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        shipping_address: typing.Optional[Address] = OMIT,
        source_document_url: typing.Optional[str] = OMIT,
        status: typing.Optional[InvoiceStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total: typing.Optional[float] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        type: typing.Optional[InvoiceType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateInvoiceResponse]:
        """
        Update Invoice

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        balance : typing.Optional[float]
            Balance of invoice due.

        billing_address : typing.Optional[Address]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        customer_memo : typing.Optional[str]
            Customer memo

        deposit : typing.Optional[float]
            Amount of deposit made to this invoice.

        discount_amount : typing.Optional[float]
            Discount amount applied to this invoice.

        discount_percentage : typing.Optional[float]
            Discount percentage applied to this invoice.

        downstream_id : typing.Optional[DownstreamId]

        due_date : typing.Optional[dt.date]
            The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.

        id : typing.Optional[Id]

        invoice_date : typing.Optional[dt.date]
            Date invoice was issued - YYYY-MM-DD.

        invoice_sent : typing.Optional[bool]
            Invoice sent to contact/customer.

        line_items : typing.Optional[typing.Sequence[InvoiceLineItem]]

        number : typing.Optional[str]
            Invoice number.

        po_number : typing.Optional[str]
            A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.

        reference : typing.Optional[str]
            Optional invoice reference.

        row_version : typing.Optional[RowVersion]

        shipping_address : typing.Optional[Address]

        source_document_url : typing.Optional[str]
            URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.

        status : typing.Optional[InvoiceStatus]
            Invoice status

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        template_id : typing.Optional[str]
            Optional invoice template

        terms : typing.Optional[str]
            Terms of payment.

        total : typing.Optional[float]
            Total amount of invoice, including tax.

        total_tax : typing.Optional[float]
            Total tax amount applied to this invoice.

        type : typing.Optional[InvoiceType]
            Invoice type

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateInvoiceResponse]
            Invoice updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/invoices/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "balance": balance,
                "billing_address": convert_and_respect_annotation_metadata(
                    object_=billing_address, annotation=Address, direction="write"
                ),
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "customer_memo": customer_memo,
                "deposit": deposit,
                "discount_amount": discount_amount,
                "discount_percentage": discount_percentage,
                "downstream_id": downstream_id,
                "due_date": due_date,
                "id": id,
                "invoice_date": invoice_date,
                "invoice_sent": invoice_sent,
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[InvoiceLineItem], direction="write"
                ),
                "number": number,
                "po_number": po_number,
                "reference": reference,
                "row_version": row_version,
                "shipping_address": convert_and_respect_annotation_metadata(
                    object_=shipping_address, annotation=Address, direction="write"
                ),
                "source_document_url": source_document_url,
                "status": status,
                "sub_total": sub_total,
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "template_id": template_id,
                "terms": terms,
                "total": total,
                "total_tax": total_tax,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawInvoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[InvoicesSort] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetInvoicesResponse]:
        """
        List Invoices

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[InvoicesSort]
            Apply sorting

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetInvoicesResponse]
            Invoices
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/invoices",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "sort": convert_and_respect_annotation_metadata(
                    object_=sort, annotation=InvoicesSort, direction="write"
                ),
                "pass_through": convert_and_respect_annotation_metadata(
                    object_=pass_through, annotation=PassThroughQuery, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetInvoicesResponse,
                    parse_obj_as(
                        type_=GetInvoicesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        balance: typing.Optional[float] = OMIT,
        billing_address: typing.Optional[Address] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        customer_memo: typing.Optional[str] = OMIT,
        deposit: typing.Optional[float] = OMIT,
        discount_amount: typing.Optional[float] = OMIT,
        discount_percentage: typing.Optional[float] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        due_date: typing.Optional[dt.date] = OMIT,
        id: typing.Optional[Id] = OMIT,
        invoice_date: typing.Optional[dt.date] = OMIT,
        invoice_sent: typing.Optional[bool] = OMIT,
        line_items: typing.Optional[typing.Sequence[InvoiceLineItem]] = OMIT,
        number: typing.Optional[str] = OMIT,
        po_number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        shipping_address: typing.Optional[Address] = OMIT,
        source_document_url: typing.Optional[str] = OMIT,
        status: typing.Optional[InvoiceStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total: typing.Optional[float] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        type: typing.Optional[InvoiceType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateInvoiceResponse]:
        """
        Create Invoice

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        balance : typing.Optional[float]
            Balance of invoice due.

        billing_address : typing.Optional[Address]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        customer_memo : typing.Optional[str]
            Customer memo

        deposit : typing.Optional[float]
            Amount of deposit made to this invoice.

        discount_amount : typing.Optional[float]
            Discount amount applied to this invoice.

        discount_percentage : typing.Optional[float]
            Discount percentage applied to this invoice.

        downstream_id : typing.Optional[DownstreamId]

        due_date : typing.Optional[dt.date]
            The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.

        id : typing.Optional[Id]

        invoice_date : typing.Optional[dt.date]
            Date invoice was issued - YYYY-MM-DD.

        invoice_sent : typing.Optional[bool]
            Invoice sent to contact/customer.

        line_items : typing.Optional[typing.Sequence[InvoiceLineItem]]

        number : typing.Optional[str]
            Invoice number.

        po_number : typing.Optional[str]
            A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.

        reference : typing.Optional[str]
            Optional invoice reference.

        row_version : typing.Optional[RowVersion]

        shipping_address : typing.Optional[Address]

        source_document_url : typing.Optional[str]
            URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.

        status : typing.Optional[InvoiceStatus]
            Invoice status

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        template_id : typing.Optional[str]
            Optional invoice template

        terms : typing.Optional[str]
            Terms of payment.

        total : typing.Optional[float]
            Total amount of invoice, including tax.

        total_tax : typing.Optional[float]
            Total tax amount applied to this invoice.

        type : typing.Optional[InvoiceType]
            Invoice type

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateInvoiceResponse]
            Invoice created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/invoices",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "balance": balance,
                "billing_address": convert_and_respect_annotation_metadata(
                    object_=billing_address, annotation=Address, direction="write"
                ),
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "customer_memo": customer_memo,
                "deposit": deposit,
                "discount_amount": discount_amount,
                "discount_percentage": discount_percentage,
                "downstream_id": downstream_id,
                "due_date": due_date,
                "id": id,
                "invoice_date": invoice_date,
                "invoice_sent": invoice_sent,
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[InvoiceLineItem], direction="write"
                ),
                "number": number,
                "po_number": po_number,
                "reference": reference,
                "row_version": row_version,
                "shipping_address": convert_and_respect_annotation_metadata(
                    object_=shipping_address, annotation=Address, direction="write"
                ),
                "source_document_url": source_document_url,
                "status": status,
                "sub_total": sub_total,
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "template_id": template_id,
                "terms": terms,
                "total": total,
                "total_tax": total_tax,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetInvoiceResponse]:
        """
        Get Invoice

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
        AsyncHttpResponse[GetInvoiceResponse]
            Invoice
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/invoices/{encode_path_param(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteInvoiceResponse]:
        """
        Delete Invoice

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
        AsyncHttpResponse[DeleteInvoiceResponse]
            Invoice deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/invoices/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        balance: typing.Optional[float] = OMIT,
        billing_address: typing.Optional[Address] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        customer: typing.Optional[LinkedCustomer] = OMIT,
        customer_memo: typing.Optional[str] = OMIT,
        deposit: typing.Optional[float] = OMIT,
        discount_amount: typing.Optional[float] = OMIT,
        discount_percentage: typing.Optional[float] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        due_date: typing.Optional[dt.date] = OMIT,
        id: typing.Optional[Id] = OMIT,
        invoice_date: typing.Optional[dt.date] = OMIT,
        invoice_sent: typing.Optional[bool] = OMIT,
        line_items: typing.Optional[typing.Sequence[InvoiceLineItem]] = OMIT,
        number: typing.Optional[str] = OMIT,
        po_number: typing.Optional[str] = OMIT,
        reference: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        shipping_address: typing.Optional[Address] = OMIT,
        source_document_url: typing.Optional[str] = OMIT,
        status: typing.Optional[InvoiceStatus] = OMIT,
        sub_total: typing.Optional[float] = OMIT,
        tax_code: typing.Optional[str] = OMIT,
        tax_inclusive: typing.Optional[TaxInclusive] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        terms: typing.Optional[str] = OMIT,
        total: typing.Optional[float] = OMIT,
        total_tax: typing.Optional[float] = OMIT,
        type: typing.Optional[InvoiceType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateInvoiceResponse]:
        """
        Update Invoice

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        balance : typing.Optional[float]
            Balance of invoice due.

        billing_address : typing.Optional[Address]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        customer : typing.Optional[LinkedCustomer]

        customer_memo : typing.Optional[str]
            Customer memo

        deposit : typing.Optional[float]
            Amount of deposit made to this invoice.

        discount_amount : typing.Optional[float]
            Discount amount applied to this invoice.

        discount_percentage : typing.Optional[float]
            Discount percentage applied to this invoice.

        downstream_id : typing.Optional[DownstreamId]

        due_date : typing.Optional[dt.date]
            The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.

        id : typing.Optional[Id]

        invoice_date : typing.Optional[dt.date]
            Date invoice was issued - YYYY-MM-DD.

        invoice_sent : typing.Optional[bool]
            Invoice sent to contact/customer.

        line_items : typing.Optional[typing.Sequence[InvoiceLineItem]]

        number : typing.Optional[str]
            Invoice number.

        po_number : typing.Optional[str]
            A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.

        reference : typing.Optional[str]
            Optional invoice reference.

        row_version : typing.Optional[RowVersion]

        shipping_address : typing.Optional[Address]

        source_document_url : typing.Optional[str]
            URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.

        status : typing.Optional[InvoiceStatus]
            Invoice status

        sub_total : typing.Optional[float]
            Sub-total amount, normally before tax.

        tax_code : typing.Optional[str]
            Applicable tax id/code override if tax is not supplied on a line item basis.

        tax_inclusive : typing.Optional[TaxInclusive]

        template_id : typing.Optional[str]
            Optional invoice template

        terms : typing.Optional[str]
            Terms of payment.

        total : typing.Optional[float]
            Total amount of invoice, including tax.

        total_tax : typing.Optional[float]
            Total tax amount applied to this invoice.

        type : typing.Optional[InvoiceType]
            Invoice type

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateInvoiceResponse]
            Invoice updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/invoices/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "balance": balance,
                "billing_address": convert_and_respect_annotation_metadata(
                    object_=billing_address, annotation=Address, direction="write"
                ),
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "customer_memo": customer_memo,
                "deposit": deposit,
                "discount_amount": discount_amount,
                "discount_percentage": discount_percentage,
                "downstream_id": downstream_id,
                "due_date": due_date,
                "id": id,
                "invoice_date": invoice_date,
                "invoice_sent": invoice_sent,
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[InvoiceLineItem], direction="write"
                ),
                "number": number,
                "po_number": po_number,
                "reference": reference,
                "row_version": row_version,
                "shipping_address": convert_and_respect_annotation_metadata(
                    object_=shipping_address, annotation=Address, direction="write"
                ),
                "source_document_url": source_document_url,
                "status": status,
                "sub_total": sub_total,
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "template_id": template_id,
                "terms": terms,
                "total": total,
                "total_tax": total_tax,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
