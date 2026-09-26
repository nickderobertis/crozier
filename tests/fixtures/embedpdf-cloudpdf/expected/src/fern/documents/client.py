

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.documents_commit200response import DocumentsCommit200Response
from ..types.documents_get200response import DocumentsGet200Response
from ..types.documents_import_from200response import DocumentsImportFrom200Response
from ..types.documents_init200response import DocumentsInit200Response
from ..types.documents_list200response import DocumentsList200Response
from ..types.documents_upload_proxy200response import DocumentsUploadProxy200Response
from .raw_client import AsyncRawDocumentsClient, RawDocumentsClient
from .types.documents_import_from_request_dedup_mode import DocumentsImportFromRequestDedupMode
from .types.documents_import_from_request_expected import DocumentsImportFromRequestExpected
from .types.documents_import_from_request_mode import DocumentsImportFromRequestMode
from .types.documents_import_from_request_source import DocumentsImportFromRequestSource
from .types.documents_init_request_dedup_mode import DocumentsInitRequestDedupMode
from .types.documents_init_request_upload_preference import DocumentsInitRequestUploadPreference
from .types.list_documents_request_state import ListDocumentsRequestState


OMIT = typing.cast(typing.Any, ...)


class DocumentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDocumentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDocumentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDocumentsClient
        """
        return self._raw_client

    def list(
        self,
        tenant_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        state: typing.Optional[ListDocumentsRequestState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocumentsList200Response:
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
        DocumentsList200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.documents.list(
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.list(
            tenant_id, limit=limit, cursor=cursor, state=state, request_options=request_options
        )
        return _response.data

    def get(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentsGet200Response:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentsGet200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.documents.get(
            tenant_id="tenantId",
            id="id",
        )
        """
        _response = self._raw_client.get(tenant_id, id, request_options=request_options)
        return _response.data

    def delete(self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.documents.delete(
            tenant_id="tenantId",
            id="id",
        )
        """
        _response = self._raw_client.delete(tenant_id, id, request_options=request_options)
        return _response.data

    def commit(
        self, tenant_id: str, id: str, *, sha256: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentsCommit200Response:
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
        DocumentsCommit200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.documents.commit(
            tenant_id="tenantId",
            id="id",
            sha256="sha256",
        )
        """
        _response = self._raw_client.commit(tenant_id, id, sha256=sha256, request_options=request_options)
        return _response.data

    def download(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.documents.download(
            tenant_id="tenantId",
            id="id",
        )
        """
        with self._raw_client.download(tenant_id, id, request_options=request_options) as r:
            yield from r.data

    def thumbnail(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.documents.thumbnail(
            tenant_id="tenantId",
            id="id",
        )
        """
        with self._raw_client.thumbnail(tenant_id, id, request_options=request_options) as r:
            yield from r.data

    def upload_proxy(
        self, tenant_id: str, id: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentsUploadProxy200Response:
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
        DocumentsUploadProxy200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.documents.upload_proxy(
            tenant_id="tenantId",
            id="id",
        )
        """
        _response = self._raw_client.upload_proxy(tenant_id, id, file=file, request_options=request_options)
        return _response.data

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
    ) -> DocumentsImportFrom200Response:
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
        DocumentsImportFrom200Response
            OK

        Examples
        --------
        from fern.documents import DocumentsImportFromRequestSource_Url

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.documents.import_from(
            tenant_id="tenantId",
            source=DocumentsImportFromRequestSource_Url(
                url="url",
            ),
        )
        """
        _response = self._raw_client.import_from(
            tenant_id,
            source=source,
            expected=expected,
            metadata=metadata,
            idempotency_key=idempotency_key,
            dedup_mode=dedup_mode,
            doc_id=doc_id,
            mode=mode,
            request_options=request_options,
        )
        return _response.data

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
    ) -> DocumentsInit200Response:
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
        DocumentsInit200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.documents.init(
            tenant_id="tenantId",
            content_length=1.1,
            content_sha256="contentSha256",
        )
        """
        _response = self._raw_client.init(
            tenant_id,
            content_length=content_length,
            content_sha256=content_sha256,
            metadata=metadata,
            idempotency_key=idempotency_key,
            dedup_mode=dedup_mode,
            doc_id=doc_id,
            upload_ttl_sec=upload_ttl_sec,
            upload_preference=upload_preference,
            request_options=request_options,
        )
        return _response.data


class AsyncDocumentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDocumentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDocumentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDocumentsClient
        """
        return self._raw_client

    async def list(
        self,
        tenant_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        state: typing.Optional[ListDocumentsRequestState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocumentsList200Response:
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
        DocumentsList200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.documents.list(
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            tenant_id, limit=limit, cursor=cursor, state=state, request_options=request_options
        )
        return _response.data

    async def get(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentsGet200Response:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentsGet200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.documents.get(
                tenant_id="tenantId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(tenant_id, id, request_options=request_options)
        return _response.data

    async def delete(self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.documents.delete(
                tenant_id="tenantId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(tenant_id, id, request_options=request_options)
        return _response.data

    async def commit(
        self, tenant_id: str, id: str, *, sha256: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentsCommit200Response:
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
        DocumentsCommit200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.documents.commit(
                tenant_id="tenantId",
                id="id",
                sha256="sha256",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.commit(tenant_id, id, sha256=sha256, request_options=request_options)
        return _response.data

    async def download(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.documents.download(
                tenant_id="tenantId",
                id="id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download(tenant_id, id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def thumbnail(
        self, tenant_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        tenant_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.documents.thumbnail(
                tenant_id="tenantId",
                id="id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.thumbnail(tenant_id, id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def upload_proxy(
        self, tenant_id: str, id: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> DocumentsUploadProxy200Response:
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
        DocumentsUploadProxy200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.documents.upload_proxy(
                tenant_id="tenantId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_proxy(tenant_id, id, file=file, request_options=request_options)
        return _response.data

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
    ) -> DocumentsImportFrom200Response:
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
        DocumentsImportFrom200Response
            OK

        Examples
        --------
        import asyncio

        from fern.documents import DocumentsImportFromRequestSource_Url

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.documents.import_from(
                tenant_id="tenantId",
                source=DocumentsImportFromRequestSource_Url(
                    url="url",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_from(
            tenant_id,
            source=source,
            expected=expected,
            metadata=metadata,
            idempotency_key=idempotency_key,
            dedup_mode=dedup_mode,
            doc_id=doc_id,
            mode=mode,
            request_options=request_options,
        )
        return _response.data

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
    ) -> DocumentsInit200Response:
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
        DocumentsInit200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.documents.init(
                tenant_id="tenantId",
                content_length=1.1,
                content_sha256="contentSha256",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.init(
            tenant_id,
            content_length=content_length,
            content_sha256=content_sha256,
            metadata=metadata,
            idempotency_key=idempotency_key,
            dedup_mode=dedup_mode,
            doc_id=doc_id,
            upload_ttl_sec=upload_ttl_sec,
            upload_preference=upload_preference,
            request_options=request_options,
        )
        return _response.data
