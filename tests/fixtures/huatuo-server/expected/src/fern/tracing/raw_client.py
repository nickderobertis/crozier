

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.apis_v1components_error_response import ApisV1ComponentsErrorResponse
from ..types.apis_v1components_observation_scope import ApisV1ComponentsObservationScope
from ..types.tracing_capabilities_response import TracingCapabilitiesResponse
from ..types.tracing_job_list_response import TracingJobListResponse
from ..types.tracing_job_response import TracingJobResponse
from ..types.tracing_type import TracingType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTracingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_tracing_jobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TracingJobListResponse]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TracingJobListResponse]
            Tracing Jobs.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tracing",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TracingJobListResponse,
                    parse_obj_as(
                        type_=TracingJobListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
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

    def create_tracing_job(
        self,
        *,
        duration_seconds: int,
        hostname: str,
        scope: ApisV1ComponentsObservationScope,
        type: TracingType,
        container_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TracingJobResponse]:
        """
        Parameters
        ----------
        duration_seconds : int

        hostname : str

        scope : ApisV1ComponentsObservationScope

        type : TracingType

        container_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TracingJobResponse]
            Tracing Job created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tracing",
            method="POST",
            json={
                "container_id": container_id,
                "duration_seconds": duration_seconds,
                "hostname": hostname,
                "scope": scope,
                "type": type,
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
                    TracingJobResponse,
                    parse_obj_as(
                        type_=TracingJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
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

    def get_tracing_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TracingCapabilitiesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TracingCapabilitiesResponse]
            Static tracing capabilities.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tracing/capabilities",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TracingCapabilitiesResponse,
                    parse_obj_as(
                        type_=TracingCapabilitiesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
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

    def get_tracing_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TracingJobResponse]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TracingJobResponse]
            Tracing Job.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tracing/{encode_path_param(request_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TracingJobResponse,
                    parse_obj_as(
                        type_=TracingJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
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

    def stop_tracing_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TracingJobResponse]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TracingJobResponse]
            Current Tracing Job after applying the stop intent.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tracing/{encode_path_param(request_id)}/stop",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TracingJobResponse,
                    parse_obj_as(
                        type_=TracingJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
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


class AsyncRawTracingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_tracing_jobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TracingJobListResponse]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TracingJobListResponse]
            Tracing Jobs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tracing",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TracingJobListResponse,
                    parse_obj_as(
                        type_=TracingJobListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
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

    async def create_tracing_job(
        self,
        *,
        duration_seconds: int,
        hostname: str,
        scope: ApisV1ComponentsObservationScope,
        type: TracingType,
        container_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TracingJobResponse]:
        """
        Parameters
        ----------
        duration_seconds : int

        hostname : str

        scope : ApisV1ComponentsObservationScope

        type : TracingType

        container_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TracingJobResponse]
            Tracing Job created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tracing",
            method="POST",
            json={
                "container_id": container_id,
                "duration_seconds": duration_seconds,
                "hostname": hostname,
                "scope": scope,
                "type": type,
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
                    TracingJobResponse,
                    parse_obj_as(
                        type_=TracingJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
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

    async def get_tracing_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TracingCapabilitiesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TracingCapabilitiesResponse]
            Static tracing capabilities.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tracing/capabilities",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TracingCapabilitiesResponse,
                    parse_obj_as(
                        type_=TracingCapabilitiesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
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

    async def get_tracing_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TracingJobResponse]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TracingJobResponse]
            Tracing Job.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tracing/{encode_path_param(request_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TracingJobResponse,
                    parse_obj_as(
                        type_=TracingJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
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

    async def stop_tracing_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TracingJobResponse]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TracingJobResponse]
            Current Tracing Job after applying the stop intent.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tracing/{encode_path_param(request_id)}/stop",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TracingJobResponse,
                    parse_obj_as(
                        type_=TracingJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApisV1ComponentsErrorResponse,
                        parse_obj_as(
                            type_=ApisV1ComponentsErrorResponse,
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
