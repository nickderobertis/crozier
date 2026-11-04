

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_unified_search_get_providers200response import CoreUnifiedSearchGetProviders200Response
from ..types.core_unified_search_search200response import CoreUnifiedSearchSearch200Response
from pydantic import ValidationError


class RawCoreUnifiedSearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_providers(
        self, *, from_: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreUnifiedSearchGetProviders200Response]:
        """
        Parameters
        ----------
        from_ : typing.Optional[str]
            the url the user is currently at

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreUnifiedSearchGetProviders200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/search/providers",
            method="GET",
            params={
                "from": from_,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreUnifiedSearchGetProviders200Response,
                    parse_obj_as(
                        type_=CoreUnifiedSearchGetProviders200Response,
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

    def search(
        self,
        provider_id: str,
        *,
        term: typing.Optional[str] = None,
        sort_order: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreUnifiedSearchSearch200Response]:
        """
        Parameters
        ----------
        provider_id : str
            ID of the provider

        term : typing.Optional[str]
            Term to search

        sort_order : typing.Optional[int]
            Order of entries

        limit : typing.Optional[int]
            Maximum amount of entries

        cursor : typing.Optional[str]
            Offset for searching

        from_ : typing.Optional[str]
            The current user URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreUnifiedSearchSearch200Response]
            Search entries returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/search/providers/{encode_path_param(provider_id)}/search",
            method="GET",
            params={
                "term": term,
                "sortOrder": sort_order,
                "limit": limit,
                "cursor": cursor,
                "from": from_,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreUnifiedSearchSearch200Response,
                    parse_obj_as(
                        type_=CoreUnifiedSearchSearch200Response,
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


class AsyncRawCoreUnifiedSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_providers(
        self, *, from_: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreUnifiedSearchGetProviders200Response]:
        """
        Parameters
        ----------
        from_ : typing.Optional[str]
            the url the user is currently at

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreUnifiedSearchGetProviders200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/search/providers",
            method="GET",
            params={
                "from": from_,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreUnifiedSearchGetProviders200Response,
                    parse_obj_as(
                        type_=CoreUnifiedSearchGetProviders200Response,
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

    async def search(
        self,
        provider_id: str,
        *,
        term: typing.Optional[str] = None,
        sort_order: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreUnifiedSearchSearch200Response]:
        """
        Parameters
        ----------
        provider_id : str
            ID of the provider

        term : typing.Optional[str]
            Term to search

        sort_order : typing.Optional[int]
            Order of entries

        limit : typing.Optional[int]
            Maximum amount of entries

        cursor : typing.Optional[str]
            Offset for searching

        from_ : typing.Optional[str]
            The current user URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreUnifiedSearchSearch200Response]
            Search entries returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/search/providers/{encode_path_param(provider_id)}/search",
            method="GET",
            params={
                "term": term,
                "sortOrder": sort_order,
                "limit": limit,
                "cursor": cursor,
                "from": from_,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreUnifiedSearchSearch200Response,
                    parse_obj_as(
                        type_=CoreUnifiedSearchSearch200Response,
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
