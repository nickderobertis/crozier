

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.query_response import QueryResponse
from ..types.store_item import StoreItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_item(
        self, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StoreItem]:
        """
        Parameters
        ----------
        item_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StoreItem]
            The item.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"items/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StoreItem,
                    parse_obj_as(
                        type_=StoreItem,
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

    def run_query(
        self, *, scope_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[QueryResponse]:
        """
        Parameters
        ----------
        scope_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryResponse]
            The query result or status.
        """
        _response = self._client_wrapper.httpx_client.request(
            "queries",
            method="POST",
            json={
                "scope_id": scope_id,
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
                    QueryResponse,
                    parse_obj_as(
                        type_=QueryResponse,
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


class AsyncRawItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_item(
        self, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StoreItem]:
        """
        Parameters
        ----------
        item_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StoreItem]
            The item.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"items/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StoreItem,
                    parse_obj_as(
                        type_=StoreItem,
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

    async def run_query(
        self, *, scope_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[QueryResponse]:
        """
        Parameters
        ----------
        scope_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryResponse]
            The query result or status.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "queries",
            method="POST",
            json={
                "scope_id": scope_id,
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
                    QueryResponse,
                    parse_obj_as(
                        type_=QueryResponse,
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
