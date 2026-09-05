

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.api_error_model import ApiErrorModel
from ..types.http_validation_error import HttpValidationError
from ..types.v1alpha1metrics import V1Alpha1Metrics
from ..types.v1alpha1system_status import V1Alpha1SystemStatus
from pydantic import ValidationError


class RawHealthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def status(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[V1Alpha1SystemStatus]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1SystemStatus]
            System info
        """
        _response = self._client_wrapper.httpx_client.request(
            "status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1SystemStatus,
                    parse_obj_as(
                        type_=V1Alpha1SystemStatus,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def metrics(
        self,
        *,
        name: typing.Optional[str] = None,
        start_time: typing.Optional[dt.datetime] = None,
        end_time: typing.Optional[dt.datetime] = None,
        max_length: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Alpha1Metrics]:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        start_time : typing.Optional[dt.datetime]

        end_time : typing.Optional[dt.datetime]

        max_length : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1Metrics]
            System metrics
        """
        _response = self._client_wrapper.httpx_client.request(
            "metrics",
            method="GET",
            params={
                "name": name,
                "start_time": serialize_datetime(start_time) if start_time is not None else None,
                "end_time": serialize_datetime(end_time) if end_time is not None else None,
                "max_length": max_length,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1Metrics,
                    parse_obj_as(
                        type_=V1Alpha1Metrics,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawHealthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Alpha1SystemStatus]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1SystemStatus]
            System info
        """
        _response = await self._client_wrapper.httpx_client.request(
            "status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1SystemStatus,
                    parse_obj_as(
                        type_=V1Alpha1SystemStatus,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def metrics(
        self,
        *,
        name: typing.Optional[str] = None,
        start_time: typing.Optional[dt.datetime] = None,
        end_time: typing.Optional[dt.datetime] = None,
        max_length: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Alpha1Metrics]:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        start_time : typing.Optional[dt.datetime]

        end_time : typing.Optional[dt.datetime]

        max_length : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1Metrics]
            System metrics
        """
        _response = await self._client_wrapper.httpx_client.request(
            "metrics",
            method="GET",
            params={
                "name": name,
                "start_time": serialize_datetime(start_time) if start_time is not None else None,
                "end_time": serialize_datetime(end_time) if end_time is not None else None,
                "max_length": max_length,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1Metrics,
                    parse_obj_as(
                        type_=V1Alpha1Metrics,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
