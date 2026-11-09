

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.app_id import AppId
from ..types.metric_name import MetricName
from ..types.metrics_response import MetricsResponse
from ..types.metrics_step import MetricsStep
from ..types.process_id import ProcessId
from pydantic import ValidationError


class RawMetricsV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_metrics(
        self,
        app_id: AppId,
        process_id: ProcessId,
        *,
        metrics: typing.Optional[typing.Union[MetricName, typing.Sequence[MetricName]]] = None,
        end: typing.Optional[float] = None,
        start: typing.Optional[float] = None,
        step: typing.Optional[MetricsStep] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MetricsResponse]:
        """
        Get metrics for a [process](https://hathora.dev/docs/concepts/hathora-entities#process) using `appId` and `processId`.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        metrics : typing.Optional[typing.Union[MetricName, typing.Sequence[MetricName]]]
            Available metrics to query over time.

        end : typing.Optional[float]
            Unix timestamp. Default is current time.

        start : typing.Optional[float]
            Unix timestamp. Default is -1 hour from `end`.

        step : typing.Optional[MetricsStep]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MetricsResponse]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"metrics/v1/{encode_path_param(app_id)}/process/{encode_path_param(process_id)}",
            method="GET",
            params={
                "metrics": metrics,
                "end": end,
                "start": start,
                "step": step,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetricsResponse,
                    parse_obj_as(
                        type_=MetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )


class AsyncRawMetricsV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_metrics(
        self,
        app_id: AppId,
        process_id: ProcessId,
        *,
        metrics: typing.Optional[typing.Union[MetricName, typing.Sequence[MetricName]]] = None,
        end: typing.Optional[float] = None,
        start: typing.Optional[float] = None,
        step: typing.Optional[MetricsStep] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MetricsResponse]:
        """
        Get metrics for a [process](https://hathora.dev/docs/concepts/hathora-entities#process) using `appId` and `processId`.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        metrics : typing.Optional[typing.Union[MetricName, typing.Sequence[MetricName]]]
            Available metrics to query over time.

        end : typing.Optional[float]
            Unix timestamp. Default is current time.

        start : typing.Optional[float]
            Unix timestamp. Default is -1 hour from `end`.

        step : typing.Optional[MetricsStep]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MetricsResponse]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"metrics/v1/{encode_path_param(app_id)}/process/{encode_path_param(process_id)}",
            method="GET",
            params={
                "metrics": metrics,
                "end": end,
                "start": start,
                "step": step,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetricsResponse,
                    parse_obj_as(
                        type_=MetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )
