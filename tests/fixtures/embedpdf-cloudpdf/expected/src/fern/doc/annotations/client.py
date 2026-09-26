

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.doc_annotations_create200response import DocAnnotationsCreate200Response
from ...types.doc_annotations_create_request import DocAnnotationsCreateRequest
from ...types.doc_annotations_delete200response import DocAnnotationsDelete200Response
from ...types.doc_annotations_export_appearance_request import DocAnnotationsExportAppearanceRequest
from ...types.doc_annotations_flatten200response import DocAnnotationsFlatten200Response
from ...types.doc_annotations_flatten_request import DocAnnotationsFlattenRequest
from ...types.doc_annotations_list200response import DocAnnotationsList200Response
from ...types.doc_annotations_list_all200response import DocAnnotationsListAll200Response
from ...types.doc_annotations_update200response import DocAnnotationsUpdate200Response
from ...types.doc_annotations_update_request import DocAnnotationsUpdateRequest
from .raw_client import AsyncRawAnnotationsClient, RawAnnotationsClient


OMIT = typing.cast(typing.Any, ...)


class AnnotationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnnotationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnnotationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnnotationsClient
        """
        return self._raw_client

    def list_all(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsListAll200Response:
        """
        Returns one entry per page plus the audit-log cursor for reconciling subsequent document events. Page order is unspecified; join by `pageState.pageObjectNumber` when display order matters.

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
        DocAnnotationsListAll200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.annotations.list_all(
            doc_id="docId",
            layer_name="layerName",
        )
        """
        _response = self._raw_client.list_all(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        )
        return _response.data

    def list(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsList200Response:
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
        DocAnnotationsList200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.annotations.list(
            doc_id="docId",
            layer_name="layerName",
            page_key="pageKey",
        )
        """
        _response = self._raw_client.list(
            doc_id, layer_name, page_key, document_password=document_password, request_options=request_options
        )
        return _response.data

    def create(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        request: DocAnnotationsCreateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsCreate200Response:
        """
        Doc JWTs may instead carry collab scopes (annotations:create:self, …) that refine per-annotation authorship rules; the API token is exempt from both.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsCreateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocAnnotationsCreate200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.annotations.create(
            doc_id="docId",
            layer_name="layerName",
            page_key="pageKey",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create(
            doc_id,
            layer_name,
            page_key,
            request=request,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        annot_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsDelete200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        annot_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocAnnotationsDelete200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.annotations.delete(
            doc_id="docId",
            layer_name="layerName",
            page_key="pageKey",
            annot_key="annotKey",
        )
        """
        _response = self._raw_client.delete(
            doc_id,
            layer_name,
            page_key,
            annot_key,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    def update(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        annot_key: str,
        *,
        request: DocAnnotationsUpdateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsUpdate200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        annot_key : str

        request : DocAnnotationsUpdateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocAnnotationsUpdate200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.annotations.update(
            doc_id="docId",
            layer_name="layerName",
            page_key="pageKey",
            annot_key="annotKey",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update(
            doc_id,
            layer_name,
            page_key,
            annot_key,
            request=request,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    def export_appearance(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        request: DocAnnotationsExportAppearanceRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsExportAppearanceRequest

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
        client.doc.annotations.export_appearance(
            doc_id="docId",
            layer_name="layerName",
            page_key="pageKey",
            request={"string": {"key": "value"}},
        )
        """
        with self._raw_client.export_appearance(
            doc_id,
            layer_name,
            page_key,
            request=request,
            document_password=document_password,
            request_options=request_options,
        ) as r:
            yield from r.data

    def flatten(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        request: DocAnnotationsFlattenRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsFlatten200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsFlattenRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocAnnotationsFlatten200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.annotations.flatten(
            doc_id="docId",
            layer_name="layerName",
            page_key="pageKey",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.flatten(
            doc_id,
            layer_name,
            page_key,
            request=request,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data


class AsyncAnnotationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnnotationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnnotationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnnotationsClient
        """
        return self._raw_client

    async def list_all(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsListAll200Response:
        """
        Returns one entry per page plus the audit-log cursor for reconciling subsequent document events. Page order is unspecified; join by `pageState.pageObjectNumber` when display order matters.

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
        DocAnnotationsListAll200Response
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
            await client.doc.annotations.list_all(
                doc_id="docId",
                layer_name="layerName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def list(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsList200Response:
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
        DocAnnotationsList200Response
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
            await client.doc.annotations.list(
                doc_id="docId",
                layer_name="layerName",
                page_key="pageKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            doc_id, layer_name, page_key, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        request: DocAnnotationsCreateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsCreate200Response:
        """
        Doc JWTs may instead carry collab scopes (annotations:create:self, …) that refine per-annotation authorship rules; the API token is exempt from both.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsCreateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocAnnotationsCreate200Response
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
            await client.doc.annotations.create(
                doc_id="docId",
                layer_name="layerName",
                page_key="pageKey",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            doc_id,
            layer_name,
            page_key,
            request=request,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        annot_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsDelete200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        annot_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocAnnotationsDelete200Response
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
            await client.doc.annotations.delete(
                doc_id="docId",
                layer_name="layerName",
                page_key="pageKey",
                annot_key="annotKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            doc_id,
            layer_name,
            page_key,
            annot_key,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    async def update(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        annot_key: str,
        *,
        request: DocAnnotationsUpdateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsUpdate200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        annot_key : str

        request : DocAnnotationsUpdateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocAnnotationsUpdate200Response
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
            await client.doc.annotations.update(
                doc_id="docId",
                layer_name="layerName",
                page_key="pageKey",
                annot_key="annotKey",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            doc_id,
            layer_name,
            page_key,
            annot_key,
            request=request,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data

    async def export_appearance(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        request: DocAnnotationsExportAppearanceRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsExportAppearanceRequest

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
            await client.doc.annotations.export_appearance(
                doc_id="docId",
                layer_name="layerName",
                page_key="pageKey",
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        async with self._raw_client.export_appearance(
            doc_id,
            layer_name,
            page_key,
            request=request,
            document_password=document_password,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def flatten(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        request: DocAnnotationsFlattenRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocAnnotationsFlatten200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        request : DocAnnotationsFlattenRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocAnnotationsFlatten200Response
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
            await client.doc.annotations.flatten(
                doc_id="docId",
                layer_name="layerName",
                page_key="pageKey",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.flatten(
            doc_id,
            layer_name,
            page_key,
            request=request,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data
