

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.doc_versions_analysis200response import DocVersionsAnalysis200Response
from ...types.doc_versions_list200response import DocVersionsList200Response
from ...types.doc_versions_signatures200response import DocVersionsSignatures200Response
from .raw_client import AsyncRawVersionsClient, RawVersionsClient
from .types.analysis_versions_request_level import AnalysisVersionsRequestLevel
from .types.signature_digest_versions_request_algorithm import SignatureDigestVersionsRequestAlgorithm


class VersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVersionsClient
        """
        return self._raw_client

    def list(
        self,
        doc_id: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocVersionsList200Response:
        """
        Every completed signature publishes a new version. Never cached: the list grows.

        Parameters
        ----------
        doc_id : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocVersionsList200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.versions.list(
            doc_id="docId",
        )
        """
        _response = self._raw_client.list(doc_id, document_password=document_password, request_options=request_options)
        return _response.data

    def analysis(
        self,
        doc_id: str,
        sha: str,
        *,
        since_signature: typing.Optional[int] = None,
        since_revision: typing.Optional[int] = None,
        level: typing.Optional[AnalysisVersionsRequestLevel] = None,
        until: typing.Optional[int] = None,
        policy: typing.Optional[int] = None,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocVersionsAnalysis200Response:
        """
        Exactly one of `since.signature` / `since.revision`; `until=<revision>` defaults to the last. The same answer for every layer and every caller.

        Parameters
        ----------
        doc_id : str

        sha : str

        since_signature : typing.Optional[int]

        since_revision : typing.Optional[int]

        level : typing.Optional[AnalysisVersionsRequestLevel]

        until : typing.Optional[int]

        policy : typing.Optional[int]

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocVersionsAnalysis200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.versions.analysis(
            doc_id="docId",
            sha="sha",
        )
        """
        _response = self._raw_client.analysis(
            doc_id,
            sha,
            since_signature=since_signature,
            since_revision=since_revision,
            level=level,
            until=until,
            policy=policy,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    def download(
        self,
        doc_id: str,
        sha: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        doc_id : str

        sha : str

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
        client.doc.versions.download(
            doc_id="docId",
            sha="sha",
        )
        """
        with self._raw_client.download(
            doc_id, sha, document_password=document_password, request_options=request_options
        ) as r:
            yield from r.data

    def revision(
        self,
        doc_id: str,
        sha: str,
        index: int,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        doc_id : str

        sha : str

        index : int

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
        client.doc.versions.revision(
            doc_id="docId",
            sha="sha",
            index=1,
        )
        """
        with self._raw_client.revision(
            doc_id, sha, index, document_password=document_password, request_options=request_options
        ) as r:
            yield from r.data

    def signatures(
        self,
        doc_id: str,
        sha: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocVersionsSignatures200Response:
        """
        Parameters
        ----------
        doc_id : str

        sha : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocVersionsSignatures200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.versions.signatures(
            doc_id="docId",
            sha="sha",
        )
        """
        _response = self._raw_client.signatures(
            doc_id, sha, document_password=document_password, request_options=request_options
        )
        return _response.data

    def signature_contents(
        self,
        doc_id: str,
        sha: str,
        field_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        `fieldKey` is the field's fully qualified name, token-text encoded (the same encoding attachment keys use).

        Parameters
        ----------
        doc_id : str

        sha : str

        field_key : str

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
        client.doc.versions.signature_contents(
            doc_id="docId",
            sha="sha",
            field_key="fieldKey",
        )
        """
        with self._raw_client.signature_contents(
            doc_id, sha, field_key, document_password=document_password, request_options=request_options
        ) as r:
            yield from r.data

    def signature_digest(
        self,
        doc_id: str,
        sha: str,
        field_key: str,
        algorithm: SignatureDigestVersionsRequestAlgorithm,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        What a CMS verifier compares its message digest to.

        Parameters
        ----------
        doc_id : str

        sha : str

        field_key : str

        algorithm : SignatureDigestVersionsRequestAlgorithm

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
        from fern.doc.versions import SignatureDigestVersionsRequestAlgorithm

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.versions.signature_digest(
            doc_id="docId",
            sha="sha",
            field_key="fieldKey",
            algorithm=SignatureDigestVersionsRequestAlgorithm.SHA1,
        )
        """
        with self._raw_client.signature_digest(
            doc_id, sha, field_key, algorithm, document_password=document_password, request_options=request_options
        ) as r:
            yield from r.data


class AsyncVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVersionsClient
        """
        return self._raw_client

    async def list(
        self,
        doc_id: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocVersionsList200Response:
        """
        Every completed signature publishes a new version. Never cached: the list grows.

        Parameters
        ----------
        doc_id : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocVersionsList200Response
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
            await client.doc.versions.list(
                doc_id="docId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            doc_id, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def analysis(
        self,
        doc_id: str,
        sha: str,
        *,
        since_signature: typing.Optional[int] = None,
        since_revision: typing.Optional[int] = None,
        level: typing.Optional[AnalysisVersionsRequestLevel] = None,
        until: typing.Optional[int] = None,
        policy: typing.Optional[int] = None,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocVersionsAnalysis200Response:
        """
        Exactly one of `since.signature` / `since.revision`; `until=<revision>` defaults to the last. The same answer for every layer and every caller.

        Parameters
        ----------
        doc_id : str

        sha : str

        since_signature : typing.Optional[int]

        since_revision : typing.Optional[int]

        level : typing.Optional[AnalysisVersionsRequestLevel]

        until : typing.Optional[int]

        policy : typing.Optional[int]

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocVersionsAnalysis200Response
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
            await client.doc.versions.analysis(
                doc_id="docId",
                sha="sha",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analysis(
            doc_id,
            sha,
            since_signature=since_signature,
            since_revision=since_revision,
            level=level,
            until=until,
            policy=policy,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    async def download(
        self,
        doc_id: str,
        sha: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        doc_id : str

        sha : str

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
            await client.doc.versions.download(
                doc_id="docId",
                sha="sha",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download(
            doc_id, sha, document_password=document_password, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def revision(
        self,
        doc_id: str,
        sha: str,
        index: int,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        doc_id : str

        sha : str

        index : int

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
            await client.doc.versions.revision(
                doc_id="docId",
                sha="sha",
                index=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.revision(
            doc_id, sha, index, document_password=document_password, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def signatures(
        self,
        doc_id: str,
        sha: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocVersionsSignatures200Response:
        """
        Parameters
        ----------
        doc_id : str

        sha : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocVersionsSignatures200Response
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
            await client.doc.versions.signatures(
                doc_id="docId",
                sha="sha",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.signatures(
            doc_id, sha, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def signature_contents(
        self,
        doc_id: str,
        sha: str,
        field_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        `fieldKey` is the field's fully qualified name, token-text encoded (the same encoding attachment keys use).

        Parameters
        ----------
        doc_id : str

        sha : str

        field_key : str

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
            await client.doc.versions.signature_contents(
                doc_id="docId",
                sha="sha",
                field_key="fieldKey",
            )


        asyncio.run(main())
        """
        async with self._raw_client.signature_contents(
            doc_id, sha, field_key, document_password=document_password, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def signature_digest(
        self,
        doc_id: str,
        sha: str,
        field_key: str,
        algorithm: SignatureDigestVersionsRequestAlgorithm,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        What a CMS verifier compares its message digest to.

        Parameters
        ----------
        doc_id : str

        sha : str

        field_key : str

        algorithm : SignatureDigestVersionsRequestAlgorithm

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

        from fern.doc.versions import SignatureDigestVersionsRequestAlgorithm

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.doc.versions.signature_digest(
                doc_id="docId",
                sha="sha",
                field_key="fieldKey",
                algorithm=SignatureDigestVersionsRequestAlgorithm.SHA1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.signature_digest(
            doc_id, sha, field_key, algorithm, document_password=document_password, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
