

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
from ..types.account_category import AccountCategory
from ..types.categories import Categories
from ..types.categorised_account import CategorisedAccount
from ..types.categorised_accounts import CategorisedAccounts
from .types.confirm_categories_categories_item import ConfirmCategoriesCategoriesItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCategoriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_available_account_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Categories]:
        """
        Lists available account categories Codat's categorisation engine can provide.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Categories]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "data/assess/accounts/categories",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Categories,
                    parse_obj_as(
                        type_=Categories,
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

    def list_accounts_categories(
        self,
        company_id: str,
        connection_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CategorisedAccounts]:
        """
        Lists suggested and confirmed chart of account categories for the given company and data connection.

        Parameters
        ----------
        company_id : str

        connection_id : str

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        order_by : typing.Optional[str]
            Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CategorisedAccounts]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/accounts/categories",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "query": query,
                "orderBy": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CategorisedAccounts,
                    parse_obj_as(
                        type_=CategorisedAccounts,
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

    def update_accounts_categories(
        self,
        company_id: str,
        connection_id: str,
        *,
        categories: typing.Optional[typing.Sequence[ConfirmCategoriesCategoriesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[CategorisedAccount]]:
        """
        Comfirms the categories for all or a batch of accounts for a specific connection.

        Parameters
        ----------
        company_id : str

        connection_id : str

        categories : typing.Optional[typing.Sequence[ConfirmCategoriesCategoriesItem]]
            List of confirmed account categories set manually by the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CategorisedAccount]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/accounts/categories",
            method="PATCH",
            json={
                "categories": convert_and_respect_annotation_metadata(
                    object_=categories, annotation=typing.Sequence[ConfirmCategoriesCategoriesItem], direction="write"
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
                    typing.List[CategorisedAccount],
                    parse_obj_as(
                        type_=typing.List[CategorisedAccount],
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

    def get_account_category(
        self,
        company_id: str,
        connection_id: str,
        account_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CategorisedAccount]:
        """
        Get category for specific nominal account.

        Parameters
        ----------
        company_id : str

        connection_id : str

        account_id : str
            Nominal account id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CategorisedAccount]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/accounts/{encode_path_param(account_id)}/categories",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CategorisedAccount,
                    parse_obj_as(
                        type_=CategorisedAccount,
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

    def update_account_category(
        self,
        company_id: str,
        connection_id: str,
        account_id: str,
        *,
        confirmed: AccountCategory,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CategorisedAccount]:
        """
        Update category for a specific nominal account

        Parameters
        ----------
        company_id : str

        connection_id : str

        account_id : str
            Nominal account id

        confirmed : AccountCategory

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CategorisedAccount]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/accounts/{encode_path_param(account_id)}/categories",
            method="PATCH",
            json={
                "confirmed": convert_and_respect_annotation_metadata(
                    object_=confirmed, annotation=AccountCategory, direction="write"
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
                    CategorisedAccount,
                    parse_obj_as(
                        type_=CategorisedAccount,
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


class AsyncRawCategoriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_available_account_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Categories]:
        """
        Lists available account categories Codat's categorisation engine can provide.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Categories]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "data/assess/accounts/categories",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Categories,
                    parse_obj_as(
                        type_=Categories,
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

    async def list_accounts_categories(
        self,
        company_id: str,
        connection_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CategorisedAccounts]:
        """
        Lists suggested and confirmed chart of account categories for the given company and data connection.

        Parameters
        ----------
        company_id : str

        connection_id : str

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        order_by : typing.Optional[str]
            Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CategorisedAccounts]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/accounts/categories",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "query": query,
                "orderBy": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CategorisedAccounts,
                    parse_obj_as(
                        type_=CategorisedAccounts,
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

    async def update_accounts_categories(
        self,
        company_id: str,
        connection_id: str,
        *,
        categories: typing.Optional[typing.Sequence[ConfirmCategoriesCategoriesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[CategorisedAccount]]:
        """
        Comfirms the categories for all or a batch of accounts for a specific connection.

        Parameters
        ----------
        company_id : str

        connection_id : str

        categories : typing.Optional[typing.Sequence[ConfirmCategoriesCategoriesItem]]
            List of confirmed account categories set manually by the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CategorisedAccount]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/accounts/categories",
            method="PATCH",
            json={
                "categories": convert_and_respect_annotation_metadata(
                    object_=categories, annotation=typing.Sequence[ConfirmCategoriesCategoriesItem], direction="write"
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
                    typing.List[CategorisedAccount],
                    parse_obj_as(
                        type_=typing.List[CategorisedAccount],
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

    async def get_account_category(
        self,
        company_id: str,
        connection_id: str,
        account_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CategorisedAccount]:
        """
        Get category for specific nominal account.

        Parameters
        ----------
        company_id : str

        connection_id : str

        account_id : str
            Nominal account id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CategorisedAccount]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/accounts/{encode_path_param(account_id)}/categories",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CategorisedAccount,
                    parse_obj_as(
                        type_=CategorisedAccount,
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

    async def update_account_category(
        self,
        company_id: str,
        connection_id: str,
        account_id: str,
        *,
        confirmed: AccountCategory,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CategorisedAccount]:
        """
        Update category for a specific nominal account

        Parameters
        ----------
        company_id : str

        connection_id : str

        account_id : str
            Nominal account id

        confirmed : AccountCategory

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CategorisedAccount]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/accounts/{encode_path_param(account_id)}/categories",
            method="PATCH",
            json={
                "confirmed": convert_and_respect_annotation_metadata(
                    object_=confirmed, annotation=AccountCategory, direction="write"
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
                    CategorisedAccount,
                    parse_obj_as(
                        type_=CategorisedAccount,
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
