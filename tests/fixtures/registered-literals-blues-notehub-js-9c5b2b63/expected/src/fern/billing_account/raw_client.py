

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_billing_account_balance_history_response import GetBillingAccountBalanceHistoryResponse
from .types.get_billing_account_response import GetBillingAccountResponse
from .types.get_billing_accounts_response import GetBillingAccountsResponse
from pydantic import ValidationError


class RawBillingAccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_billing_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBillingAccountsResponse]:
        """
        Get Billing Accounts accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBillingAccountsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/billing-accounts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBillingAccountsResponse,
                    parse_obj_as(
                        type_=GetBillingAccountsResponse,
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

    def get_billing_account(
        self, billing_account_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBillingAccountResponse]:
        """
        Get Billing Account Information

        Parameters
        ----------
        billing_account_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBillingAccountResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/billing-accounts/{encode_path_param(billing_account_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBillingAccountResponse,
                    parse_obj_as(
                        type_=GetBillingAccountResponse,
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

    def get_billing_account_balance_history(
        self,
        billing_account_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetBillingAccountBalanceHistoryResponse]:
        """
        Get Billing Account Balance history

        Parameters
        ----------
        billing_account_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBillingAccountBalanceHistoryResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/billing-accounts/{encode_path_param(billing_account_uid)}/balance-history",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBillingAccountBalanceHistoryResponse,
                    parse_obj_as(
                        type_=GetBillingAccountBalanceHistoryResponse,
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


class AsyncRawBillingAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_billing_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBillingAccountsResponse]:
        """
        Get Billing Accounts accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBillingAccountsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/billing-accounts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBillingAccountsResponse,
                    parse_obj_as(
                        type_=GetBillingAccountsResponse,
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

    async def get_billing_account(
        self, billing_account_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBillingAccountResponse]:
        """
        Get Billing Account Information

        Parameters
        ----------
        billing_account_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBillingAccountResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/billing-accounts/{encode_path_param(billing_account_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBillingAccountResponse,
                    parse_obj_as(
                        type_=GetBillingAccountResponse,
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

    async def get_billing_account_balance_history(
        self,
        billing_account_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetBillingAccountBalanceHistoryResponse]:
        """
        Get Billing Account Balance history

        Parameters
        ----------
        billing_account_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBillingAccountBalanceHistoryResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/billing-accounts/{encode_path_param(billing_account_uid)}/balance-history",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBillingAccountBalanceHistoryResponse,
                    parse_obj_as(
                        type_=GetBillingAccountBalanceHistoryResponse,
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
