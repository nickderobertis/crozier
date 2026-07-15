

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.bad_request_response import BadRequestResponse
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
from ..types.not_found_response import NotFoundResponse
from ..types.pass_through_query import PassThroughQuery
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.row_version import RowVersion
from ..types.tax_inclusive import TaxInclusive
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_credit_note_response import UpdateCreditNoteResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy


OMIT = typing.cast(typing.Any, ...)


class RawCreditNotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetCreditNotesResponse]:
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
        HttpResponse[GetCreditNotesResponse]
            Credit Notes
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/credit-notes",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
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
                    GetCreditNotesResponse,
                    parse_obj_as(
                        type_=GetCreditNotesResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[CreateCreditNoteResponse]:
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
        HttpResponse[CreateCreditNoteResponse]
            Credit Note created
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/credit-notes",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "allocations": convert_and_respect_annotation_metadata(
                    object_=allocations, annotation=typing.Sequence[CreditNoteAllocationsItem], direction="write"
                ),
                "balance": balance,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "date_issued": date_issued,
                "date_paid": date_paid,
                "id": id,
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[InvoiceLineItem], direction="write"
                ),
                "note": note,
                "number": number,
                "reference": reference,
                "remaining_credit": remaining_credit,
                "row_version": row_version,
                "status": status,
                "sub_total": sub_total,
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "terms": terms,
                "total_amount": total_amount,
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
                    CreateCreditNoteResponse,
                    parse_obj_as(
                        type_=CreateCreditNoteResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetCreditNoteResponse]:
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
        HttpResponse[GetCreditNoteResponse]
            Credit Note
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/credit-notes/{jsonable_encoder(id)}",
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
                    GetCreditNoteResponse,
                    parse_obj_as(
                        type_=GetCreditNoteResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteCreditNoteResponse]:
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
        HttpResponse[DeleteCreditNoteResponse]
            Credit Note deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/credit-notes/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteCreditNoteResponse,
                    parse_obj_as(
                        type_=DeleteCreditNoteResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[UpdateCreditNoteResponse]:
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
        HttpResponse[UpdateCreditNoteResponse]
            Credit Note updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/credit-notes/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "allocations": convert_and_respect_annotation_metadata(
                    object_=allocations, annotation=typing.Sequence[CreditNoteAllocationsItem], direction="write"
                ),
                "balance": balance,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "date_issued": date_issued,
                "date_paid": date_paid,
                "id": id,
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[InvoiceLineItem], direction="write"
                ),
                "note": note,
                "number": number,
                "reference": reference,
                "remaining_credit": remaining_credit,
                "row_version": row_version,
                "status": status,
                "sub_total": sub_total,
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "terms": terms,
                "total_amount": total_amount,
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
                    UpdateCreditNoteResponse,
                    parse_obj_as(
                        type_=UpdateCreditNoteResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCreditNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetCreditNotesResponse]:
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
        AsyncHttpResponse[GetCreditNotesResponse]
            Credit Notes
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/credit-notes",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
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
                    GetCreditNotesResponse,
                    parse_obj_as(
                        type_=GetCreditNotesResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[CreateCreditNoteResponse]:
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
        AsyncHttpResponse[CreateCreditNoteResponse]
            Credit Note created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/credit-notes",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "allocations": convert_and_respect_annotation_metadata(
                    object_=allocations, annotation=typing.Sequence[CreditNoteAllocationsItem], direction="write"
                ),
                "balance": balance,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "date_issued": date_issued,
                "date_paid": date_paid,
                "id": id,
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[InvoiceLineItem], direction="write"
                ),
                "note": note,
                "number": number,
                "reference": reference,
                "remaining_credit": remaining_credit,
                "row_version": row_version,
                "status": status,
                "sub_total": sub_total,
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "terms": terms,
                "total_amount": total_amount,
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
                    CreateCreditNoteResponse,
                    parse_obj_as(
                        type_=CreateCreditNoteResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetCreditNoteResponse]:
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
        AsyncHttpResponse[GetCreditNoteResponse]
            Credit Note
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/credit-notes/{jsonable_encoder(id)}",
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
                    GetCreditNoteResponse,
                    parse_obj_as(
                        type_=GetCreditNoteResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteCreditNoteResponse]:
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
        AsyncHttpResponse[DeleteCreditNoteResponse]
            Credit Note deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/credit-notes/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteCreditNoteResponse,
                    parse_obj_as(
                        type_=DeleteCreditNoteResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[UpdateCreditNoteResponse]:
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
        AsyncHttpResponse[UpdateCreditNoteResponse]
            Credit Note updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/credit-notes/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "allocations": convert_and_respect_annotation_metadata(
                    object_=allocations, annotation=typing.Sequence[CreditNoteAllocationsItem], direction="write"
                ),
                "balance": balance,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "date_issued": date_issued,
                "date_paid": date_paid,
                "id": id,
                "line_items": convert_and_respect_annotation_metadata(
                    object_=line_items, annotation=typing.Sequence[InvoiceLineItem], direction="write"
                ),
                "note": note,
                "number": number,
                "reference": reference,
                "remaining_credit": remaining_credit,
                "row_version": row_version,
                "status": status,
                "sub_total": sub_total,
                "tax_code": tax_code,
                "tax_inclusive": tax_inclusive,
                "terms": terms,
                "total_amount": total_amount,
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
                    UpdateCreditNoteResponse,
                    parse_obj_as(
                        type_=UpdateCreditNoteResponse,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
