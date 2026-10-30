

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import encode_path_param
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...core.serialization import convert_and_respect_annotation_metadata
from ...errors.bad_request_error import BadRequestError
from ...errors.content_too_large_error import ContentTooLargeError
from ...errors.gone_error import GoneError
from ...errors.not_found_error import NotFoundError
from ...errors.service_unavailable_error import ServiceUnavailableError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.error_response import ErrorResponse
from ...types.run_maintenance_request import RunMaintenanceRequest
from ...types.run_maintenance_response import RunMaintenanceResponse
from ...types.service_unavailable_error_body import ServiceUnavailableErrorBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        namespace_id: str,
        *,
        request: RunMaintenanceRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunMaintenanceResponse]:
        """
        Runs one maintenance job for the namespace. The body's `kind` selects the job, which is one of `metadata`, `gc`, `retention`, `retention_window`, or `recover_administrator`. The response includes the same `kind` and the job's result. A deleted namespace accepts only `gc`. A `metadata` job folds the WAL tail and compacts metadata until nothing is due, or until it publishes 16 compaction units. A compaction unit can take minutes, so the call can too. When the result's `outcome` is `due`, another `metadata` run continues the work. A `gc` job reads the current manifest, lists the pins, and then sweeps every object family to the end. Each listing starts at the beginning, and the job doesn't keep a position to continue from. When the deployment maintains a grep index, the job then deletes aged, unreferenced grep index objects, and the result includes their counts in `extensions.grep`. A `retention` job advances the retention floor to the folded manifest head, or to the one target that `to_seq` or `cutoff_at_ms` sets. A `retention_window` job sets the namespace's retention window to `retention_window_ms`, or clears it when the body doesn't include that field.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request : RunMaintenanceRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunMaintenanceResponse]
            Maintenance job completed
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = self._client_wrapper.httpx_client.request(
            f"v0/maintenance/namespaces/{encode_path_param(namespace_id)}/runs",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=RunMaintenanceRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=_request_options_with_retries_disabled,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunMaintenanceResponse,
                    parse_obj_as(
                        type_=RunMaintenanceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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


class AsyncRawRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        namespace_id: str,
        *,
        request: RunMaintenanceRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunMaintenanceResponse]:
        """
        Runs one maintenance job for the namespace. The body's `kind` selects the job, which is one of `metadata`, `gc`, `retention`, `retention_window`, or `recover_administrator`. The response includes the same `kind` and the job's result. A deleted namespace accepts only `gc`. A `metadata` job folds the WAL tail and compacts metadata until nothing is due, or until it publishes 16 compaction units. A compaction unit can take minutes, so the call can too. When the result's `outcome` is `due`, another `metadata` run continues the work. A `gc` job reads the current manifest, lists the pins, and then sweeps every object family to the end. Each listing starts at the beginning, and the job doesn't keep a position to continue from. When the deployment maintains a grep index, the job then deletes aged, unreferenced grep index objects, and the result includes their counts in `extensions.grep`. A `retention` job advances the retention floor to the folded manifest head, or to the one target that `to_seq` or `cutoff_at_ms` sets. A `retention_window` job sets the namespace's retention window to `retention_window_ms`, or clears it when the body doesn't include that field.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request : RunMaintenanceRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunMaintenanceResponse]
            Maintenance job completed
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/maintenance/namespaces/{encode_path_param(namespace_id)}/runs",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=RunMaintenanceRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=_request_options_with_retries_disabled,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunMaintenanceResponse,
                    parse_obj_as(
                        type_=RunMaintenanceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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
