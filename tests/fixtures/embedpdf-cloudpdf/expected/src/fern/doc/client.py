

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.doc_head200response import DocHead200Response
from ..types.doc_manifest200response import DocManifest200Response
from ..types.doc_text200response import DocText200Response
from .raw_client import AsyncRawDocClient, RawDocClient

if typing.TYPE_CHECKING:
    from .annotations.client import AnnotationsClient, AsyncAnnotationsClient
    from .forms.client import AsyncFormsClient, FormsClient
    from .metadata.client import AsyncMetadataClient, MetadataClient
    from .pages.client import AsyncPagesClient, PagesClient
    from .redactions.client import AsyncRedactionsClient, RedactionsClient
    from .signatures.client import AsyncSignaturesClient, SignaturesClient
    from .versions.client import AsyncVersionsClient, VersionsClient


class DocClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDocClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._annotations: typing.Optional[AnnotationsClient] = None
        self._forms: typing.Optional[FormsClient] = None
        self._metadata: typing.Optional[MetadataClient] = None
        self._pages: typing.Optional[PagesClient] = None
        self._redactions: typing.Optional[RedactionsClient] = None
        self._signatures: typing.Optional[SignaturesClient] = None
        self._versions: typing.Optional[VersionsClient] = None

    @property
    def with_raw_response(self) -> RawDocClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDocClient
        """
        return self._raw_client

    def head(
        self,
        doc_id: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocHead200Response:
        """
        Parameters
        ----------
        doc_id : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocHead200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.head(
            doc_id="docId",
        )
        """
        _response = self._raw_client.head(doc_id, document_password=document_password, request_options=request_options)
        return _response.data

    def download(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

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
        client.doc.download(
            doc_id="docId",
            layer_name="layerName",
        )
        """
        with self._raw_client.download(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        ) as r:
            yield from r.data

    def manifest(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocManifest200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocManifest200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.manifest(
            doc_id="docId",
            layer_name="layerName",
        )
        """
        _response = self._raw_client.manifest(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        )
        return _response.data

    def render(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Render parameters (viewport, format) pass as flat dotted query keys, e.g. `?viewport.kind=width&viewport.width=800`; the full grammar is documented with the viewer.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

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
        client.doc.render(
            doc_id="docId",
            layer_name="layerName",
            page_key="pageKey",
        )
        """
        with self._raw_client.render(
            doc_id, layer_name, page_key, document_password=document_password, request_options=request_options
        ) as r:
            yield from r.data

    def text(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocText200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocText200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.text(
            doc_id="docId",
            layer_name="layerName",
            page_key="pageKey",
        )
        """
        _response = self._raw_client.text(
            doc_id, layer_name, page_key, document_password=document_password, request_options=request_options
        )
        return _response.data

    @property
    def annotations(self):
        if self._annotations is None:
            from .annotations.client import AnnotationsClient

            self._annotations = AnnotationsClient(client_wrapper=self._client_wrapper)
        return self._annotations

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import FormsClient

            self._forms = FormsClient(client_wrapper=self._client_wrapper)
        return self._forms

    @property
    def metadata(self):
        if self._metadata is None:
            from .metadata.client import MetadataClient

            self._metadata = MetadataClient(client_wrapper=self._client_wrapper)
        return self._metadata

    @property
    def pages(self):
        if self._pages is None:
            from .pages.client import PagesClient

            self._pages = PagesClient(client_wrapper=self._client_wrapper)
        return self._pages

    @property
    def redactions(self):
        if self._redactions is None:
            from .redactions.client import RedactionsClient

            self._redactions = RedactionsClient(client_wrapper=self._client_wrapper)
        return self._redactions

    @property
    def signatures(self):
        if self._signatures is None:
            from .signatures.client import SignaturesClient

            self._signatures = SignaturesClient(client_wrapper=self._client_wrapper)
        return self._signatures

    @property
    def versions(self):
        if self._versions is None:
            from .versions.client import VersionsClient

            self._versions = VersionsClient(client_wrapper=self._client_wrapper)
        return self._versions


class AsyncDocClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDocClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._annotations: typing.Optional[AsyncAnnotationsClient] = None
        self._forms: typing.Optional[AsyncFormsClient] = None
        self._metadata: typing.Optional[AsyncMetadataClient] = None
        self._pages: typing.Optional[AsyncPagesClient] = None
        self._redactions: typing.Optional[AsyncRedactionsClient] = None
        self._signatures: typing.Optional[AsyncSignaturesClient] = None
        self._versions: typing.Optional[AsyncVersionsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawDocClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDocClient
        """
        return self._raw_client

    async def head(
        self,
        doc_id: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocHead200Response:
        """
        Parameters
        ----------
        doc_id : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocHead200Response
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
            await client.doc.head(
                doc_id="docId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head(
            doc_id, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def download(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

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
            await client.doc.download(
                doc_id="docId",
                layer_name="layerName",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def manifest(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocManifest200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocManifest200Response
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
            await client.doc.manifest(
                doc_id="docId",
                layer_name="layerName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.manifest(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def render(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Render parameters (viewport, format) pass as flat dotted query keys, e.g. `?viewport.kind=width&viewport.width=800`; the full grammar is documented with the viewer.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

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
            await client.doc.render(
                doc_id="docId",
                layer_name="layerName",
                page_key="pageKey",
            )


        asyncio.run(main())
        """
        async with self._raw_client.render(
            doc_id, layer_name, page_key, document_password=document_password, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def text(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocText200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocText200Response
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
            await client.doc.text(
                doc_id="docId",
                layer_name="layerName",
                page_key="pageKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.text(
            doc_id, layer_name, page_key, document_password=document_password, request_options=request_options
        )
        return _response.data

    @property
    def annotations(self):
        if self._annotations is None:
            from .annotations.client import AsyncAnnotationsClient

            self._annotations = AsyncAnnotationsClient(client_wrapper=self._client_wrapper)
        return self._annotations

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import AsyncFormsClient

            self._forms = AsyncFormsClient(client_wrapper=self._client_wrapper)
        return self._forms

    @property
    def metadata(self):
        if self._metadata is None:
            from .metadata.client import AsyncMetadataClient

            self._metadata = AsyncMetadataClient(client_wrapper=self._client_wrapper)
        return self._metadata

    @property
    def pages(self):
        if self._pages is None:
            from .pages.client import AsyncPagesClient

            self._pages = AsyncPagesClient(client_wrapper=self._client_wrapper)
        return self._pages

    @property
    def redactions(self):
        if self._redactions is None:
            from .redactions.client import AsyncRedactionsClient

            self._redactions = AsyncRedactionsClient(client_wrapper=self._client_wrapper)
        return self._redactions

    @property
    def signatures(self):
        if self._signatures is None:
            from .signatures.client import AsyncSignaturesClient

            self._signatures = AsyncSignaturesClient(client_wrapper=self._client_wrapper)
        return self._signatures

    @property
    def versions(self):
        if self._versions is None:
            from .versions.client import AsyncVersionsClient

            self._versions = AsyncVersionsClient(client_wrapper=self._client_wrapper)
        return self._versions
