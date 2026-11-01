

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
from ..errors.gone_error import GoneError
from ..errors.not_found_error import NotFoundError
from ..errors.not_implemented_error import NotImplementedError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.commit import Commit
from ..types.commit_id import CommitId
from ..types.commit_precondition import CommitPrecondition
from ..types.content_token import ContentToken
from ..types.error_response import ErrorResponse
from ..types.filesystem_operation import FilesystemOperation
from ..types.service_unavailable_error_body import ServiceUnavailableErrorBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCommitsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        namespace_id: str,
        *,
        commit_id: CommitId,
        operations: typing.Sequence[FilesystemOperation],
        content_tokens: typing.Optional[typing.Sequence[ContentToken]] = OMIT,
        message: typing.Optional[str] = OMIT,
        preconditions: typing.Optional[typing.Sequence[CommitPrecondition]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Commit]:
        """
        Applies one commit, which is an ordered, non-empty list of path operations that are committed together. The commit ID makes retries idempotent. The server checks the request's preconditions against the state before the commit, after it resolves any commit receipt and before it runs the operations. A failed precondition's position is reported in `details.precondition_index`. A request can contain a single operation. If an operation fails, the whole request fails, and for a request with more than one operation, `details.operation_index` reports the failed operation's position.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        commit_id : CommitId
            The caller's idempotency key for the whole request.

        operations : typing.Sequence[FilesystemOperation]
            The operations to commit atomically, in order. The list can't be empty.

        content_tokens : typing.Optional[typing.Sequence[ContentToken]]
            One content token for each uploaded `content_ref` that the request uses.

        message : typing.Optional[str]
            An annotation from the caller. The message is part of the commit's identity.

        preconditions : typing.Optional[typing.Sequence[CommitPrecondition]]
            The conditions that the server checks, in order, before it runs any operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Commit]
            Commit applied
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/commits",
            method="POST",
            json={
                "commit_id": commit_id,
                "content_tokens": convert_and_respect_annotation_metadata(
                    object_=content_tokens, annotation=typing.Sequence[ContentToken], direction="write"
                ),
                "message": message,
                "operations": convert_and_respect_annotation_metadata(
                    object_=operations, annotation=typing.Sequence[FilesystemOperation], direction="write"
                ),
                "preconditions": convert_and_respect_annotation_metadata(
                    object_=preconditions, annotation=typing.Sequence[CommitPrecondition], direction="write"
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
                    Commit,
                    parse_obj_as(
                        type_=Commit,
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
            if _response.status_code == 409:
                raise ConflictError(
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
            if _response.status_code == 501:
                raise NotImplementedError(
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


class AsyncRawCommitsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        namespace_id: str,
        *,
        commit_id: CommitId,
        operations: typing.Sequence[FilesystemOperation],
        content_tokens: typing.Optional[typing.Sequence[ContentToken]] = OMIT,
        message: typing.Optional[str] = OMIT,
        preconditions: typing.Optional[typing.Sequence[CommitPrecondition]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Commit]:
        """
        Applies one commit, which is an ordered, non-empty list of path operations that are committed together. The commit ID makes retries idempotent. The server checks the request's preconditions against the state before the commit, after it resolves any commit receipt and before it runs the operations. A failed precondition's position is reported in `details.precondition_index`. A request can contain a single operation. If an operation fails, the whole request fails, and for a request with more than one operation, `details.operation_index` reports the failed operation's position.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        commit_id : CommitId
            The caller's idempotency key for the whole request.

        operations : typing.Sequence[FilesystemOperation]
            The operations to commit atomically, in order. The list can't be empty.

        content_tokens : typing.Optional[typing.Sequence[ContentToken]]
            One content token for each uploaded `content_ref` that the request uses.

        message : typing.Optional[str]
            An annotation from the caller. The message is part of the commit's identity.

        preconditions : typing.Optional[typing.Sequence[CommitPrecondition]]
            The conditions that the server checks, in order, before it runs any operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Commit]
            Commit applied
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/commits",
            method="POST",
            json={
                "commit_id": commit_id,
                "content_tokens": convert_and_respect_annotation_metadata(
                    object_=content_tokens, annotation=typing.Sequence[ContentToken], direction="write"
                ),
                "message": message,
                "operations": convert_and_respect_annotation_metadata(
                    object_=operations, annotation=typing.Sequence[FilesystemOperation], direction="write"
                ),
                "preconditions": convert_and_respect_annotation_metadata(
                    object_=preconditions, annotation=typing.Sequence[CommitPrecondition], direction="write"
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
                    Commit,
                    parse_obj_as(
                        type_=Commit,
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
            if _response.status_code == 409:
                raise ConflictError(
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
            if _response.status_code == 501:
                raise NotImplementedError(
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
