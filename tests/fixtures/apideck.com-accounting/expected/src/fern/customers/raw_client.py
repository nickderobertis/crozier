

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
from ..types.accounting_customer_status import AccountingCustomerStatus
from ..types.address import Address
from ..types.bad_request_response import BadRequestResponse
from ..types.bank_account import BankAccount
from ..types.company_name import CompanyName
from ..types.create_customer_response import CreateCustomerResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.currency import Currency
from ..types.customers_filter import CustomersFilter
from ..types.delete_customer_response import DeleteCustomerResponse
from ..types.downstream_id import DownstreamId
from ..types.email import Email
from ..types.first_name import FirstName
from ..types.get_customer_response import GetCustomerResponse
from ..types.get_customers_response import GetCustomersResponse
from ..types.id import Id
from ..types.last_name import LastName
from ..types.linked_ledger_account import LinkedLedgerAccount
from ..types.linked_parent_customer import LinkedParentCustomer
from ..types.linked_tax_rate import LinkedTaxRate
from ..types.middle_name import MiddleName
from ..types.not_found_response import NotFoundResponse
from ..types.pass_through_query import PassThroughQuery
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.phone_number import PhoneNumber
from ..types.row_version import RowVersion
from ..types.suffix import Suffix
from ..types.tax_number import TaxNumber
from ..types.title import Title
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_customer_response import UpdateCustomerResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from ..types.website import Website


OMIT = typing.cast(typing.Any, ...)


class RawCustomersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[CustomersFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetCustomersResponse]:
        """
        List Customers

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[CustomersFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCustomersResponse]
            Customers
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/customers",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=CustomersFilter, direction="write"
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
                    GetCustomersResponse,
                    parse_obj_as(
                        type_=GetCustomersResponse,
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
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[Id] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        parent: typing.Optional[LinkedParentCustomer] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        project: typing.Optional[bool] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[AccountingCustomerStatus] = OMIT,
        suffix: typing.Optional[Suffix] = OMIT,
        tax_number: typing.Optional[TaxNumber] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCustomerResponse]:
        """
        Create Customer

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        display_id : typing.Optional[str]
            Display ID

        display_name : typing.Optional[str]
            Display name

        downstream_id : typing.Optional[DownstreamId]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[Id]

        individual : typing.Optional[bool]
            Is this an individual or business customer

        last_name : typing.Optional[LastName]

        middle_name : typing.Optional[MiddleName]

        notes : typing.Optional[str]
            Some notes about this customer

        parent : typing.Optional[LinkedParentCustomer]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        project : typing.Optional[bool]
            If true, indicates this is a Project.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[AccountingCustomerStatus]
            Customer status

        suffix : typing.Optional[Suffix]

        tax_number : typing.Optional[TaxNumber]

        tax_rate : typing.Optional[LinkedTaxRate]

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateCustomerResponse]
            Customers
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/customers",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "bank_accounts": convert_and_respect_annotation_metadata(
                    object_=bank_accounts, annotation=typing.Sequence[BankAccount], direction="write"
                ),
                "company_name": company_name,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "display_id": display_id,
                "display_name": display_name,
                "downstream_id": downstream_id,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "first_name": first_name,
                "id": id,
                "individual": individual,
                "last_name": last_name,
                "middle_name": middle_name,
                "notes": notes,
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=typing.Optional[LinkedParentCustomer], direction="write"
                ),
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "project": project,
                "row_version": row_version,
                "status": status,
                "suffix": suffix,
                "tax_number": tax_number,
                "tax_rate": convert_and_respect_annotation_metadata(
                    object_=tax_rate, annotation=LinkedTaxRate, direction="write"
                ),
                "title": title,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "websites": convert_and_respect_annotation_metadata(
                    object_=websites, annotation=typing.Sequence[Website], direction="write"
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
                    CreateCustomerResponse,
                    parse_obj_as(
                        type_=CreateCustomerResponse,
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
    ) -> HttpResponse[GetCustomerResponse]:
        """
        Get Customer

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
        HttpResponse[GetCustomerResponse]
            Customer
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/customers/{jsonable_encoder(id)}",
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
                    GetCustomerResponse,
                    parse_obj_as(
                        type_=GetCustomerResponse,
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
    ) -> HttpResponse[DeleteCustomerResponse]:
        """
        Delete Customer

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
        HttpResponse[DeleteCustomerResponse]
            Customers
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/customers/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteCustomerResponse,
                    parse_obj_as(
                        type_=DeleteCustomerResponse,
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
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[Id] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        parent: typing.Optional[LinkedParentCustomer] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        project: typing.Optional[bool] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[AccountingCustomerStatus] = OMIT,
        suffix: typing.Optional[Suffix] = OMIT,
        tax_number: typing.Optional[TaxNumber] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateCustomerResponse]:
        """
        Update Customer

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        display_id : typing.Optional[str]
            Display ID

        display_name : typing.Optional[str]
            Display name

        downstream_id : typing.Optional[DownstreamId]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[Id]

        individual : typing.Optional[bool]
            Is this an individual or business customer

        last_name : typing.Optional[LastName]

        middle_name : typing.Optional[MiddleName]

        notes : typing.Optional[str]
            Some notes about this customer

        parent : typing.Optional[LinkedParentCustomer]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        project : typing.Optional[bool]
            If true, indicates this is a Project.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[AccountingCustomerStatus]
            Customer status

        suffix : typing.Optional[Suffix]

        tax_number : typing.Optional[TaxNumber]

        tax_rate : typing.Optional[LinkedTaxRate]

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateCustomerResponse]
            Customers
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/customers/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "bank_accounts": convert_and_respect_annotation_metadata(
                    object_=bank_accounts, annotation=typing.Sequence[BankAccount], direction="write"
                ),
                "company_name": company_name,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "display_id": display_id,
                "display_name": display_name,
                "downstream_id": downstream_id,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "first_name": first_name,
                "id": id,
                "individual": individual,
                "last_name": last_name,
                "middle_name": middle_name,
                "notes": notes,
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=typing.Optional[LinkedParentCustomer], direction="write"
                ),
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "project": project,
                "row_version": row_version,
                "status": status,
                "suffix": suffix,
                "tax_number": tax_number,
                "tax_rate": convert_and_respect_annotation_metadata(
                    object_=tax_rate, annotation=LinkedTaxRate, direction="write"
                ),
                "title": title,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "websites": convert_and_respect_annotation_metadata(
                    object_=websites, annotation=typing.Sequence[Website], direction="write"
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
                    UpdateCustomerResponse,
                    parse_obj_as(
                        type_=UpdateCustomerResponse,
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


class AsyncRawCustomersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[CustomersFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetCustomersResponse]:
        """
        List Customers

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[CustomersFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCustomersResponse]
            Customers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/customers",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=CustomersFilter, direction="write"
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
                    GetCustomersResponse,
                    parse_obj_as(
                        type_=GetCustomersResponse,
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
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[Id] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        parent: typing.Optional[LinkedParentCustomer] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        project: typing.Optional[bool] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[AccountingCustomerStatus] = OMIT,
        suffix: typing.Optional[Suffix] = OMIT,
        tax_number: typing.Optional[TaxNumber] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateCustomerResponse]:
        """
        Create Customer

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        display_id : typing.Optional[str]
            Display ID

        display_name : typing.Optional[str]
            Display name

        downstream_id : typing.Optional[DownstreamId]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[Id]

        individual : typing.Optional[bool]
            Is this an individual or business customer

        last_name : typing.Optional[LastName]

        middle_name : typing.Optional[MiddleName]

        notes : typing.Optional[str]
            Some notes about this customer

        parent : typing.Optional[LinkedParentCustomer]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        project : typing.Optional[bool]
            If true, indicates this is a Project.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[AccountingCustomerStatus]
            Customer status

        suffix : typing.Optional[Suffix]

        tax_number : typing.Optional[TaxNumber]

        tax_rate : typing.Optional[LinkedTaxRate]

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateCustomerResponse]
            Customers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/customers",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "bank_accounts": convert_and_respect_annotation_metadata(
                    object_=bank_accounts, annotation=typing.Sequence[BankAccount], direction="write"
                ),
                "company_name": company_name,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "display_id": display_id,
                "display_name": display_name,
                "downstream_id": downstream_id,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "first_name": first_name,
                "id": id,
                "individual": individual,
                "last_name": last_name,
                "middle_name": middle_name,
                "notes": notes,
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=typing.Optional[LinkedParentCustomer], direction="write"
                ),
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "project": project,
                "row_version": row_version,
                "status": status,
                "suffix": suffix,
                "tax_number": tax_number,
                "tax_rate": convert_and_respect_annotation_metadata(
                    object_=tax_rate, annotation=LinkedTaxRate, direction="write"
                ),
                "title": title,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "websites": convert_and_respect_annotation_metadata(
                    object_=websites, annotation=typing.Sequence[Website], direction="write"
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
                    CreateCustomerResponse,
                    parse_obj_as(
                        type_=CreateCustomerResponse,
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
    ) -> AsyncHttpResponse[GetCustomerResponse]:
        """
        Get Customer

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
        AsyncHttpResponse[GetCustomerResponse]
            Customer
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/customers/{jsonable_encoder(id)}",
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
                    GetCustomerResponse,
                    parse_obj_as(
                        type_=GetCustomerResponse,
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
    ) -> AsyncHttpResponse[DeleteCustomerResponse]:
        """
        Delete Customer

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
        AsyncHttpResponse[DeleteCustomerResponse]
            Customers
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/customers/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteCustomerResponse,
                    parse_obj_as(
                        type_=DeleteCustomerResponse,
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
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[Id] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        parent: typing.Optional[LinkedParentCustomer] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        project: typing.Optional[bool] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[AccountingCustomerStatus] = OMIT,
        suffix: typing.Optional[Suffix] = OMIT,
        tax_number: typing.Optional[TaxNumber] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateCustomerResponse]:
        """
        Update Customer

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        display_id : typing.Optional[str]
            Display ID

        display_name : typing.Optional[str]
            Display name

        downstream_id : typing.Optional[DownstreamId]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[Id]

        individual : typing.Optional[bool]
            Is this an individual or business customer

        last_name : typing.Optional[LastName]

        middle_name : typing.Optional[MiddleName]

        notes : typing.Optional[str]
            Some notes about this customer

        parent : typing.Optional[LinkedParentCustomer]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        project : typing.Optional[bool]
            If true, indicates this is a Project.

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[AccountingCustomerStatus]
            Customer status

        suffix : typing.Optional[Suffix]

        tax_number : typing.Optional[TaxNumber]

        tax_rate : typing.Optional[LinkedTaxRate]

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateCustomerResponse]
            Customers
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/customers/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "account": convert_and_respect_annotation_metadata(
                    object_=account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "addresses": convert_and_respect_annotation_metadata(
                    object_=addresses, annotation=typing.Sequence[Address], direction="write"
                ),
                "bank_accounts": convert_and_respect_annotation_metadata(
                    object_=bank_accounts, annotation=typing.Sequence[BankAccount], direction="write"
                ),
                "company_name": company_name,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "display_id": display_id,
                "display_name": display_name,
                "downstream_id": downstream_id,
                "emails": convert_and_respect_annotation_metadata(
                    object_=emails, annotation=typing.Sequence[Email], direction="write"
                ),
                "first_name": first_name,
                "id": id,
                "individual": individual,
                "last_name": last_name,
                "middle_name": middle_name,
                "notes": notes,
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=typing.Optional[LinkedParentCustomer], direction="write"
                ),
                "phone_numbers": convert_and_respect_annotation_metadata(
                    object_=phone_numbers, annotation=typing.Sequence[PhoneNumber], direction="write"
                ),
                "project": project,
                "row_version": row_version,
                "status": status,
                "suffix": suffix,
                "tax_number": tax_number,
                "tax_rate": convert_and_respect_annotation_metadata(
                    object_=tax_rate, annotation=LinkedTaxRate, direction="write"
                ),
                "title": title,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "websites": convert_and_respect_annotation_metadata(
                    object_=websites, annotation=typing.Sequence[Website], direction="write"
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
                    UpdateCustomerResponse,
                    parse_obj_as(
                        type_=UpdateCustomerResponse,
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
