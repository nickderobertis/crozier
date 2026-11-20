

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.get_params_default_object_query_request_filter import GetParamsDefaultObjectQueryRequestFilter
from .types.get_params_default_object_query_response import GetParamsDefaultObjectQueryResponse
from .types.get_params_mixed_query_request_statuses_item import GetParamsMixedQueryRequestStatusesItem
from .types.get_params_mixed_query_response import GetParamsMixedQueryResponse
from .types.get_params_simple_query_request_order_by import GetParamsSimpleQueryRequestOrderBy
from .types.get_params_simple_query_response import GetParamsSimpleQueryResponse
from .types.get_params_unexploded_object_query_request_filter import GetParamsUnexplodedObjectQueryRequestFilter
from .types.get_params_unexploded_object_query_response import GetParamsUnexplodedObjectQueryResponse
from pydantic import ValidationError


class RawQueryParametersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_params_simple_query(
        self,
        *,
        order_by: GetParamsSimpleQueryRequestOrderBy,
        limit: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetParamsSimpleQueryResponse]:
        """
        Parameters
        ----------
        order_by : GetParamsSimpleQueryRequestOrderBy

        limit : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetParamsSimpleQueryResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "params/simple-query",
            method="GET",
            params={
                "orderBy": order_by,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetParamsSimpleQueryResponse,
                    parse_obj_as(
                        type_=GetParamsSimpleQueryResponse,
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

    def get_params_default_object_query(
        self,
        *,
        filter: GetParamsDefaultObjectQueryRequestFilter,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetParamsDefaultObjectQueryResponse]:
        """
        Parameters
        ----------
        filter : GetParamsDefaultObjectQueryRequestFilter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetParamsDefaultObjectQueryResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "params/default-object-query",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=GetParamsDefaultObjectQueryRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetParamsDefaultObjectQueryResponse,
                    parse_obj_as(
                        type_=GetParamsDefaultObjectQueryResponse,
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

    def get_params_unexploded_object_query(
        self,
        *,
        filter: GetParamsUnexplodedObjectQueryRequestFilter,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetParamsUnexplodedObjectQueryResponse]:
        """
        Parameters
        ----------
        filter : GetParamsUnexplodedObjectQueryRequestFilter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetParamsUnexplodedObjectQueryResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "params/unexploded-object-query",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=GetParamsUnexplodedObjectQueryRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetParamsUnexplodedObjectQueryResponse,
                    parse_obj_as(
                        type_=GetParamsUnexplodedObjectQueryResponse,
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

    def get_params_mixed_query(
        self,
        *,
        limit: float,
        kebab_case: str,
        author_ids: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        statuses: typing.Optional[
            typing.Union[
                GetParamsMixedQueryRequestStatusesItem, typing.Sequence[GetParamsMixedQueryRequestStatusesItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetParamsMixedQueryResponse]:
        """
        Parameters
        ----------
        limit : float

        kebab_case : str

        author_ids : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        statuses : typing.Optional[typing.Union[GetParamsMixedQueryRequestStatusesItem, typing.Sequence[GetParamsMixedQueryRequestStatusesItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetParamsMixedQueryResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "params/mixed-query",
            method="GET",
            params={
                "limit": limit,
                "author_ids": author_ids,
                "kebab-case": kebab_case,
                "statuses": statuses,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetParamsMixedQueryResponse,
                    parse_obj_as(
                        type_=GetParamsMixedQueryResponse,
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


class AsyncRawQueryParametersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_params_simple_query(
        self,
        *,
        order_by: GetParamsSimpleQueryRequestOrderBy,
        limit: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetParamsSimpleQueryResponse]:
        """
        Parameters
        ----------
        order_by : GetParamsSimpleQueryRequestOrderBy

        limit : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetParamsSimpleQueryResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "params/simple-query",
            method="GET",
            params={
                "orderBy": order_by,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetParamsSimpleQueryResponse,
                    parse_obj_as(
                        type_=GetParamsSimpleQueryResponse,
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

    async def get_params_default_object_query(
        self,
        *,
        filter: GetParamsDefaultObjectQueryRequestFilter,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetParamsDefaultObjectQueryResponse]:
        """
        Parameters
        ----------
        filter : GetParamsDefaultObjectQueryRequestFilter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetParamsDefaultObjectQueryResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "params/default-object-query",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=GetParamsDefaultObjectQueryRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetParamsDefaultObjectQueryResponse,
                    parse_obj_as(
                        type_=GetParamsDefaultObjectQueryResponse,
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

    async def get_params_unexploded_object_query(
        self,
        *,
        filter: GetParamsUnexplodedObjectQueryRequestFilter,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetParamsUnexplodedObjectQueryResponse]:
        """
        Parameters
        ----------
        filter : GetParamsUnexplodedObjectQueryRequestFilter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetParamsUnexplodedObjectQueryResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "params/unexploded-object-query",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=GetParamsUnexplodedObjectQueryRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetParamsUnexplodedObjectQueryResponse,
                    parse_obj_as(
                        type_=GetParamsUnexplodedObjectQueryResponse,
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

    async def get_params_mixed_query(
        self,
        *,
        limit: float,
        kebab_case: str,
        author_ids: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        statuses: typing.Optional[
            typing.Union[
                GetParamsMixedQueryRequestStatusesItem, typing.Sequence[GetParamsMixedQueryRequestStatusesItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetParamsMixedQueryResponse]:
        """
        Parameters
        ----------
        limit : float

        kebab_case : str

        author_ids : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        statuses : typing.Optional[typing.Union[GetParamsMixedQueryRequestStatusesItem, typing.Sequence[GetParamsMixedQueryRequestStatusesItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetParamsMixedQueryResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "params/mixed-query",
            method="GET",
            params={
                "limit": limit,
                "author_ids": author_ids,
                "kebab-case": kebab_case,
                "statuses": statuses,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetParamsMixedQueryResponse,
                    parse_obj_as(
                        type_=GetParamsMixedQueryResponse,
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
