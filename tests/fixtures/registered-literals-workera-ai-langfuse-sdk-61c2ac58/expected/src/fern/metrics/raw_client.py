

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.daily_metrics import DailyMetrics
from pydantic import ValidationError


class RawMetricsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def daily(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        trace_name: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DailyMetrics]:
        """
        Get daily metrics of the Langfuse project

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        trace_name : typing.Optional[str]
            Optional filter by the name of the trace

        user_id : typing.Optional[str]
            Optional filter by the userId associated with the trace

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for metrics where traces include all of these tags

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for metrics where events include any of these environments

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces and observations on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces and observations before a certain datetime (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DailyMetrics]

        """
        _response = self._client_wrapper.httpx_client.request(
            "api/public/metrics/daily",
            method="GET",
            params={
                "page": page,
                "limit": limit,
                "traceName": trace_name,
                "userId": user_id,
                "tags": tags,
                "environment": environment,
                "fromTimestamp": serialize_datetime(from_timestamp) if from_timestamp is not None else None,
                "toTimestamp": serialize_datetime(to_timestamp) if to_timestamp is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DailyMetrics,
                    parse_obj_as(
                        type_=DailyMetrics,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
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


class AsyncRawMetricsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def daily(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        trace_name: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DailyMetrics]:
        """
        Get daily metrics of the Langfuse project

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        trace_name : typing.Optional[str]
            Optional filter by the name of the trace

        user_id : typing.Optional[str]
            Optional filter by the userId associated with the trace

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for metrics where traces include all of these tags

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for metrics where events include any of these environments

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces and observations on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces and observations before a certain datetime (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DailyMetrics]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/public/metrics/daily",
            method="GET",
            params={
                "page": page,
                "limit": limit,
                "traceName": trace_name,
                "userId": user_id,
                "tags": tags,
                "environment": environment,
                "fromTimestamp": serialize_datetime(from_timestamp) if from_timestamp is not None else None,
                "toTimestamp": serialize_datetime(to_timestamp) if to_timestamp is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DailyMetrics,
                    parse_obj_as(
                        type_=DailyMetrics,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
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
