

import contextlib
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.documents_commit200response import DocumentsCommit200Response
from ..types.documents_get200response import DocumentsGet200Response
from ..types.documents_import_from200response import DocumentsImportFrom200Response
from ..types.documents_import_from502response import DocumentsImportFrom502Response
from ..types.documents_init200response import DocumentsInit200Response
from ..types.documents_list200response import DocumentsList200Response
from ..types.documents_upload_proxy200response import DocumentsUploadProxy200Response
from .types.documents_import_from_request_dedup_mode import DocumentsImportFromRequestDedupMode
from .types.documents_import_from_request_expected import DocumentsImportFromRequestExpected
from .types.documents_import_from_request_mode import DocumentsImportFromRequestMode
from .types.documents_import_from_request_source import DocumentsImportFromRequestSource
from .types.documents_init_request_dedup_mode import DocumentsInitRequestDedupMode
from .types.documents_init_request_upload_preference import DocumentsInitRequestUploadPreference
from .types.list_documents_request_state import ListDocumentsRequestState
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDocumentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        tenant_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        state: typing.Optional[ListDocumentsRequestState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocumentsList200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        state : typing.Optional[ListDocumentsRequestState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocumentsList200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
                "state": state,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocumentsList200Response,
                    parse_obj_as(
                        type_=DocumentsList200Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def get(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DocumentsGet200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocumentsGet200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocumentsGet200Response,
                    parse_obj_as(
                        type_=DocumentsGet200Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def delete(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def commit(
        self, tenant_id: str, id: str, *, sha256: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DocumentsCommit200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        sha256 : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocumentsCommit200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}/commit",
            method="POST",
            json={
                "sha256": sha256,
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
                    DocumentsCommit200Response,
                    parse_obj_as(
                        type_=DocumentsCommit200Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    @contextlib.contextmanager
    def download(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            OK
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}/download",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    @contextlib.contextmanager
    def thumbnail(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            OK
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}/thumbnail",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 404:
                        raise NotFoundError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def upload_proxy(
        self, tenant_id: str, id: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DocumentsUploadProxy200Response]:
        """
        This bounded origin-mediated fallback must only be used after documents.init returns upload.kind=proxy. Auto mode prefers a presigned object-store PUT whenever available.

        Parameters
        ----------
        tenant_id : str

        id : str

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocumentsUploadProxy200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}/upload-proxy",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocumentsUploadProxy200Response,
                    parse_obj_as(
                        type_=DocumentsUploadProxy200Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    def import_from(
        self,
        tenant_id: str,
        *,
        source: DocumentsImportFromRequestSource,
        expected: typing.Optional[DocumentsImportFromRequestExpected] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        dedup_mode: typing.Optional[DocumentsImportFromRequestDedupMode] = OMIT,
        doc_id: typing.Optional[str] = OMIT,
        mode: typing.Optional[DocumentsImportFromRequestMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocumentsImportFrom200Response]:
        """
        Default mode is synchronous and bounded: the response returns only after the transfer verified and committed (or failed). mode=async (connection sources only) answers 202 immediately and an in-process worker performs the transfer with leased, fenced retries; poll the document until ready/failed. The deployment import policy gates scheme, network range, and size; sources must declare a length. CloudPDF copies and owns the bytes — the source is never referenced in place. A 502 marks a retryable upstream failure: retry with the same idempotencyKey to resume the same document. URL sources are capabilities and never echoed back. Connection sources name operator-registered storage (bucket/prefix scope, allowed credential classes, and tenant bindings are deployment configuration); `revision` is provider-interpreted (S3 VersionId, GCS generation, Azure version id).

        Parameters
        ----------
        tenant_id : str

        source : DocumentsImportFromRequestSource
            Where CloudPDF pulls the bytes from. The two shapes differ in WHO supplies the authority to read, not in which storage vendor holds the file.

        expected : typing.Optional[DocumentsImportFromRequestExpected]
            Integrity pins, enforced when present. When absent, the server-observed values become authoritative.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        idempotency_key : typing.Optional[str]
            Retrying with the same key resumes the same document rather than importing a second copy — including after a 502.

        dedup_mode : typing.Optional[DocumentsImportFromRequestDedupMode]
            always-create (default) creates a new document every time. reuse-existing returns a document that already holds the same content instead of storing it twice.

        doc_id : typing.Optional[str]

        mode : typing.Optional[DocumentsImportFromRequestMode]
            sync (default) holds the response open for the whole transfer. async answers 202 with the document pending and transfers in the background; it requires a connection source, and filesystem connections additionally require expected.sha256.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocumentsImportFrom200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/import",
            method="POST",
            json={
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=DocumentsImportFromRequestSource, direction="write"
                ),
                "expected": convert_and_respect_annotation_metadata(
                    object_=expected, annotation=DocumentsImportFromRequestExpected, direction="write"
                ),
                "metadata": metadata,
                "idempotencyKey": idempotency_key,
                "dedupMode": dedup_mode,
                "docId": doc_id,
                "mode": mode,
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
                    DocumentsImportFrom200Response,
                    parse_obj_as(
                        type_=DocumentsImportFrom200Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DocumentsImportFrom502Response,
                        parse_obj_as(
                            type_=DocumentsImportFrom502Response,
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

    def init(
        self,
        tenant_id: str,
        *,
        content_length: float,
        content_sha256: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        dedup_mode: typing.Optional[DocumentsInitRequestDedupMode] = OMIT,
        doc_id: typing.Optional[str] = OMIT,
        upload_ttl_sec: typing.Optional[float] = OMIT,
        upload_preference: typing.Optional[DocumentsInitRequestUploadPreference] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocumentsInit200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        content_length : float

        content_sha256 : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        idempotency_key : typing.Optional[str]

        dedup_mode : typing.Optional[DocumentsInitRequestDedupMode]
            always-create (default) creates a new document every time. reuse-existing returns a document that already holds the same content instead of storing it twice.

        doc_id : typing.Optional[str]

        upload_ttl_sec : typing.Optional[float]

        upload_preference : typing.Optional[DocumentsInitRequestUploadPreference]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocumentsInit200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/init",
            method="POST",
            json={
                "contentLength": content_length,
                "contentSha256": content_sha256,
                "metadata": metadata,
                "idempotencyKey": idempotency_key,
                "dedupMode": dedup_mode,
                "docId": doc_id,
                "uploadTtlSec": upload_ttl_sec,
                "uploadPreference": upload_preference,
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
                    DocumentsInit200Response,
                    parse_obj_as(
                        type_=DocumentsInit200Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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


class AsyncRawDocumentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        tenant_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        state: typing.Optional[ListDocumentsRequestState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocumentsList200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        state : typing.Optional[ListDocumentsRequestState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocumentsList200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
                "state": state,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocumentsList200Response,
                    parse_obj_as(
                        type_=DocumentsList200Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def get(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DocumentsGet200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocumentsGet200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocumentsGet200Response,
                    parse_obj_as(
                        type_=DocumentsGet200Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def delete(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def commit(
        self, tenant_id: str, id: str, *, sha256: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DocumentsCommit200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        sha256 : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocumentsCommit200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}/commit",
            method="POST",
            json={
                "sha256": sha256,
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
                    DocumentsCommit200Response,
                    parse_obj_as(
                        type_=DocumentsCommit200Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    @contextlib.asynccontextmanager
    async def download(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            OK
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}/download",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    @contextlib.asynccontextmanager
    async def thumbnail(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            OK
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}/thumbnail",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 404:
                        raise NotFoundError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def upload_proxy(
        self, tenant_id: str, id: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DocumentsUploadProxy200Response]:
        """
        This bounded origin-mediated fallback must only be used after documents.init returns upload.kind=proxy. Auto mode prefers a presigned object-store PUT whenever available.

        Parameters
        ----------
        tenant_id : str

        id : str

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocumentsUploadProxy200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/{encode_path_param(id)}/upload-proxy",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocumentsUploadProxy200Response,
                    parse_obj_as(
                        type_=DocumentsUploadProxy200Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    async def import_from(
        self,
        tenant_id: str,
        *,
        source: DocumentsImportFromRequestSource,
        expected: typing.Optional[DocumentsImportFromRequestExpected] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        dedup_mode: typing.Optional[DocumentsImportFromRequestDedupMode] = OMIT,
        doc_id: typing.Optional[str] = OMIT,
        mode: typing.Optional[DocumentsImportFromRequestMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocumentsImportFrom200Response]:
        """
        Default mode is synchronous and bounded: the response returns only after the transfer verified and committed (or failed). mode=async (connection sources only) answers 202 immediately and an in-process worker performs the transfer with leased, fenced retries; poll the document until ready/failed. The deployment import policy gates scheme, network range, and size; sources must declare a length. CloudPDF copies and owns the bytes — the source is never referenced in place. A 502 marks a retryable upstream failure: retry with the same idempotencyKey to resume the same document. URL sources are capabilities and never echoed back. Connection sources name operator-registered storage (bucket/prefix scope, allowed credential classes, and tenant bindings are deployment configuration); `revision` is provider-interpreted (S3 VersionId, GCS generation, Azure version id).

        Parameters
        ----------
        tenant_id : str

        source : DocumentsImportFromRequestSource
            Where CloudPDF pulls the bytes from. The two shapes differ in WHO supplies the authority to read, not in which storage vendor holds the file.

        expected : typing.Optional[DocumentsImportFromRequestExpected]
            Integrity pins, enforced when present. When absent, the server-observed values become authoritative.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        idempotency_key : typing.Optional[str]
            Retrying with the same key resumes the same document rather than importing a second copy — including after a 502.

        dedup_mode : typing.Optional[DocumentsImportFromRequestDedupMode]
            always-create (default) creates a new document every time. reuse-existing returns a document that already holds the same content instead of storing it twice.

        doc_id : typing.Optional[str]

        mode : typing.Optional[DocumentsImportFromRequestMode]
            sync (default) holds the response open for the whole transfer. async answers 202 with the document pending and transfers in the background; it requires a connection source, and filesystem connections additionally require expected.sha256.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocumentsImportFrom200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/import",
            method="POST",
            json={
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=DocumentsImportFromRequestSource, direction="write"
                ),
                "expected": convert_and_respect_annotation_metadata(
                    object_=expected, annotation=DocumentsImportFromRequestExpected, direction="write"
                ),
                "metadata": metadata,
                "idempotencyKey": idempotency_key,
                "dedupMode": dedup_mode,
                "docId": doc_id,
                "mode": mode,
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
                    DocumentsImportFrom200Response,
                    parse_obj_as(
                        type_=DocumentsImportFrom200Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DocumentsImportFrom502Response,
                        parse_obj_as(
                            type_=DocumentsImportFrom502Response,
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

    async def init(
        self,
        tenant_id: str,
        *,
        content_length: float,
        content_sha256: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        dedup_mode: typing.Optional[DocumentsInitRequestDedupMode] = OMIT,
        doc_id: typing.Optional[str] = OMIT,
        upload_ttl_sec: typing.Optional[float] = OMIT,
        upload_preference: typing.Optional[DocumentsInitRequestUploadPreference] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocumentsInit200Response]:
        """
        Parameters
        ----------
        tenant_id : str

        content_length : float

        content_sha256 : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        idempotency_key : typing.Optional[str]

        dedup_mode : typing.Optional[DocumentsInitRequestDedupMode]
            always-create (default) creates a new document every time. reuse-existing returns a document that already holds the same content instead of storing it twice.

        doc_id : typing.Optional[str]

        upload_ttl_sec : typing.Optional[float]

        upload_preference : typing.Optional[DocumentsInitRequestUploadPreference]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocumentsInit200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tenants/{encode_path_param(tenant_id)}/documents/init",
            method="POST",
            json={
                "contentLength": content_length,
                "contentSha256": content_sha256,
                "metadata": metadata,
                "idempotencyKey": idempotency_key,
                "dedupMode": dedup_mode,
                "docId": doc_id,
                "uploadTtlSec": upload_ttl_sec,
                "uploadPreference": upload_preference,
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
                    DocumentsInit200Response,
                    parse_obj_as(
                        type_=DocumentsInit200Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
