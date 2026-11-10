

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.unauthorized_error import UnauthorizedError
from .types.log_filters_sort_direction import LogFiltersSortDirection
from .types.post_logs_response import PostLogsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def returns_logs(
        self,
        *,
        type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        attributes: typing.Optional[typing.Sequence[str]] = OMIT,
        message: typing.Optional[str] = OMIT,
        page_size: typing.Optional[float] = OMIT,
        page_index: typing.Optional[float] = OMIT,
        sort_direction: typing.Optional[LogFiltersSortDirection] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostLogsResponse]:
        """
        Returns logs. For users with the Standard Registry role only.

        Parameters
        ----------
        type : typing.Optional[str]

        start_date : typing.Optional[str]

        end_date : typing.Optional[str]

        attributes : typing.Optional[typing.Sequence[str]]

        message : typing.Optional[str]

        page_size : typing.Optional[float]

        page_index : typing.Optional[float]

        sort_direction : typing.Optional[LogFiltersSortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLogsResponse]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            "logs",
            method="POST",
            json={
                "type": type,
                "startDate": start_date,
                "endDate": end_date,
                "attributes": attributes,
                "message": message,
                "pageSize": page_size,
                "pageIndex": page_index,
                "sortDirection": sort_direction,
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
                    PostLogsResponse,
                    parse_obj_as(
                        type_=PostLogsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def returns_logs_attributes(
        self,
        *,
        name: typing.Optional[str] = None,
        existing_attributes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Returns logs attributes. For users with the Standard Registry role only.

        Parameters
        ----------
        name : typing.Optional[str]
            Part of name.

        existing_attributes : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Attributes to exclude.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Successful operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            "logs/attributes",
            method="GET",
            params={
                "name": name,
                "existingAttributes": existing_attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def returns_logs(
        self,
        *,
        type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        attributes: typing.Optional[typing.Sequence[str]] = OMIT,
        message: typing.Optional[str] = OMIT,
        page_size: typing.Optional[float] = OMIT,
        page_index: typing.Optional[float] = OMIT,
        sort_direction: typing.Optional[LogFiltersSortDirection] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostLogsResponse]:
        """
        Returns logs. For users with the Standard Registry role only.

        Parameters
        ----------
        type : typing.Optional[str]

        start_date : typing.Optional[str]

        end_date : typing.Optional[str]

        attributes : typing.Optional[typing.Sequence[str]]

        message : typing.Optional[str]

        page_size : typing.Optional[float]

        page_index : typing.Optional[float]

        sort_direction : typing.Optional[LogFiltersSortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLogsResponse]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "logs",
            method="POST",
            json={
                "type": type,
                "startDate": start_date,
                "endDate": end_date,
                "attributes": attributes,
                "message": message,
                "pageSize": page_size,
                "pageIndex": page_index,
                "sortDirection": sort_direction,
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
                    PostLogsResponse,
                    parse_obj_as(
                        type_=PostLogsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def returns_logs_attributes(
        self,
        *,
        name: typing.Optional[str] = None,
        existing_attributes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Returns logs attributes. For users with the Standard Registry role only.

        Parameters
        ----------
        name : typing.Optional[str]
            Part of name.

        existing_attributes : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Attributes to exclude.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Successful operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "logs/attributes",
            method="GET",
            params={
                "name": name,
                "existingAttributes": existing_attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
