

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
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.not_implemented_error import NotImplementedError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.apis_v1components_error_response import ApisV1ComponentsErrorResponse
from ..types.apis_v1components_observation_scope import ApisV1ComponentsObservationScope
from ..types.operation_kind import OperationKind
from ..types.operation_response import OperationResponse
from .types.start_operation_request_spec import StartOperationRequestSpec
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def start_operation(
        self,
        *,
        duration_seconds: int,
        kind: OperationKind,
        request_id: str,
        scope: ApisV1ComponentsObservationScope,
        spec: StartOperationRequestSpec,
        container_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OperationResponse]:
        """
        Parameters
        ----------
        duration_seconds : int

        kind : OperationKind

        request_id : str

        scope : ApisV1ComponentsObservationScope

        spec : StartOperationRequestSpec

        container_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OperationResponse]
            Existing idempotent Operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/operations",
            method="POST",
            json={
                "container_id": container_id,
                "duration_seconds": duration_seconds,
                "kind": kind,
                "request_id": request_id,
                "scope": scope,
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=StartOperationRequestSpec, direction="write"
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
                    OperationResponse,
                    parse_obj_as(
                        type_=OperationResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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
            if _response.status_code == 501:
                raise NotImplementedError(
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

    def get_operation(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OperationResponse]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OperationResponse]
            Operation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/operations/{encode_path_param(request_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OperationResponse,
                    parse_obj_as(
                        type_=OperationResponse,
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

    def stop_operation(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OperationResponse]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OperationResponse]
            Operation already stopping or terminal.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/operations/{encode_path_param(request_id)}/stop",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OperationResponse,
                    parse_obj_as(
                        type_=OperationResponse,
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


class AsyncRawOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def start_operation(
        self,
        *,
        duration_seconds: int,
        kind: OperationKind,
        request_id: str,
        scope: ApisV1ComponentsObservationScope,
        spec: StartOperationRequestSpec,
        container_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OperationResponse]:
        """
        Parameters
        ----------
        duration_seconds : int

        kind : OperationKind

        request_id : str

        scope : ApisV1ComponentsObservationScope

        spec : StartOperationRequestSpec

        container_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OperationResponse]
            Existing idempotent Operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/operations",
            method="POST",
            json={
                "container_id": container_id,
                "duration_seconds": duration_seconds,
                "kind": kind,
                "request_id": request_id,
                "scope": scope,
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=StartOperationRequestSpec, direction="write"
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
                    OperationResponse,
                    parse_obj_as(
                        type_=OperationResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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
            if _response.status_code == 501:
                raise NotImplementedError(
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

    async def get_operation(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OperationResponse]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OperationResponse]
            Operation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/operations/{encode_path_param(request_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OperationResponse,
                    parse_obj_as(
                        type_=OperationResponse,
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

    async def stop_operation(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OperationResponse]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OperationResponse]
            Operation already stopping or terminal.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/operations/{encode_path_param(request_id)}/stop",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OperationResponse,
                    parse_obj_as(
                        type_=OperationResponse,
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
