

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.accounting_create_or_update_account_request import AccountingCreateOrUpdateAccountRequest
from ..types.accounting_create_or_update_account_response import AccountingCreateOrUpdateAccountResponse
from ..types.accounting_delete_account_response import AccountingDeleteAccountResponse
from ..types.accounting_get_account_response import AccountingGetAccountResponse
from ..types.accounting_get_accounts_response import AccountingGetAccountsResponse
from ..types.common_base_error import CommonBaseError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAccountingAccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def accounting_account_get_account(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AccountingGetAccountResponse]:
        """
        Get details of an account

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccountingGetAccountResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/accounts/{encode_path_param(id)}",
            method="GET",
            params={
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountingGetAccountResponse,
                    parse_obj_as(
                        type_=AccountingGetAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def accounting_account_delete_account(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AccountingDeleteAccountResponse]:
        """
        Delete account

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccountingDeleteAccountResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/accounts/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountingDeleteAccountResponse,
                    parse_obj_as(
                        type_=AccountingDeleteAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def accounting_account_update_account(
        self,
        id: str,
        *,
        request: AccountingCreateOrUpdateAccountRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AccountingCreateOrUpdateAccountResponse]:
        """
        Update Account

        Parameters
        ----------
        id : str

        request : AccountingCreateOrUpdateAccountRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccountingCreateOrUpdateAccountResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/accounts/{encode_path_param(id)}",
            method="PATCH",
            params={
                "fields": fields,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountingCreateOrUpdateAccountResponse,
                    parse_obj_as(
                        type_=AccountingCreateOrUpdateAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def accounting_account_get_accounts(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AccountingGetAccountsResponse]:
        """
        Get all the accounts

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccountingGetAccountsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/accounts",
            method="GET",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountingGetAccountsResponse,
                    parse_obj_as(
                        type_=AccountingGetAccountsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def accounting_account_create_account(
        self,
        *,
        request: AccountingCreateOrUpdateAccountRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AccountingCreateOrUpdateAccountResponse]:
        """
        Post Account

        Parameters
        ----------
        request : AccountingCreateOrUpdateAccountRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccountingCreateOrUpdateAccountResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/accounts",
            method="POST",
            params={
                "fields": fields,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountingCreateOrUpdateAccountResponse,
                    parse_obj_as(
                        type_=AccountingCreateOrUpdateAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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


class AsyncRawAccountingAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def accounting_account_get_account(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AccountingGetAccountResponse]:
        """
        Get details of an account

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccountingGetAccountResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/accounts/{encode_path_param(id)}",
            method="GET",
            params={
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountingGetAccountResponse,
                    parse_obj_as(
                        type_=AccountingGetAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def accounting_account_delete_account(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AccountingDeleteAccountResponse]:
        """
        Delete account

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccountingDeleteAccountResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/accounts/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountingDeleteAccountResponse,
                    parse_obj_as(
                        type_=AccountingDeleteAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def accounting_account_update_account(
        self,
        id: str,
        *,
        request: AccountingCreateOrUpdateAccountRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AccountingCreateOrUpdateAccountResponse]:
        """
        Update Account

        Parameters
        ----------
        id : str

        request : AccountingCreateOrUpdateAccountRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccountingCreateOrUpdateAccountResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/accounts/{encode_path_param(id)}",
            method="PATCH",
            params={
                "fields": fields,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountingCreateOrUpdateAccountResponse,
                    parse_obj_as(
                        type_=AccountingCreateOrUpdateAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def accounting_account_get_accounts(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AccountingGetAccountsResponse]:
        """
        Get all the accounts

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccountingGetAccountsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/accounts",
            method="GET",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountingGetAccountsResponse,
                    parse_obj_as(
                        type_=AccountingGetAccountsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def accounting_account_create_account(
        self,
        *,
        request: AccountingCreateOrUpdateAccountRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AccountingCreateOrUpdateAccountResponse]:
        """
        Post Account

        Parameters
        ----------
        request : AccountingCreateOrUpdateAccountRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccountingCreateOrUpdateAccountResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/accounts",
            method="POST",
            params={
                "fields": fields,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountingCreateOrUpdateAccountResponse,
                    parse_obj_as(
                        type_=AccountingCreateOrUpdateAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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
