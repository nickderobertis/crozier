

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.get_bank_account_by_v1id_response import GetBankAccountByV1IdResponse
from ..types.get_bank_account_response import GetBankAccountResponse
from ..types.list_bank_accounts_response import ListBankAccountsResponse
from pydantic import ValidationError


class RawBankAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_bank_accounts(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListBankAccountsResponse]:
        """
        Returns a list of [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) objects linked to a Square account.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor returned by a previous call to this endpoint.
            Use it in the next `ListBankAccounts` request to retrieve the next set
            of results.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        limit : typing.Optional[int]
            Upper limit on the number of bank accounts to return in the response.
            Currently, 1000 is the largest supported limit. You can specify a limit
            of up to 1000 bank accounts. This is also the default limit.

        location_id : typing.Optional[str]
            Location ID. You can specify this optional filter
            to retrieve only the linked bank accounts belonging to a specific location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListBankAccountsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/bank-accounts",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "location_id": location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListBankAccountsResponse,
                    parse_obj_as(
                        type_=ListBankAccountsResponse,
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

    def get_bank_account_by_v1id(
        self, v1bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBankAccountByV1IdResponse]:
        """
        Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) identified by V1 bank account ID.

        Parameters
        ----------
        v1bank_account_id : str
            Connect V1 ID of the desired `BankAccount`. For more information, see
            [Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBankAccountByV1IdResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bank-accounts/by-v1-id/{encode_path_param(v1bank_account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBankAccountByV1IdResponse,
                    parse_obj_as(
                        type_=GetBankAccountByV1IdResponse,
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

    def get_bank_account(
        self, bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBankAccountResponse]:
        """
        Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount)
        linked to a Square account.

        Parameters
        ----------
        bank_account_id : str
            Square-issued ID of the desired `BankAccount`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBankAccountResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/bank-accounts/{encode_path_param(bank_account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBankAccountResponse,
                    parse_obj_as(
                        type_=GetBankAccountResponse,
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


class AsyncRawBankAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_bank_accounts(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListBankAccountsResponse]:
        """
        Returns a list of [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) objects linked to a Square account.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor returned by a previous call to this endpoint.
            Use it in the next `ListBankAccounts` request to retrieve the next set
            of results.

            See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.

        limit : typing.Optional[int]
            Upper limit on the number of bank accounts to return in the response.
            Currently, 1000 is the largest supported limit. You can specify a limit
            of up to 1000 bank accounts. This is also the default limit.

        location_id : typing.Optional[str]
            Location ID. You can specify this optional filter
            to retrieve only the linked bank accounts belonging to a specific location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListBankAccountsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/bank-accounts",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "location_id": location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListBankAccountsResponse,
                    parse_obj_as(
                        type_=ListBankAccountsResponse,
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

    async def get_bank_account_by_v1id(
        self, v1bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBankAccountByV1IdResponse]:
        """
        Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) identified by V1 bank account ID.

        Parameters
        ----------
        v1bank_account_id : str
            Connect V1 ID of the desired `BankAccount`. For more information, see
            [Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBankAccountByV1IdResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bank-accounts/by-v1-id/{encode_path_param(v1bank_account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBankAccountByV1IdResponse,
                    parse_obj_as(
                        type_=GetBankAccountByV1IdResponse,
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

    async def get_bank_account(
        self, bank_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBankAccountResponse]:
        """
        Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount)
        linked to a Square account.

        Parameters
        ----------
        bank_account_id : str
            Square-issued ID of the desired `BankAccount`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBankAccountResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/bank-accounts/{encode_path_param(bank_account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBankAccountResponse,
                    parse_obj_as(
                        type_=GetBankAccountResponse,
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
