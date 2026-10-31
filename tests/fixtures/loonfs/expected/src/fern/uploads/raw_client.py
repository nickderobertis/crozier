

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
from ..types.complete_upload_body import CompleteUploadBody
from ..types.create_upload_body import CreateUploadBody
from ..types.error_response import ErrorResponse
from ..types.service_unavailable_error_body import ServiceUnavailableErrorBody
from ..types.sign_upload_parts_response import SignUploadPartsResponse
from ..types.upload_part_checksum_claim import UploadPartChecksumClaim
from ..types.upload_session import UploadSession
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUploadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self, namespace_id: str, *, request: CreateUploadBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UploadSession]:
        """
        Starts an upload session for content that a later commit can reference. A service-proxied upload sends the bytes through the server, and a direct PUT upload returns a presigned upload capability.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request : CreateUploadBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadSession]
            Upload session started
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateUploadBody, direction="write"
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
                    UploadSession,
                    parse_obj_as(
                        type_=UploadSession,
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

    def retrieve(
        self, namespace_id: str, upload_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UploadSession]:
        """
        Returns an upload session. An open `direct_put` session includes a newly signed upload capability. A completed session includes a new content token, so the client can retry the commit without uploading the content again.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadSession]
            Upload session state
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads/{encode_path_param(upload_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadSession,
                    parse_obj_as(
                        type_=UploadSession,
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

    def abort(
        self, namespace_id: str, upload_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UploadSession]:
        """
        Aborts an open upload session and deletes the object that the session was writing. Repeating the request succeeds, but a completed session can't be aborted.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadSession]
            Upload aborted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads/{encode_path_param(upload_id)}/abort",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadSession,
                    parse_obj_as(
                        type_=UploadSession,
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

    def complete(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        request: CompleteUploadBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UploadSession]:
        """
        Completes an upload. The request mode must match the mode that started the session. A direct upload includes a content claim, and a multipart upload also includes the completed parts.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request : CompleteUploadBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadSession]
            Upload completed
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads/{encode_path_param(upload_id)}/complete",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CompleteUploadBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadSession,
                    parse_obj_as(
                        type_=UploadSession,
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

    def put_content(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UploadSession]:
        """
        Uploads bytes into a service-proxied upload session and returns the open session with the staged content reference.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadSession]
            Open session with the staged content reference
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads/{encode_path_param(upload_id)}/content",
            method="PUT",
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadSession,
                    parse_obj_as(
                        type_=UploadSession,
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

    def sign_parts(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        parts: typing.Sequence[UploadPartChecksumClaim],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SignUploadPartsResponse]:
        """
        Returns one short-lived upload capability for each requested part of an open `direct_multipart` session. Each capability is bound to the part's checksum. To retry a part, a client asks for its capability again.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        parts : typing.Sequence[UploadPartChecksumClaim]
            The parts to authorize. A repeated part number replaces the earlier upload of that part.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SignUploadPartsResponse]
            Part capabilities issued
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads/{encode_path_param(upload_id)}/parts",
            method="POST",
            json={
                "parts": convert_and_respect_annotation_metadata(
                    object_=parts, annotation=typing.Sequence[UploadPartChecksumClaim], direction="write"
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
                    SignUploadPartsResponse,
                    parse_obj_as(
                        type_=SignUploadPartsResponse,
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


class AsyncRawUploadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self, namespace_id: str, *, request: CreateUploadBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UploadSession]:
        """
        Starts an upload session for content that a later commit can reference. A service-proxied upload sends the bytes through the server, and a direct PUT upload returns a presigned upload capability.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request : CreateUploadBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadSession]
            Upload session started
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**request_options, "max_retries": 0} if request_options is not None else {"max_retries": 0}
        )
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateUploadBody, direction="write"
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
                    UploadSession,
                    parse_obj_as(
                        type_=UploadSession,
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

    async def retrieve(
        self, namespace_id: str, upload_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UploadSession]:
        """
        Returns an upload session. An open `direct_put` session includes a newly signed upload capability. A completed session includes a new content token, so the client can retry the commit without uploading the content again.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadSession]
            Upload session state
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads/{encode_path_param(upload_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadSession,
                    parse_obj_as(
                        type_=UploadSession,
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

    async def abort(
        self, namespace_id: str, upload_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UploadSession]:
        """
        Aborts an open upload session and deletes the object that the session was writing. Repeating the request succeeds, but a completed session can't be aborted.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadSession]
            Upload aborted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads/{encode_path_param(upload_id)}/abort",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadSession,
                    parse_obj_as(
                        type_=UploadSession,
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

    async def complete(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        request: CompleteUploadBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UploadSession]:
        """
        Completes an upload. The request mode must match the mode that started the session. A direct upload includes a content claim, and a multipart upload also includes the completed parts.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request : CompleteUploadBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadSession]
            Upload completed
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads/{encode_path_param(upload_id)}/complete",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CompleteUploadBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadSession,
                    parse_obj_as(
                        type_=UploadSession,
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

    async def put_content(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UploadSession]:
        """
        Uploads bytes into a service-proxied upload session and returns the open session with the staged content reference.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadSession]
            Open session with the staged content reference
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads/{encode_path_param(upload_id)}/content",
            method="PUT",
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadSession,
                    parse_obj_as(
                        type_=UploadSession,
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

    async def sign_parts(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        parts: typing.Sequence[UploadPartChecksumClaim],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SignUploadPartsResponse]:
        """
        Returns one short-lived upload capability for each requested part of an open `direct_multipart` session. Each capability is bound to the part's checksum. To retry a part, a client asks for its capability again.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        parts : typing.Sequence[UploadPartChecksumClaim]
            The parts to authorize. A repeated part number replaces the earlier upload of that part.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SignUploadPartsResponse]
            Part capabilities issued
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/uploads/{encode_path_param(upload_id)}/parts",
            method="POST",
            json={
                "parts": convert_and_respect_annotation_metadata(
                    object_=parts, annotation=typing.Sequence[UploadPartChecksumClaim], direction="write"
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
                    SignUploadPartsResponse,
                    parse_obj_as(
                        type_=SignUploadPartsResponse,
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
