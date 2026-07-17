

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
from ..types.bad_request_response import BadRequestResponse
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
from ..types.not_found_response import NotFoundResponse
from ..types.pass_through_query import PassThroughQuery
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.row_version import RowVersion
from ..types.tax_inclusive import TaxInclusive
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_bill_response import UpdateBillResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBillsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[GetBillsResponse]:
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
        HttpResponse[GetBillsResponse]
            Bills
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/bills",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "sort": convert_and_respect_annotation_metadata(object_=sort, annotation=BillsSort, direction="write"),
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
                    GetBillsResponse,
                    parse_obj_as(
                        type_=GetBillsResponse,
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
    ) -> HttpResponse[CreateBillResponse]:
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
        HttpResponse[CreateBillResponse]
            Bill created
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/bills",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "balance": balance,
                "bill_date": bill_date,
                "bill_number": bill_number,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "deposit": deposit,
                "downstream_id": downstream_id,
                "due_date": due_date,
                "id": id,
                "ledger_account": convert_and_respect_annotation_metadata(
                    object_=ledger_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[BillLineItem], direction="write"
                ),
                "notes": notes,
                "paid_date": paid_date,
                "po_number": po_number,
                "reference": reference,
                "row_version": row_version,
                "status": status,
                "sub_total": sub_total,
                "supplier": convert_and_respect_annotation_metadata(
                    object_=supplier, annotation=typing.Optional[LinkedSupplier], direction="write"
                ),
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "terms": terms,
                "total": total,
                "total_tax": total_tax,
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
                    CreateBillResponse,
                    parse_obj_as(
                        type_=CreateBillResponse,
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
    ) -> HttpResponse[GetBillResponse]:
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
        HttpResponse[GetBillResponse]
            Bill
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/bills/{encode_path_param(id)}",
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
                    GetBillResponse,
                    parse_obj_as(
                        type_=GetBillResponse,
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
    ) -> HttpResponse[DeleteBillResponse]:
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
        HttpResponse[DeleteBillResponse]
            Bill deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/bills/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteBillResponse,
                    parse_obj_as(
                        type_=DeleteBillResponse,
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
    ) -> HttpResponse[UpdateBillResponse]:
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
        HttpResponse[UpdateBillResponse]
            Bill Updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/bills/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "balance": balance,
                "bill_date": bill_date,
                "bill_number": bill_number,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "deposit": deposit,
                "downstream_id": downstream_id,
                "due_date": due_date,
                "id": id,
                "ledger_account": convert_and_respect_annotation_metadata(
                    object_=ledger_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[BillLineItem], direction="write"
                ),
                "notes": notes,
                "paid_date": paid_date,
                "po_number": po_number,
                "reference": reference,
                "row_version": row_version,
                "status": status,
                "sub_total": sub_total,
                "supplier": convert_and_respect_annotation_metadata(
                    object_=supplier, annotation=typing.Optional[LinkedSupplier], direction="write"
                ),
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "terms": terms,
                "total": total,
                "total_tax": total_tax,
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
                    UpdateBillResponse,
                    parse_obj_as(
                        type_=UpdateBillResponse,
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


class AsyncRawBillsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[GetBillsResponse]:
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
        AsyncHttpResponse[GetBillsResponse]
            Bills
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/bills",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "sort": convert_and_respect_annotation_metadata(object_=sort, annotation=BillsSort, direction="write"),
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
                    GetBillsResponse,
                    parse_obj_as(
                        type_=GetBillsResponse,
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
    ) -> AsyncHttpResponse[CreateBillResponse]:
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
        AsyncHttpResponse[CreateBillResponse]
            Bill created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/bills",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "balance": balance,
                "bill_date": bill_date,
                "bill_number": bill_number,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "deposit": deposit,
                "downstream_id": downstream_id,
                "due_date": due_date,
                "id": id,
                "ledger_account": convert_and_respect_annotation_metadata(
                    object_=ledger_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[BillLineItem], direction="write"
                ),
                "notes": notes,
                "paid_date": paid_date,
                "po_number": po_number,
                "reference": reference,
                "row_version": row_version,
                "status": status,
                "sub_total": sub_total,
                "supplier": convert_and_respect_annotation_metadata(
                    object_=supplier, annotation=typing.Optional[LinkedSupplier], direction="write"
                ),
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "terms": terms,
                "total": total,
                "total_tax": total_tax,
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
                    CreateBillResponse,
                    parse_obj_as(
                        type_=CreateBillResponse,
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
    ) -> AsyncHttpResponse[GetBillResponse]:
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
        AsyncHttpResponse[GetBillResponse]
            Bill
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/bills/{encode_path_param(id)}",
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
                    GetBillResponse,
                    parse_obj_as(
                        type_=GetBillResponse,
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
    ) -> AsyncHttpResponse[DeleteBillResponse]:
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
        AsyncHttpResponse[DeleteBillResponse]
            Bill deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/bills/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteBillResponse,
                    parse_obj_as(
                        type_=DeleteBillResponse,
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
    ) -> AsyncHttpResponse[UpdateBillResponse]:
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
        AsyncHttpResponse[UpdateBillResponse]
            Bill Updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/bills/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "balance": balance,
                "bill_date": bill_date,
                "bill_number": bill_number,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "deposit": deposit,
                "downstream_id": downstream_id,
                "due_date": due_date,
                "id": id,
                "ledger_account": convert_and_respect_annotation_metadata(
                    object_=ledger_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[BillLineItem], direction="write"
                ),
                "notes": notes,
                "paid_date": paid_date,
                "po_number": po_number,
                "reference": reference,
                "row_version": row_version,
                "status": status,
                "sub_total": sub_total,
                "supplier": convert_and_respect_annotation_metadata(
                    object_=supplier, annotation=typing.Optional[LinkedSupplier], direction="write"
                ),
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "terms": terms,
                "total": total,
                "total_tax": total_tax,
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
                    UpdateBillResponse,
                    parse_obj_as(
                        type_=UpdateBillResponse,
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
