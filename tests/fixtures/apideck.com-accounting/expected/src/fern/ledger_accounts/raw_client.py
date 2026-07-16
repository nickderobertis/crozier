

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
from ..types.bank_account import BankAccount
from ..types.create_ledger_account_response import CreateLedgerAccountResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.currency import Currency
from ..types.delete_ledger_account_response import DeleteLedgerAccountResponse
from ..types.get_ledger_account_response import GetLedgerAccountResponse
from ..types.get_ledger_accounts_response import GetLedgerAccountsResponse
from ..types.id import Id
from ..types.ledger_account_categories_item import LedgerAccountCategoriesItem
from ..types.ledger_account_classification import LedgerAccountClassification
from ..types.ledger_account_parent_account import LedgerAccountParentAccount
from ..types.ledger_account_status import LedgerAccountStatus
from ..types.ledger_account_sub_accounts_item import LedgerAccountSubAccountsItem
from ..types.ledger_account_type import LedgerAccountType
from ..types.linked_tax_rate import LinkedTaxRate
from ..types.not_found_response import NotFoundResponse
from ..types.pass_through_query import PassThroughQuery
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.row_version import RowVersion
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_ledger_account_response import UpdateLedgerAccountResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLedgerAccountsClient:
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
    ) -> HttpResponse[GetLedgerAccountsResponse]:
        """
        List Ledger Accounts

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
        HttpResponse[GetLedgerAccountsResponse]
            LedgerAccounts
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/ledger-accounts",
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
                    GetLedgerAccountsResponse,
                    parse_obj_as(
                        type_=GetLedgerAccountsResponse,
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
        active: typing.Optional[bool] = OMIT,
        bank_account: typing.Optional[BankAccount] = OMIT,
        categories: typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]] = OMIT,
        classification: typing.Optional[LedgerAccountClassification] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        fully_qualified_name: typing.Optional[str] = OMIT,
        header: typing.Optional[bool] = OMIT,
        id: typing.Optional[Id] = OMIT,
        last_reconciliation_date: typing.Optional[dt.date] = OMIT,
        level: typing.Optional[float] = OMIT,
        name: typing.Optional[str] = OMIT,
        nominal_code: typing.Optional[str] = OMIT,
        opening_balance: typing.Optional[float] = OMIT,
        parent_account: typing.Optional[LedgerAccountParentAccount] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[LedgerAccountStatus] = OMIT,
        sub_account: typing.Optional[bool] = OMIT,
        sub_accounts: typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        tax_type: typing.Optional[str] = OMIT,
        type: typing.Optional[LedgerAccountType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateLedgerAccountResponse]:
        """
        Create Ledger Account

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]
            Whether the account is active or not.

        bank_account : typing.Optional[BankAccount]

        categories : typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]]
            The categories of the account.

        classification : typing.Optional[LedgerAccountClassification]
            The classification of account.

        code : typing.Optional[str]
            The code assigned to the account.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        current_balance : typing.Optional[float]
            The current balance of the account.

        description : typing.Optional[str]
            The description of the account.

        display_id : typing.Optional[str]
            The human readable display ID used when displaying the account

        fully_qualified_name : typing.Optional[str]
            The fully qualified name of the account.

        header : typing.Optional[bool]
            Whether the account is a header or not.

        id : typing.Optional[Id]

        last_reconciliation_date : typing.Optional[dt.date]
            Reconciliation Date means the last calendar day of each Reconciliation Period.

        level : typing.Optional[float]

        name : typing.Optional[str]
            The name of the account.

        nominal_code : typing.Optional[str]
            The nominal code of the ledger account.

        opening_balance : typing.Optional[float]
            The opening balance of the account.

        parent_account : typing.Optional[LedgerAccountParentAccount]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[LedgerAccountStatus]
            The status of the account.

        sub_account : typing.Optional[bool]
            Whether the account is a sub account or not.

        sub_accounts : typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]]
            The sub accounts of the account.

        sub_type : typing.Optional[str]
            The sub type of account.

        tax_rate : typing.Optional[LinkedTaxRate]

        tax_type : typing.Optional[str]
            The tax type of the account.

        type : typing.Optional[LedgerAccountType]
            The type of account.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateLedgerAccountResponse]
            LedgerAccount created
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/ledger-accounts",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "bank_account": convert_and_respect_annotation_metadata(
                    object_=bank_account, annotation=BankAccount, direction="write"
                ),
                "categories": convert_and_respect_annotation_metadata(
                    object_=categories, annotation=typing.Sequence[LedgerAccountCategoriesItem], direction="write"
                ),
                "classification": classification,
                "code": code,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "current_balance": current_balance,
                "description": description,
                "display_id": display_id,
                "fully_qualified_name": fully_qualified_name,
                "header": header,
                "id": id,
                "last_reconciliation_date": last_reconciliation_date,
                "level": level,
                "name": name,
                "nominal_code": nominal_code,
                "opening_balance": opening_balance,
                "parent_account": convert_and_respect_annotation_metadata(
                    object_=parent_account, annotation=LedgerAccountParentAccount, direction="write"
                ),
                "row_version": row_version,
                "status": status,
                "sub_account": sub_account,
                "sub_accounts": convert_and_respect_annotation_metadata(
                    object_=sub_accounts, annotation=typing.Sequence[LedgerAccountSubAccountsItem], direction="write"
                ),
                "sub_type": sub_type,
                "tax_rate": convert_and_respect_annotation_metadata(
                    object_=tax_rate, annotation=LinkedTaxRate, direction="write"
                ),
                "tax_type": tax_type,
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
                    CreateLedgerAccountResponse,
                    parse_obj_as(
                        type_=CreateLedgerAccountResponse,
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
    ) -> HttpResponse[GetLedgerAccountResponse]:
        """
        Get Ledger Account

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
        HttpResponse[GetLedgerAccountResponse]
            LedgerAccount
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/ledger-accounts/{encode_path_param(id)}",
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
                    GetLedgerAccountResponse,
                    parse_obj_as(
                        type_=GetLedgerAccountResponse,
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
    ) -> HttpResponse[DeleteLedgerAccountResponse]:
        """
        Delete Ledger Account

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
        HttpResponse[DeleteLedgerAccountResponse]
            LedgerAccount deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/ledger-accounts/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteLedgerAccountResponse,
                    parse_obj_as(
                        type_=DeleteLedgerAccountResponse,
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
        active: typing.Optional[bool] = OMIT,
        bank_account: typing.Optional[BankAccount] = OMIT,
        categories: typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]] = OMIT,
        classification: typing.Optional[LedgerAccountClassification] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        fully_qualified_name: typing.Optional[str] = OMIT,
        header: typing.Optional[bool] = OMIT,
        id: typing.Optional[Id] = OMIT,
        last_reconciliation_date: typing.Optional[dt.date] = OMIT,
        level: typing.Optional[float] = OMIT,
        name: typing.Optional[str] = OMIT,
        nominal_code: typing.Optional[str] = OMIT,
        opening_balance: typing.Optional[float] = OMIT,
        parent_account: typing.Optional[LedgerAccountParentAccount] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[LedgerAccountStatus] = OMIT,
        sub_account: typing.Optional[bool] = OMIT,
        sub_accounts: typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        tax_type: typing.Optional[str] = OMIT,
        type: typing.Optional[LedgerAccountType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateLedgerAccountResponse]:
        """
        Update Ledger Account

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]
            Whether the account is active or not.

        bank_account : typing.Optional[BankAccount]

        categories : typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]]
            The categories of the account.

        classification : typing.Optional[LedgerAccountClassification]
            The classification of account.

        code : typing.Optional[str]
            The code assigned to the account.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        current_balance : typing.Optional[float]
            The current balance of the account.

        description : typing.Optional[str]
            The description of the account.

        display_id : typing.Optional[str]
            The human readable display ID used when displaying the account

        fully_qualified_name : typing.Optional[str]
            The fully qualified name of the account.

        header : typing.Optional[bool]
            Whether the account is a header or not.

        id : typing.Optional[Id]

        last_reconciliation_date : typing.Optional[dt.date]
            Reconciliation Date means the last calendar day of each Reconciliation Period.

        level : typing.Optional[float]

        name : typing.Optional[str]
            The name of the account.

        nominal_code : typing.Optional[str]
            The nominal code of the ledger account.

        opening_balance : typing.Optional[float]
            The opening balance of the account.

        parent_account : typing.Optional[LedgerAccountParentAccount]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[LedgerAccountStatus]
            The status of the account.

        sub_account : typing.Optional[bool]
            Whether the account is a sub account or not.

        sub_accounts : typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]]
            The sub accounts of the account.

        sub_type : typing.Optional[str]
            The sub type of account.

        tax_rate : typing.Optional[LinkedTaxRate]

        tax_type : typing.Optional[str]
            The tax type of the account.

        type : typing.Optional[LedgerAccountType]
            The type of account.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateLedgerAccountResponse]
            LedgerAccount updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/ledger-accounts/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "bank_account": convert_and_respect_annotation_metadata(
                    object_=bank_account, annotation=BankAccount, direction="write"
                ),
                "categories": convert_and_respect_annotation_metadata(
                    object_=categories, annotation=typing.Sequence[LedgerAccountCategoriesItem], direction="write"
                ),
                "classification": classification,
                "code": code,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "current_balance": current_balance,
                "description": description,
                "display_id": display_id,
                "fully_qualified_name": fully_qualified_name,
                "header": header,
                "id": id,
                "last_reconciliation_date": last_reconciliation_date,
                "level": level,
                "name": name,
                "nominal_code": nominal_code,
                "opening_balance": opening_balance,
                "parent_account": convert_and_respect_annotation_metadata(
                    object_=parent_account, annotation=LedgerAccountParentAccount, direction="write"
                ),
                "row_version": row_version,
                "status": status,
                "sub_account": sub_account,
                "sub_accounts": convert_and_respect_annotation_metadata(
                    object_=sub_accounts, annotation=typing.Sequence[LedgerAccountSubAccountsItem], direction="write"
                ),
                "sub_type": sub_type,
                "tax_rate": convert_and_respect_annotation_metadata(
                    object_=tax_rate, annotation=LinkedTaxRate, direction="write"
                ),
                "tax_type": tax_type,
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
                    UpdateLedgerAccountResponse,
                    parse_obj_as(
                        type_=UpdateLedgerAccountResponse,
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


class AsyncRawLedgerAccountsClient:
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
    ) -> AsyncHttpResponse[GetLedgerAccountsResponse]:
        """
        List Ledger Accounts

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
        AsyncHttpResponse[GetLedgerAccountsResponse]
            LedgerAccounts
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/ledger-accounts",
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
                    GetLedgerAccountsResponse,
                    parse_obj_as(
                        type_=GetLedgerAccountsResponse,
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
        active: typing.Optional[bool] = OMIT,
        bank_account: typing.Optional[BankAccount] = OMIT,
        categories: typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]] = OMIT,
        classification: typing.Optional[LedgerAccountClassification] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        fully_qualified_name: typing.Optional[str] = OMIT,
        header: typing.Optional[bool] = OMIT,
        id: typing.Optional[Id] = OMIT,
        last_reconciliation_date: typing.Optional[dt.date] = OMIT,
        level: typing.Optional[float] = OMIT,
        name: typing.Optional[str] = OMIT,
        nominal_code: typing.Optional[str] = OMIT,
        opening_balance: typing.Optional[float] = OMIT,
        parent_account: typing.Optional[LedgerAccountParentAccount] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[LedgerAccountStatus] = OMIT,
        sub_account: typing.Optional[bool] = OMIT,
        sub_accounts: typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        tax_type: typing.Optional[str] = OMIT,
        type: typing.Optional[LedgerAccountType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateLedgerAccountResponse]:
        """
        Create Ledger Account

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]
            Whether the account is active or not.

        bank_account : typing.Optional[BankAccount]

        categories : typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]]
            The categories of the account.

        classification : typing.Optional[LedgerAccountClassification]
            The classification of account.

        code : typing.Optional[str]
            The code assigned to the account.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        current_balance : typing.Optional[float]
            The current balance of the account.

        description : typing.Optional[str]
            The description of the account.

        display_id : typing.Optional[str]
            The human readable display ID used when displaying the account

        fully_qualified_name : typing.Optional[str]
            The fully qualified name of the account.

        header : typing.Optional[bool]
            Whether the account is a header or not.

        id : typing.Optional[Id]

        last_reconciliation_date : typing.Optional[dt.date]
            Reconciliation Date means the last calendar day of each Reconciliation Period.

        level : typing.Optional[float]

        name : typing.Optional[str]
            The name of the account.

        nominal_code : typing.Optional[str]
            The nominal code of the ledger account.

        opening_balance : typing.Optional[float]
            The opening balance of the account.

        parent_account : typing.Optional[LedgerAccountParentAccount]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[LedgerAccountStatus]
            The status of the account.

        sub_account : typing.Optional[bool]
            Whether the account is a sub account or not.

        sub_accounts : typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]]
            The sub accounts of the account.

        sub_type : typing.Optional[str]
            The sub type of account.

        tax_rate : typing.Optional[LinkedTaxRate]

        tax_type : typing.Optional[str]
            The tax type of the account.

        type : typing.Optional[LedgerAccountType]
            The type of account.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateLedgerAccountResponse]
            LedgerAccount created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/ledger-accounts",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "bank_account": convert_and_respect_annotation_metadata(
                    object_=bank_account, annotation=BankAccount, direction="write"
                ),
                "categories": convert_and_respect_annotation_metadata(
                    object_=categories, annotation=typing.Sequence[LedgerAccountCategoriesItem], direction="write"
                ),
                "classification": classification,
                "code": code,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "current_balance": current_balance,
                "description": description,
                "display_id": display_id,
                "fully_qualified_name": fully_qualified_name,
                "header": header,
                "id": id,
                "last_reconciliation_date": last_reconciliation_date,
                "level": level,
                "name": name,
                "nominal_code": nominal_code,
                "opening_balance": opening_balance,
                "parent_account": convert_and_respect_annotation_metadata(
                    object_=parent_account, annotation=LedgerAccountParentAccount, direction="write"
                ),
                "row_version": row_version,
                "status": status,
                "sub_account": sub_account,
                "sub_accounts": convert_and_respect_annotation_metadata(
                    object_=sub_accounts, annotation=typing.Sequence[LedgerAccountSubAccountsItem], direction="write"
                ),
                "sub_type": sub_type,
                "tax_rate": convert_and_respect_annotation_metadata(
                    object_=tax_rate, annotation=LinkedTaxRate, direction="write"
                ),
                "tax_type": tax_type,
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
                    CreateLedgerAccountResponse,
                    parse_obj_as(
                        type_=CreateLedgerAccountResponse,
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
    ) -> AsyncHttpResponse[GetLedgerAccountResponse]:
        """
        Get Ledger Account

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
        AsyncHttpResponse[GetLedgerAccountResponse]
            LedgerAccount
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/ledger-accounts/{encode_path_param(id)}",
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
                    GetLedgerAccountResponse,
                    parse_obj_as(
                        type_=GetLedgerAccountResponse,
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
    ) -> AsyncHttpResponse[DeleteLedgerAccountResponse]:
        """
        Delete Ledger Account

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
        AsyncHttpResponse[DeleteLedgerAccountResponse]
            LedgerAccount deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/ledger-accounts/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteLedgerAccountResponse,
                    parse_obj_as(
                        type_=DeleteLedgerAccountResponse,
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
        active: typing.Optional[bool] = OMIT,
        bank_account: typing.Optional[BankAccount] = OMIT,
        categories: typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]] = OMIT,
        classification: typing.Optional[LedgerAccountClassification] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        fully_qualified_name: typing.Optional[str] = OMIT,
        header: typing.Optional[bool] = OMIT,
        id: typing.Optional[Id] = OMIT,
        last_reconciliation_date: typing.Optional[dt.date] = OMIT,
        level: typing.Optional[float] = OMIT,
        name: typing.Optional[str] = OMIT,
        nominal_code: typing.Optional[str] = OMIT,
        opening_balance: typing.Optional[float] = OMIT,
        parent_account: typing.Optional[LedgerAccountParentAccount] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[LedgerAccountStatus] = OMIT,
        sub_account: typing.Optional[bool] = OMIT,
        sub_accounts: typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        tax_type: typing.Optional[str] = OMIT,
        type: typing.Optional[LedgerAccountType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateLedgerAccountResponse]:
        """
        Update Ledger Account

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]
            Whether the account is active or not.

        bank_account : typing.Optional[BankAccount]

        categories : typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]]
            The categories of the account.

        classification : typing.Optional[LedgerAccountClassification]
            The classification of account.

        code : typing.Optional[str]
            The code assigned to the account.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        current_balance : typing.Optional[float]
            The current balance of the account.

        description : typing.Optional[str]
            The description of the account.

        display_id : typing.Optional[str]
            The human readable display ID used when displaying the account

        fully_qualified_name : typing.Optional[str]
            The fully qualified name of the account.

        header : typing.Optional[bool]
            Whether the account is a header or not.

        id : typing.Optional[Id]

        last_reconciliation_date : typing.Optional[dt.date]
            Reconciliation Date means the last calendar day of each Reconciliation Period.

        level : typing.Optional[float]

        name : typing.Optional[str]
            The name of the account.

        nominal_code : typing.Optional[str]
            The nominal code of the ledger account.

        opening_balance : typing.Optional[float]
            The opening balance of the account.

        parent_account : typing.Optional[LedgerAccountParentAccount]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[LedgerAccountStatus]
            The status of the account.

        sub_account : typing.Optional[bool]
            Whether the account is a sub account or not.

        sub_accounts : typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]]
            The sub accounts of the account.

        sub_type : typing.Optional[str]
            The sub type of account.

        tax_rate : typing.Optional[LinkedTaxRate]

        tax_type : typing.Optional[str]
            The tax type of the account.

        type : typing.Optional[LedgerAccountType]
            The type of account.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateLedgerAccountResponse]
            LedgerAccount updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/ledger-accounts/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "bank_account": convert_and_respect_annotation_metadata(
                    object_=bank_account, annotation=BankAccount, direction="write"
                ),
                "categories": convert_and_respect_annotation_metadata(
                    object_=categories, annotation=typing.Sequence[LedgerAccountCategoriesItem], direction="write"
                ),
                "classification": classification,
                "code": code,
                "created_at": created_at,
                "created_by": created_by,
                "currency": currency,
                "current_balance": current_balance,
                "description": description,
                "display_id": display_id,
                "fully_qualified_name": fully_qualified_name,
                "header": header,
                "id": id,
                "last_reconciliation_date": last_reconciliation_date,
                "level": level,
                "name": name,
                "nominal_code": nominal_code,
                "opening_balance": opening_balance,
                "parent_account": convert_and_respect_annotation_metadata(
                    object_=parent_account, annotation=LedgerAccountParentAccount, direction="write"
                ),
                "row_version": row_version,
                "status": status,
                "sub_account": sub_account,
                "sub_accounts": convert_and_respect_annotation_metadata(
                    object_=sub_accounts, annotation=typing.Sequence[LedgerAccountSubAccountsItem], direction="write"
                ),
                "sub_type": sub_type,
                "tax_rate": convert_and_respect_annotation_metadata(
                    object_=tax_rate, annotation=LinkedTaxRate, direction="write"
                ),
                "tax_type": tax_type,
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
                    UpdateLedgerAccountResponse,
                    parse_obj_as(
                        type_=UpdateLedgerAccountResponse,
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
