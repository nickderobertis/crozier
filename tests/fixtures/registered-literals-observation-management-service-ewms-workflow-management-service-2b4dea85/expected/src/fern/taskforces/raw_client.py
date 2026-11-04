

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
from ..errors.not_found_error import NotFoundError
from ..types.error_response import ErrorResponse
from ..types.taskforce_object import TaskforceObject
from .types.post_v1query_taskforces_response import PostV1QueryTaskforcesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTaskforcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_v1query_taskforces(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1QueryTaskforcesResponse]:
        """
        Queries and returns a list of taskforce objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        query : typing.Dict[str, typing.Any]
            The search criteria (MongoDB-filter syntax)

        projection : typing.Optional[typing.Sequence[str]]
            The fields to include in the response

        after : typing.Optional[str]
            The database '_id' to resume pagination from, taken from a previous response's 'next_after' field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1QueryTaskforcesResponse]
            Matching taskforces and pagination metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/query/taskforces",
            method="POST",
            json={
                "query": query,
                "projection": projection,
                "after": after,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV1QueryTaskforcesResponse,
                    parse_obj_as(
                        type_=PostV1QueryTaskforcesResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_v1taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TaskforceObject]:
        """
        Retrieves the taskforce object that matches the specified taskforce UUID. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskforceObject]
            The matching taskforce object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/taskforces/{encode_path_param(taskforce_uuid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskforceObject,
                    parse_obj_as(
                        type_=TaskforceObject,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTaskforcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_v1query_taskforces(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1QueryTaskforcesResponse]:
        """
        Queries and returns a list of taskforce objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        query : typing.Dict[str, typing.Any]
            The search criteria (MongoDB-filter syntax)

        projection : typing.Optional[typing.Sequence[str]]
            The fields to include in the response

        after : typing.Optional[str]
            The database '_id' to resume pagination from, taken from a previous response's 'next_after' field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1QueryTaskforcesResponse]
            Matching taskforces and pagination metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/query/taskforces",
            method="POST",
            json={
                "query": query,
                "projection": projection,
                "after": after,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV1QueryTaskforcesResponse,
                    parse_obj_as(
                        type_=PostV1QueryTaskforcesResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_v1taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TaskforceObject]:
        """
        Retrieves the taskforce object that matches the specified taskforce UUID. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskforceObject]
            The matching taskforce object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/taskforces/{encode_path_param(taskforce_uuid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskforceObject,
                    parse_obj_as(
                        type_=TaskforceObject,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
