

import typing

from ... import core
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.doc_signatures_abort200response import DocSignaturesAbort200Response
from ...types.doc_signatures_analysis200response import DocSignaturesAnalysis200Response
from ...types.doc_signatures_complete200response import DocSignaturesComplete200Response
from ...types.doc_signatures_list200response import DocSignaturesList200Response
from ...types.doc_signatures_prepare200response import DocSignaturesPrepare200Response
from .raw_client import AsyncRawSignaturesClient, RawSignaturesClient
from .types.analysis_signatures_request_level import AnalysisSignaturesRequestLevel
from .types.doc_signatures_complete_request_expected_version import DocSignaturesCompleteRequestExpectedVersion


OMIT = typing.cast(typing.Any, ...)


class SignaturesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSignaturesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSignaturesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSignaturesClient
        """
        return self._raw_client

    def list(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocSignaturesList200Response:
        """
        Describes the bytes the layer is over: the base version's signatures plus the layer's own edits as the last revision. Signed bytes (contents, digests, revision prefixes) are served per base version under /versions.

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
        DocSignaturesList200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.signatures.list(
            doc_id="docId",
            layer_name="layerName",
        )
        """
        _response = self._raw_client.list(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        )
        return _response.data

    def abort(
        self,
        doc_id: str,
        layer_name: str,
        signing_id: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocSignaturesAbort200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        signing_id : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSignaturesAbort200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.signatures.abort(
            doc_id="docId",
            layer_name="layerName",
            signing_id="signingId",
        )
        """
        _response = self._raw_client.abort(
            doc_id, layer_name, signing_id, document_password=document_password, request_options=request_options
        )
        return _response.data

    def complete(
        self,
        doc_id: str,
        layer_name: str,
        signing_id: str,
        *,
        cms: str,
        expected_version: DocSignaturesCompleteRequestExpectedVersion,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocSignaturesComplete200Response:
        """
        `cms` is the detached CMS over the prepared digest, base64. `expectedVersion` must be what prepare returned. Idempotent by signing id: the same CMS again answers `already-completed`. Every layer of the document then sits over the new version; refetch the manifest after a completion.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        signing_id : str

        cms : str

        expected_version : DocSignaturesCompleteRequestExpectedVersion

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSignaturesComplete200Response
            OK

        Examples
        --------
        from fern.doc.signatures import DocSignaturesCompleteRequestExpectedVersion

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.signatures.complete(
            doc_id="docId",
            layer_name="layerName",
            signing_id="signingId",
            cms="cms",
            expected_version=DocSignaturesCompleteRequestExpectedVersion(
                base_sha256="baseSha256",
                edits_version=1,
            ),
        )
        """
        _response = self._raw_client.complete(
            doc_id,
            layer_name,
            signing_id,
            cms=cms,
            expected_version=expected_version,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    def analysis(
        self,
        doc_id: str,
        layer_name: str,
        *,
        since_signature: typing.Optional[int] = None,
        since_revision: typing.Optional[int] = None,
        level: typing.Optional[AnalysisSignaturesRequestLevel] = None,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocSignaturesAnalysis200Response:
        """
        Exactly one of `since.signature=<index>` or `since.revision=<index>`; the layer's pending edits are the end. `level=fill|annotate|lta|none` evaluates exploratorily and never becomes a verdict. For history between two base revisions use the version analysis.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        since_signature : typing.Optional[int]

        since_revision : typing.Optional[int]

        level : typing.Optional[AnalysisSignaturesRequestLevel]

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSignaturesAnalysis200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.signatures.analysis(
            doc_id="docId",
            layer_name="layerName",
        )
        """
        _response = self._raw_client.analysis(
            doc_id,
            layer_name,
            since_signature=since_signature,
            since_revision=since_revision,
            level=level,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    def prepare(
        self,
        doc_id: str,
        layer_name: str,
        *,
        file: core.File,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocSignaturesPrepare200Response:
        """
        The multipart envelope: a JSON `body` part (field, subFilter, digest, contentsSize, signer, certify, lock, appearance) and an optional `resource:<key>` PDF part the body's `appearance.resource` names. A certification (`certify.permission`) additionally requires `doc.sign.certify`. The layer is read-only until the signing completes, is aborted, or expires (15 minutes). A layer behind the document head cannot sign (StaleBase).

        Parameters
        ----------
        doc_id : str

        layer_name : str

        file : core.File
            See core.File for more documentation

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSignaturesPrepare200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.signatures.prepare(
            doc_id="docId",
            layer_name="layerName",
        )
        """
        _response = self._raw_client.prepare(
            doc_id, layer_name, file=file, document_password=document_password, request_options=request_options
        )
        return _response.data


class AsyncSignaturesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSignaturesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSignaturesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSignaturesClient
        """
        return self._raw_client

    async def list(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocSignaturesList200Response:
        """
        Describes the bytes the layer is over: the base version's signatures plus the layer's own edits as the last revision. Signed bytes (contents, digests, revision prefixes) are served per base version under /versions.

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
        DocSignaturesList200Response
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
            await client.doc.signatures.list(
                doc_id="docId",
                layer_name="layerName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def abort(
        self,
        doc_id: str,
        layer_name: str,
        signing_id: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocSignaturesAbort200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        signing_id : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSignaturesAbort200Response
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
            await client.doc.signatures.abort(
                doc_id="docId",
                layer_name="layerName",
                signing_id="signingId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.abort(
            doc_id, layer_name, signing_id, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def complete(
        self,
        doc_id: str,
        layer_name: str,
        signing_id: str,
        *,
        cms: str,
        expected_version: DocSignaturesCompleteRequestExpectedVersion,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocSignaturesComplete200Response:
        """
        `cms` is the detached CMS over the prepared digest, base64. `expectedVersion` must be what prepare returned. Idempotent by signing id: the same CMS again answers `already-completed`. Every layer of the document then sits over the new version; refetch the manifest after a completion.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        signing_id : str

        cms : str

        expected_version : DocSignaturesCompleteRequestExpectedVersion

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSignaturesComplete200Response
            OK

        Examples
        --------
        import asyncio

        from fern.doc.signatures import DocSignaturesCompleteRequestExpectedVersion

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.doc.signatures.complete(
                doc_id="docId",
                layer_name="layerName",
                signing_id="signingId",
                cms="cms",
                expected_version=DocSignaturesCompleteRequestExpectedVersion(
                    base_sha256="baseSha256",
                    edits_version=1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete(
            doc_id,
            layer_name,
            signing_id,
            cms=cms,
            expected_version=expected_version,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    async def analysis(
        self,
        doc_id: str,
        layer_name: str,
        *,
        since_signature: typing.Optional[int] = None,
        since_revision: typing.Optional[int] = None,
        level: typing.Optional[AnalysisSignaturesRequestLevel] = None,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocSignaturesAnalysis200Response:
        """
        Exactly one of `since.signature=<index>` or `since.revision=<index>`; the layer's pending edits are the end. `level=fill|annotate|lta|none` evaluates exploratorily and never becomes a verdict. For history between two base revisions use the version analysis.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        since_signature : typing.Optional[int]

        since_revision : typing.Optional[int]

        level : typing.Optional[AnalysisSignaturesRequestLevel]

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSignaturesAnalysis200Response
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
            await client.doc.signatures.analysis(
                doc_id="docId",
                layer_name="layerName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analysis(
            doc_id,
            layer_name,
            since_signature=since_signature,
            since_revision=since_revision,
            level=level,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    async def prepare(
        self,
        doc_id: str,
        layer_name: str,
        *,
        file: core.File,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocSignaturesPrepare200Response:
        """
        The multipart envelope: a JSON `body` part (field, subFilter, digest, contentsSize, signer, certify, lock, appearance) and an optional `resource:<key>` PDF part the body's `appearance.resource` names. A certification (`certify.permission`) additionally requires `doc.sign.certify`. The layer is read-only until the signing completes, is aborted, or expires (15 minutes). A layer behind the document head cannot sign (StaleBase).

        Parameters
        ----------
        doc_id : str

        layer_name : str

        file : core.File
            See core.File for more documentation

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocSignaturesPrepare200Response
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
            await client.doc.signatures.prepare(
                doc_id="docId",
                layer_name="layerName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prepare(
            doc_id, layer_name, file=file, document_password=document_password, request_options=request_options
        )
        return _response.data
