

import datetime as dt
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
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.cursor import Cursor
from ..types.error_envelope import ErrorEnvelope
from ..types.file_entry import FileEntry
from ..types.file_hash import FileHash
from ..types.job import Job
from ..types.name_conflict_policy import NameConflictPolicy
from ..types.upload_daily_statistics import UploadDailyStatistics
from ..types.upload_import_source import UploadImportSource
from ..types.upload_part import UploadPart
from ..types.upload_session import UploadSession
from ..types.upload_state import UploadState
from ..types.uuid_ import Uuid
from .types.list_upload_parts_response import ListUploadPartsResponse
from .types.list_uploads_response import ListUploadsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUploadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_uploads(
        self,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        state: typing.Optional[UploadState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListUploadsResponse]:
        """
        List resumable upload sessions owned by the authenticated user.

        Parameters
        ----------
        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        state : typing.Optional[UploadState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListUploadsResponse]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/uploads",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "state": state,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUploadsResponse,
                    parse_obj_as(
                        type_=ListUploadsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def create_upload(
        self,
        *,
        idempotency_key: Uuid,
        name: str,
        size: int,
        mod_time: dt.datetime,
        parent_id: typing.Optional[Uuid] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        hash: typing.Optional[FileHash] = OMIT,
        encryption: typing.Optional[bool] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        preferred_part_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UploadSession]:
        """
        Create a durable upload session.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        name : str

        size : int
            Expected size in bytes, or -1 when the size is unknown until completion.

        mod_time : dt.datetime

        parent_id : typing.Optional[Uuid]

        mime_type : typing.Optional[str]

        hash : typing.Optional[FileHash]

        encryption : typing.Optional[bool]

        conflict_policy : typing.Optional[NameConflictPolicy]

        preferred_part_size : typing.Optional[int]
            Optional preferred part size. The server may choose a different value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadSession]
            The request has succeeded and a new resource has been created as a result.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/uploads",
            method="POST",
            json={
                "parentId": parent_id,
                "name": name,
                "size": size,
                "mimeType": mime_type,
                "modTime": mod_time,
                "hash": convert_and_respect_annotation_metadata(object_=hash, annotation=FileHash, direction="write"),
                "encryption": encryption,
                "conflictPolicy": conflict_policy,
                "preferredPartSize": preferred_part_size,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def get_upload_statistics(
        self, *, days: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[UploadDailyStatistics]]:
        """
        Return completed upload volume grouped by UTC day.

        Parameters
        ----------
        days : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[UploadDailyStatistics]]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/uploads/statistics",
            method="GET",
            params={
                "days": days,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UploadDailyStatistics],
                    parse_obj_as(
                        type_=typing.List[UploadDailyStatistics],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def create_upload_import(
        self,
        *,
        destination: str,
        sources: typing.Sequence[UploadImportSource],
        headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        exclude: typing.Optional[typing.Sequence[str]] = OMIT,
        min_size: typing.Optional[str] = OMIT,
        max_size: typing.Optional[str] = OMIT,
        part_concurrency: typing.Optional[int] = OMIT,
        chunk_size: typing.Optional[int] = OMIT,
        encryption: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Job]:
        """
        Queue local paths, recursive folders, and HTTP URLs for server-side upload.

        Parameters
        ----------
        destination : str
            Destination folder UUID or absolute drive path from root.

        sources : typing.Sequence[UploadImportSource]

        headers : typing.Optional[typing.Dict[str, str]]

        exclude : typing.Optional[typing.Sequence[str]]

        min_size : typing.Optional[str]

        max_size : typing.Optional[str]

        part_concurrency : typing.Optional[int]

        chunk_size : typing.Optional[int]
            Preferred upload part size. Values are aligned to the nearest 16 MiB.

        encryption : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Job]
            The request has been accepted for processing, but processing has not yet completed.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/uploads/imports",
            method="POST",
            json={
                "destination": destination,
                "sources": convert_and_respect_annotation_metadata(
                    object_=sources, annotation=typing.Sequence[UploadImportSource], direction="write"
                ),
                "headers": headers,
                "exclude": exclude,
                "minSize": min_size,
                "maxSize": max_size,
                "partConcurrency": part_concurrency,
                "chunkSize": chunk_size,
                "encryption": encryption,
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
                    Job,
                    parse_obj_as(
                        type_=Job,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def get_upload(
        self, upload_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UploadSession]:
        """
        Inspect an upload for resume and conflict handling.

        Parameters
        ----------
        upload_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadSession]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/uploads/{encode_path_param(upload_id)}",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def abort_upload(
        self, upload_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Abort an upload and schedule physical Telegram cleanup.

        Parameters
        ----------
        upload_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/uploads/{encode_path_param(upload_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def list_upload_parts(
        self,
        upload_id: Uuid,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListUploadPartsResponse]:
        """
        List parts already known to the upload session.

        Parameters
        ----------
        upload_id : Uuid

        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListUploadPartsResponse]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/uploads/{encode_path_param(upload_id)}/parts",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUploadPartsResponse,
                    parse_obj_as(
                        type_=ListUploadPartsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def put_upload_part(
        self,
        upload_id: Uuid,
        part_no: int,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UploadPart]:
        """
        Upload one part. The `(uploadId, partNo)` pair is the idempotency key.
        An exact retry returns the existing stored part; conflicting size/checksum returns 409.

        Parameters
        ----------
        upload_id : Uuid

        part_no : int

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadPart]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/uploads/{encode_path_param(upload_id)}/parts/{encode_path_param(part_no)}",
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
                    UploadPart,
                    parse_obj_as(
                        type_=UploadPart,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def complete_upload(
        self, upload_id: Uuid, *, idempotency_key: Uuid, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileEntry]:
        """
        Validate all parts and transactionally publish the file. A successful response
        guarantees immediate read-after-write visibility.

        Parameters
        ----------
        upload_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileEntry]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/uploads/{encode_path_param(upload_id)}/complete",
            method="POST",
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def list_uploads(
        self,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        state: typing.Optional[UploadState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListUploadsResponse]:
        """
        List resumable upload sessions owned by the authenticated user.

        Parameters
        ----------
        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        state : typing.Optional[UploadState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListUploadsResponse]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/uploads",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "state": state,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUploadsResponse,
                    parse_obj_as(
                        type_=ListUploadsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def create_upload(
        self,
        *,
        idempotency_key: Uuid,
        name: str,
        size: int,
        mod_time: dt.datetime,
        parent_id: typing.Optional[Uuid] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        hash: typing.Optional[FileHash] = OMIT,
        encryption: typing.Optional[bool] = OMIT,
        conflict_policy: typing.Optional[NameConflictPolicy] = OMIT,
        preferred_part_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UploadSession]:
        """
        Create a durable upload session.

        Parameters
        ----------
        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        name : str

        size : int
            Expected size in bytes, or -1 when the size is unknown until completion.

        mod_time : dt.datetime

        parent_id : typing.Optional[Uuid]

        mime_type : typing.Optional[str]

        hash : typing.Optional[FileHash]

        encryption : typing.Optional[bool]

        conflict_policy : typing.Optional[NameConflictPolicy]

        preferred_part_size : typing.Optional[int]
            Optional preferred part size. The server may choose a different value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadSession]
            The request has succeeded and a new resource has been created as a result.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/uploads",
            method="POST",
            json={
                "parentId": parent_id,
                "name": name,
                "size": size,
                "mimeType": mime_type,
                "modTime": mod_time,
                "hash": convert_and_respect_annotation_metadata(object_=hash, annotation=FileHash, direction="write"),
                "encryption": encryption,
                "conflictPolicy": conflict_policy,
                "preferredPartSize": preferred_part_size,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def get_upload_statistics(
        self, *, days: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[UploadDailyStatistics]]:
        """
        Return completed upload volume grouped by UTC day.

        Parameters
        ----------
        days : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[UploadDailyStatistics]]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/uploads/statistics",
            method="GET",
            params={
                "days": days,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UploadDailyStatistics],
                    parse_obj_as(
                        type_=typing.List[UploadDailyStatistics],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def create_upload_import(
        self,
        *,
        destination: str,
        sources: typing.Sequence[UploadImportSource],
        headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        exclude: typing.Optional[typing.Sequence[str]] = OMIT,
        min_size: typing.Optional[str] = OMIT,
        max_size: typing.Optional[str] = OMIT,
        part_concurrency: typing.Optional[int] = OMIT,
        chunk_size: typing.Optional[int] = OMIT,
        encryption: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Job]:
        """
        Queue local paths, recursive folders, and HTTP URLs for server-side upload.

        Parameters
        ----------
        destination : str
            Destination folder UUID or absolute drive path from root.

        sources : typing.Sequence[UploadImportSource]

        headers : typing.Optional[typing.Dict[str, str]]

        exclude : typing.Optional[typing.Sequence[str]]

        min_size : typing.Optional[str]

        max_size : typing.Optional[str]

        part_concurrency : typing.Optional[int]

        chunk_size : typing.Optional[int]
            Preferred upload part size. Values are aligned to the nearest 16 MiB.

        encryption : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Job]
            The request has been accepted for processing, but processing has not yet completed.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/uploads/imports",
            method="POST",
            json={
                "destination": destination,
                "sources": convert_and_respect_annotation_metadata(
                    object_=sources, annotation=typing.Sequence[UploadImportSource], direction="write"
                ),
                "headers": headers,
                "exclude": exclude,
                "minSize": min_size,
                "maxSize": max_size,
                "partConcurrency": part_concurrency,
                "chunkSize": chunk_size,
                "encryption": encryption,
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
                    Job,
                    parse_obj_as(
                        type_=Job,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def get_upload(
        self, upload_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UploadSession]:
        """
        Inspect an upload for resume and conflict handling.

        Parameters
        ----------
        upload_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadSession]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/uploads/{encode_path_param(upload_id)}",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def abort_upload(
        self, upload_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Abort an upload and schedule physical Telegram cleanup.

        Parameters
        ----------
        upload_id : Uuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/uploads/{encode_path_param(upload_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def list_upload_parts(
        self,
        upload_id: Uuid,
        *,
        cursor: typing.Optional[Cursor] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListUploadPartsResponse]:
        """
        List parts already known to the upload session.

        Parameters
        ----------
        upload_id : Uuid

        cursor : typing.Optional[Cursor]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListUploadPartsResponse]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/uploads/{encode_path_param(upload_id)}/parts",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUploadPartsResponse,
                    parse_obj_as(
                        type_=ListUploadPartsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def put_upload_part(
        self,
        upload_id: Uuid,
        part_no: int,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UploadPart]:
        """
        Upload one part. The `(uploadId, partNo)` pair is the idempotency key.
        An exact retry returns the existing stored part; conflicting size/checksum returns 409.

        Parameters
        ----------
        upload_id : Uuid

        part_no : int

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadPart]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/uploads/{encode_path_param(upload_id)}/parts/{encode_path_param(part_no)}",
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
                    UploadPart,
                    parse_obj_as(
                        type_=UploadPart,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def complete_upload(
        self, upload_id: Uuid, *, idempotency_key: Uuid, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileEntry]:
        """
        Validate all parts and transactionally publish the file. A successful response
        guarantees immediate read-after-write visibility.

        Parameters
        ----------
        upload_id : Uuid

        idempotency_key : Uuid
            Stable UUID generated by the caller for safe request retries.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileEntry]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/uploads/{encode_path_param(upload_id)}/complete",
            method="POST",
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileEntry,
                    parse_obj_as(
                        type_=FileEntry,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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
