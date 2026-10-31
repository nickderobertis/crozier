

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
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.change_seq import ChangeSeq
from ..types.delete_namespace_response import DeleteNamespaceResponse
from ..types.error_response import ErrorResponse
from ..types.namespace_access import NamespaceAccess
from ..types.namespace_id import NamespaceId
from ..types.namespace_metadata import NamespaceMetadata
from ..types.pin_id import PinId
from ..types.service_unavailable_error_body import ServiceUnavailableErrorBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNamespacesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        namespace_id: NamespaceId,
        access: typing.Optional[NamespaceAccess] = OMIT,
        retention_window_ms: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NamespaceMetadata]:
        """
        Creates a new empty namespace.

        Parameters
        ----------
        namespace_id : NamespaceId
            The durable ID of the new namespace.

        access : typing.Optional[NamespaceAccess]
            The namespace's access mode, which can't be changed after the namespace is created. The
            default is unrestricted.

        retention_window_ms : typing.Optional[int]
            The namespace's retention window, in milliseconds, which must be positive. The reference
            server's maintenance sweep then uses this window for the namespace instead of the server's
            `retention_window_ms` setting. A `retention_window` maintenance run can change or clear the
            window later.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NamespaceMetadata]
            Namespace created
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = self._client_wrapper.httpx_client.request(
            "v0/namespaces",
            method="POST",
            json={
                "access": convert_and_respect_annotation_metadata(
                    object_=access, annotation=NamespaceAccess, direction="write"
                ),
                "namespace_id": namespace_id,
                "retention_window_ms": retention_window_ms,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=_request_options_with_retries_disabled,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamespaceMetadata,
                    parse_obj_as(
                        type_=NamespaceMetadata,
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

    def retrieve(
        self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NamespaceMetadata]:
        """
        Returns the current head and retention state for a namespace.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NamespaceMetadata]
            Namespace
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamespaceMetadata,
                    parse_obj_as(
                        type_=NamespaceMetadata,
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

    def delete(
        self,
        namespace_id: str,
        *,
        expected_head_seq: typing.Optional[ChangeSeq] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteNamespaceResponse]:
        """
        Marks a namespace as deleted. The namespace ID can never be used again to create or fork a namespace.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        expected_head_seq : typing.Optional[ChangeSeq]
            The head sequence that the namespace must still have for the delete to succeed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteNamespaceResponse]
            Namespace deleted
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}",
            method="DELETE",
            params={
                "expected_head_seq": expected_head_seq,
            },
            request_options=_request_options_with_retries_disabled,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteNamespaceResponse,
                    parse_obj_as(
                        type_=DeleteNamespaceResponse,
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

    def fork(
        self,
        namespace_id: str,
        *,
        new_namespace_id: NamespaceId,
        snapshot_id: typing.Optional[PinId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NamespaceMetadata]:
        """
        Creates a new namespace from the source namespace's current head or from an unexpired snapshot.

        Parameters
        ----------
        namespace_id : str
            The source namespace ID.

        new_namespace_id : NamespaceId
            The durable ID of the new namespace that the fork creates.

        snapshot_id : typing.Optional[PinId]
            An unexpired snapshot to fork from. Without it, the fork starts from the current head.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NamespaceMetadata]
            Namespace forked
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/forks",
            method="POST",
            json={
                "new_namespace_id": new_namespace_id,
                "snapshot_id": snapshot_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=_request_options_with_retries_disabled,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamespaceMetadata,
                    parse_obj_as(
                        type_=NamespaceMetadata,
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


class AsyncRawNamespacesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        namespace_id: NamespaceId,
        access: typing.Optional[NamespaceAccess] = OMIT,
        retention_window_ms: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NamespaceMetadata]:
        """
        Creates a new empty namespace.

        Parameters
        ----------
        namespace_id : NamespaceId
            The durable ID of the new namespace.

        access : typing.Optional[NamespaceAccess]
            The namespace's access mode, which can't be changed after the namespace is created. The
            default is unrestricted.

        retention_window_ms : typing.Optional[int]
            The namespace's retention window, in milliseconds, which must be positive. The reference
            server's maintenance sweep then uses this window for the namespace instead of the server's
            `retention_window_ms` setting. A `retention_window` maintenance run can change or clear the
            window later.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NamespaceMetadata]
            Namespace created
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = await self._client_wrapper.httpx_client.request(
            "v0/namespaces",
            method="POST",
            json={
                "access": convert_and_respect_annotation_metadata(
                    object_=access, annotation=NamespaceAccess, direction="write"
                ),
                "namespace_id": namespace_id,
                "retention_window_ms": retention_window_ms,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=_request_options_with_retries_disabled,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamespaceMetadata,
                    parse_obj_as(
                        type_=NamespaceMetadata,
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

    async def retrieve(
        self, namespace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NamespaceMetadata]:
        """
        Returns the current head and retention state for a namespace.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NamespaceMetadata]
            Namespace
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamespaceMetadata,
                    parse_obj_as(
                        type_=NamespaceMetadata,
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

    async def delete(
        self,
        namespace_id: str,
        *,
        expected_head_seq: typing.Optional[ChangeSeq] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteNamespaceResponse]:
        """
        Marks a namespace as deleted. The namespace ID can never be used again to create or fork a namespace.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        expected_head_seq : typing.Optional[ChangeSeq]
            The head sequence that the namespace must still have for the delete to succeed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteNamespaceResponse]
            Namespace deleted
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}",
            method="DELETE",
            params={
                "expected_head_seq": expected_head_seq,
            },
            request_options=_request_options_with_retries_disabled,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteNamespaceResponse,
                    parse_obj_as(
                        type_=DeleteNamespaceResponse,
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

    async def fork(
        self,
        namespace_id: str,
        *,
        new_namespace_id: NamespaceId,
        snapshot_id: typing.Optional[PinId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NamespaceMetadata]:
        """
        Creates a new namespace from the source namespace's current head or from an unexpired snapshot.

        Parameters
        ----------
        namespace_id : str
            The source namespace ID.

        new_namespace_id : NamespaceId
            The durable ID of the new namespace that the fork creates.

        snapshot_id : typing.Optional[PinId]
            An unexpired snapshot to fork from. Without it, the fork starts from the current head.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NamespaceMetadata]
            Namespace forked
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/forks",
            method="POST",
            json={
                "new_namespace_id": new_namespace_id,
                "snapshot_id": snapshot_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=_request_options_with_retries_disabled,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamespaceMetadata,
                    parse_obj_as(
                        type_=NamespaceMetadata,
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
