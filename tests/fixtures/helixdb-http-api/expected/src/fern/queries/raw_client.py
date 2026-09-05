

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.request_timeout_error import RequestTimeoutError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.query_error import QueryError
from ..types.query_request import QueryRequest
from ..types.query_response import QueryResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawQueriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def execute_query(
        self,
        *,
        request: QueryRequest,
        helix_database_id: typing.Optional[str] = None,
        helix_warm: typing.Optional[bool] = None,
        helix_require_writer: typing.Optional[bool] = None,
        helix_await_durable: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[QueryResponse]]:
        """
        Executes one read or write batch. request_type must match the closed read or write variant under query. Local servers accept request bodies up to 16 MiB. Helix Cloud gateways accept request bodies up to 2 MiB.

        Parameters
        ----------
        request : QueryRequest

        helix_database_id : typing.Optional[str]
            Database identifier shown in Helix Cloud connection details. Required by the GA shared gateway, not needed by a standalone local server, and not allowed by a database-specific cluster-mode gateway. The legacy X-Helix-Tenant-Id alias is also accepted in GA mode.

        helix_warm : typing.Optional[bool]
            Warm read execution state. Valid only for read requests.

        helix_require_writer : typing.Optional[bool]
            Reject the request unless it reaches a writer-capable server.

        helix_await_durable : typing.Optional[bool]
            Flush the writer before acknowledging success. Valid only for write requests.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[QueryResponse]]
            Query executed successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/query",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=QueryRequest, direction="write"),
            headers={
                "content-type": "application/json",
                "X-Helix-Database-Id": str(helix_database_id) if helix_database_id is not None else None,
                "X-Helix-Warm": str(helix_warm) if helix_warm is not None else None,
                "X-Helix-Require-Writer": str(helix_require_writer) if helix_require_writer is not None else None,
                "X-Helix-Await-Durable": str(helix_await_durable) if helix_await_durable is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[QueryResponse],
                    parse_obj_as(
                        type_=typing.Optional[QueryResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 408:
                raise RequestTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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


class AsyncRawQueriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def execute_query(
        self,
        *,
        request: QueryRequest,
        helix_database_id: typing.Optional[str] = None,
        helix_warm: typing.Optional[bool] = None,
        helix_require_writer: typing.Optional[bool] = None,
        helix_await_durable: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[QueryResponse]]:
        """
        Executes one read or write batch. request_type must match the closed read or write variant under query. Local servers accept request bodies up to 16 MiB. Helix Cloud gateways accept request bodies up to 2 MiB.

        Parameters
        ----------
        request : QueryRequest

        helix_database_id : typing.Optional[str]
            Database identifier shown in Helix Cloud connection details. Required by the GA shared gateway, not needed by a standalone local server, and not allowed by a database-specific cluster-mode gateway. The legacy X-Helix-Tenant-Id alias is also accepted in GA mode.

        helix_warm : typing.Optional[bool]
            Warm read execution state. Valid only for read requests.

        helix_require_writer : typing.Optional[bool]
            Reject the request unless it reaches a writer-capable server.

        helix_await_durable : typing.Optional[bool]
            Flush the writer before acknowledging success. Valid only for write requests.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[QueryResponse]]
            Query executed successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/query",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=QueryRequest, direction="write"),
            headers={
                "content-type": "application/json",
                "X-Helix-Database-Id": str(helix_database_id) if helix_database_id is not None else None,
                "X-Helix-Warm": str(helix_warm) if helix_warm is not None else None,
                "X-Helix-Require-Writer": str(helix_require_writer) if helix_require_writer is not None else None,
                "X-Helix-Await-Durable": str(helix_await_durable) if helix_await_durable is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[QueryResponse],
                    parse_obj_as(
                        type_=typing.Optional[QueryResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 408:
                raise RequestTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        QueryError,
                        parse_obj_as(
                            type_=QueryError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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
