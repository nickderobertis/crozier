

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
from ..types.not_found_response import NotFoundResponse
from ..types.pass_through_query import PassThroughQuery
from ..types.payment_allocations_item import PaymentAllocationsItem
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.payment_status import PaymentStatus
from ..types.payment_type import PaymentType
from ..types.row_version import RowVersion
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_payment_response import UpdatePaymentResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPaymentsClient:
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
    ) -> HttpResponse[GetPaymentsResponse]:
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
        HttpResponse[GetPaymentsResponse]
            Payments
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/payments",
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
                    GetPaymentsResponse,
                    parse_obj_as(
                        type_=GetPaymentsResponse,
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
    ) -> HttpResponse[CreatePaymentResponse]:
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
        HttpResponse[CreatePaymentResponse]
            Payment created
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/payments",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "accounts_receivable_account_id": accounts_receivable_account_id,
                "accounts_receivable_account_type": accounts_receivable_account_type,
                "allocations": convert_and_respect_annotation_metadata(
                    object_=allocations, annotation=typing.Sequence[PaymentAllocationsItem], direction="write"
                ),
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "display_id": display_id,
                "downstream_id": downstream_id,
                "id": id,
                "note": note,
                "payment_method": payment_method,
                "payment_method_id": payment_method_id,
                "payment_method_reference": payment_method_reference,
                "reconciled": reconciled,
                "reference": reference,
                "row_version": row_version,
                "status": status,
                "supplier": convert_and_respect_annotation_metadata(
                    object_=supplier, annotation=typing.Optional[LinkedSupplier], direction="write"
                ),
                "total_amount": total_amount,
                "transaction_date": transaction_date,
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
                    CreatePaymentResponse,
                    parse_obj_as(
                        type_=CreatePaymentResponse,
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
    ) -> HttpResponse[GetPaymentResponse]:
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
        HttpResponse[GetPaymentResponse]
            Payment
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/payments/{encode_path_param(id)}",
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
                    GetPaymentResponse,
                    parse_obj_as(
                        type_=GetPaymentResponse,
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
    ) -> HttpResponse[DeletePaymentResponse]:
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
        HttpResponse[DeletePaymentResponse]
            Payment deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/payments/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletePaymentResponse,
                    parse_obj_as(
                        type_=DeletePaymentResponse,
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
    ) -> HttpResponse[UpdatePaymentResponse]:
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
        HttpResponse[UpdatePaymentResponse]
            Payment Updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/payments/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "accounts_receivable_account_id": accounts_receivable_account_id,
                "accounts_receivable_account_type": accounts_receivable_account_type,
                "allocations": convert_and_respect_annotation_metadata(
                    object_=allocations, annotation=typing.Sequence[PaymentAllocationsItem], direction="write"
                ),
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "display_id": display_id,
                "downstream_id": downstream_id,
                "id": id,
                "note": note,
                "payment_method": payment_method,
                "payment_method_id": payment_method_id,
                "payment_method_reference": payment_method_reference,
                "reconciled": reconciled,
                "reference": reference,
                "row_version": row_version,
                "status": status,
                "supplier": convert_and_respect_annotation_metadata(
                    object_=supplier, annotation=typing.Optional[LinkedSupplier], direction="write"
                ),
                "total_amount": total_amount,
                "transaction_date": transaction_date,
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
                    UpdatePaymentResponse,
                    parse_obj_as(
                        type_=UpdatePaymentResponse,
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


class AsyncRawPaymentsClient:
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
    ) -> AsyncHttpResponse[GetPaymentsResponse]:
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
        AsyncHttpResponse[GetPaymentsResponse]
            Payments
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/payments",
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
                    GetPaymentsResponse,
                    parse_obj_as(
                        type_=GetPaymentsResponse,
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
    ) -> AsyncHttpResponse[CreatePaymentResponse]:
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
        AsyncHttpResponse[CreatePaymentResponse]
            Payment created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/payments",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "accounts_receivable_account_id": accounts_receivable_account_id,
                "accounts_receivable_account_type": accounts_receivable_account_type,
                "allocations": convert_and_respect_annotation_metadata(
                    object_=allocations, annotation=typing.Sequence[PaymentAllocationsItem], direction="write"
                ),
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "display_id": display_id,
                "downstream_id": downstream_id,
                "id": id,
                "note": note,
                "payment_method": payment_method,
                "payment_method_id": payment_method_id,
                "payment_method_reference": payment_method_reference,
                "reconciled": reconciled,
                "reference": reference,
                "row_version": row_version,
                "status": status,
                "supplier": convert_and_respect_annotation_metadata(
                    object_=supplier, annotation=typing.Optional[LinkedSupplier], direction="write"
                ),
                "total_amount": total_amount,
                "transaction_date": transaction_date,
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
                    CreatePaymentResponse,
                    parse_obj_as(
                        type_=CreatePaymentResponse,
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
    ) -> AsyncHttpResponse[GetPaymentResponse]:
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
        AsyncHttpResponse[GetPaymentResponse]
            Payment
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/payments/{encode_path_param(id)}",
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
                    GetPaymentResponse,
                    parse_obj_as(
                        type_=GetPaymentResponse,
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
    ) -> AsyncHttpResponse[DeletePaymentResponse]:
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
        AsyncHttpResponse[DeletePaymentResponse]
            Payment deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/payments/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletePaymentResponse,
                    parse_obj_as(
                        type_=DeletePaymentResponse,
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
    ) -> AsyncHttpResponse[UpdatePaymentResponse]:
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
        AsyncHttpResponse[UpdatePaymentResponse]
            Payment Updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/payments/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "accounts_receivable_account_id": accounts_receivable_account_id,
                "accounts_receivable_account_type": accounts_receivable_account_type,
                "allocations": convert_and_respect_annotation_metadata(
                    object_=allocations, annotation=typing.Sequence[PaymentAllocationsItem], direction="write"
                ),
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "currency_rate": currency_rate,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=typing.Optional[LinkedCustomer], direction="write"
                ),
                "display_id": display_id,
                "downstream_id": downstream_id,
                "id": id,
                "note": note,
                "payment_method": payment_method,
                "payment_method_id": payment_method_id,
                "payment_method_reference": payment_method_reference,
                "reconciled": reconciled,
                "reference": reference,
                "row_version": row_version,
                "status": status,
                "supplier": convert_and_respect_annotation_metadata(
                    object_=supplier, annotation=typing.Optional[LinkedSupplier], direction="write"
                ),
                "total_amount": total_amount,
                "transaction_date": transaction_date,
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
                    UpdatePaymentResponse,
                    parse_obj_as(
                        type_=UpdatePaymentResponse,
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
