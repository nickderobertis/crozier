

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import jsonable_encoder
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.content_too_large_error import ContentTooLargeError
from .errors.internal_server_error import InternalServerError
from .errors.not_acceptable_error import NotAcceptableError
from .errors.unauthorized_error import UnauthorizedError
from .types.bulk_mapping_job import BulkMappingJob
from .types.bulk_mapping_job_result import BulkMappingJobResult
from .types.get_mapping_values_key_request_key import GetMappingValuesKeyRequestKey
from .types.get_mapping_values_key_response import GetMappingValuesKeyResponse


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_mapping(
        self, *, request: BulkMappingJob, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BulkMappingJobResult]:
        """
        Allows mapping from third-party identifiers to FIGIs.

        Parameters
        ----------
        request : BulkMappingJob

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkMappingJobResult]
            A list of FIGIs and their metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            "mapping",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=BulkMappingJob, direction="write"),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkMappingJobResult,
                    parse_obj_as(
                        type_=BulkMappingJobResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_mapping_values_key(
        self, key: GetMappingValuesKeyRequestKey, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMappingValuesKeyResponse]:
        """
        Get values for enum-like fields.

        Parameters
        ----------
        key : GetMappingValuesKeyRequestKey
            Key of MappingJob for which to get possible values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMappingValuesKeyResponse]
            The list of values.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mapping/values/{jsonable_encoder(key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMappingValuesKeyResponse,
                    parse_obj_as(
                        type_=GetMappingValuesKeyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_mapping(
        self, *, request: BulkMappingJob, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BulkMappingJobResult]:
        """
        Allows mapping from third-party identifiers to FIGIs.

        Parameters
        ----------
        request : BulkMappingJob

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkMappingJobResult]
            A list of FIGIs and their metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mapping",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=BulkMappingJob, direction="write"),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkMappingJobResult,
                    parse_obj_as(
                        type_=BulkMappingJobResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_mapping_values_key(
        self, key: GetMappingValuesKeyRequestKey, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMappingValuesKeyResponse]:
        """
        Get values for enum-like fields.

        Parameters
        ----------
        key : GetMappingValuesKeyRequestKey
            Key of MappingJob for which to get possible values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMappingValuesKeyResponse]
            The list of values.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mapping/values/{jsonable_encoder(key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMappingValuesKeyResponse,
                    parse_obj_as(
                        type_=GetMappingValuesKeyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
