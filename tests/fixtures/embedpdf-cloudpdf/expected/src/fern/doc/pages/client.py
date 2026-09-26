

import typing

from ... import core
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.doc_pages_delete200response import DocPagesDelete200Response
from ...types.doc_pages_delete_request import DocPagesDeleteRequest
from ...types.doc_pages_extract_request import DocPagesExtractRequest
from ...types.doc_pages_flatten200response import DocPagesFlatten200Response
from ...types.doc_pages_flatten_request import DocPagesFlattenRequest
from ...types.doc_pages_insert200response import DocPagesInsert200Response
from ...types.doc_pages_insert_blank200response import DocPagesInsertBlank200Response
from ...types.doc_pages_insert_blank_request import DocPagesInsertBlankRequest
from ...types.doc_pages_move200response import DocPagesMove200Response
from ...types.doc_pages_move_request import DocPagesMoveRequest
from ...types.doc_pages_remove_name200response import DocPagesRemoveName200Response
from ...types.doc_pages_remove_name_request import DocPagesRemoveNameRequest
from ...types.doc_pages_rotate200response import DocPagesRotate200Response
from ...types.doc_pages_rotate_request import DocPagesRotateRequest
from ...types.doc_pages_set_name200response import DocPagesSetName200Response
from ...types.doc_pages_set_name_request import DocPagesSetNameRequest
from ...types.doc_pages_set_scale200response import DocPagesSetScale200Response
from ...types.doc_pages_viewports200response import DocPagesViewports200Response
from .raw_client import AsyncRawPagesClient, RawPagesClient
from .types.doc_pages_set_scale_request_measure import DocPagesSetScaleRequestMeasure


OMIT = typing.cast(typing.Any, ...)


class PagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPagesClient
        """
        return self._raw_client

    def set_scale(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        measure: typing.Optional[DocPagesSetScaleRequestMeasure] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesSetScale200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        measure : typing.Optional[DocPagesSetScaleRequestMeasure]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesSetScale200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.pages.set_scale(
            doc_id="docId",
            layer_name="layerName",
            page_key="pageKey",
        )
        """
        _response = self._raw_client.set_scale(
            doc_id,
            layer_name,
            page_key,
            document_password=document_password,
            measure=measure,
            request_options=request_options,
        )
        return _response.data

    def viewports(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesViewports200Response:
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
        DocPagesViewports200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.pages.viewports(
            doc_id="docId",
            layer_name="layerName",
            page_key="pageKey",
        )
        """
        _response = self._raw_client.viewports(
            doc_id, layer_name, page_key, document_password=document_password, request_options=request_options
        )
        return _response.data

    def delete(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesDeleteRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesDelete200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesDeleteRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesDelete200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.pages.delete(
            doc_id="docId",
            layer_name="layerName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.delete(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    def extract(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesExtractRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        A read, not a mutation: the source document is untouched and no event is published. Body is `{"pageObjectNumbers": number[]}`; the response body is the new PDF.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesExtractRequest

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
        client.doc.pages.extract(
            doc_id="docId",
            layer_name="layerName",
            request={"string": {"key": "value"}},
        )
        """
        with self._raw_client.extract(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        ) as r:
            yield from r.data

    def flatten(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesFlattenRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesFlatten200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesFlattenRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesFlatten200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.pages.flatten(
            doc_id="docId",
            layer_name="layerName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.flatten(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    def insert(
        self,
        doc_id: str,
        layer_name: str,
        *,
        file: core.File,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesInsert200Response:
        """
        Multipart mutation envelope: a `body` field holding `{"destIndex"?: number}` (omitted → append) plus a `resource:source` file part carrying the standalone PDF whose pages are copied in. The inserted copies get fresh page object numbers, returned in insertion order.

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
        DocPagesInsert200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.pages.insert(
            doc_id="docId",
            layer_name="layerName",
        )
        """
        _response = self._raw_client.insert(
            doc_id, layer_name, file=file, document_password=document_password, request_options=request_options
        )
        return _response.data

    def insert_blank(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesInsertBlankRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesInsertBlank200Response:
        """
        Body is `{"size": {"width", "height"}, "count"?, "destIndex"?}` — size in PDF points, count in [1, 100], destIndex omitted → append.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesInsertBlankRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesInsertBlank200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.pages.insert_blank(
            doc_id="docId",
            layer_name="layerName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.insert_blank(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    def move(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesMoveRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesMove200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesMoveRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesMove200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.pages.move(
            doc_id="docId",
            layer_name="layerName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.move(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    def set_name(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesSetNameRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesSetName200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesSetNameRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesSetName200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.pages.set_name(
            doc_id="docId",
            layer_name="layerName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.set_name(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    def remove_name(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesRemoveNameRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesRemoveName200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesRemoveNameRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesRemoveName200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.pages.remove_name(
            doc_id="docId",
            layer_name="layerName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.remove_name(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    def rotate(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesRotateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesRotate200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesRotateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesRotate200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.pages.rotate(
            doc_id="docId",
            layer_name="layerName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.rotate(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data


class AsyncPagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPagesClient
        """
        return self._raw_client

    async def set_scale(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        measure: typing.Optional[DocPagesSetScaleRequestMeasure] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesSetScale200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        page_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        measure : typing.Optional[DocPagesSetScaleRequestMeasure]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesSetScale200Response
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
            await client.doc.pages.set_scale(
                doc_id="docId",
                layer_name="layerName",
                page_key="pageKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_scale(
            doc_id,
            layer_name,
            page_key,
            document_password=document_password,
            measure=measure,
            request_options=request_options,
        )
        return _response.data

    async def viewports(
        self,
        doc_id: str,
        layer_name: str,
        page_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesViewports200Response:
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
        DocPagesViewports200Response
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
            await client.doc.pages.viewports(
                doc_id="docId",
                layer_name="layerName",
                page_key="pageKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.viewports(
            doc_id, layer_name, page_key, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def delete(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesDeleteRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesDelete200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesDeleteRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesDelete200Response
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
            await client.doc.pages.delete(
                doc_id="docId",
                layer_name="layerName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def extract(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesExtractRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        A read, not a mutation: the source document is untouched and no event is published. Body is `{"pageObjectNumbers": number[]}`; the response body is the new PDF.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesExtractRequest

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
            await client.doc.pages.extract(
                doc_id="docId",
                layer_name="layerName",
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        async with self._raw_client.extract(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def flatten(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesFlattenRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesFlatten200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesFlattenRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesFlatten200Response
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
            await client.doc.pages.flatten(
                doc_id="docId",
                layer_name="layerName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.flatten(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def insert(
        self,
        doc_id: str,
        layer_name: str,
        *,
        file: core.File,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesInsert200Response:
        """
        Multipart mutation envelope: a `body` field holding `{"destIndex"?: number}` (omitted → append) plus a `resource:source` file part carrying the standalone PDF whose pages are copied in. The inserted copies get fresh page object numbers, returned in insertion order.

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
        DocPagesInsert200Response
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
            await client.doc.pages.insert(
                doc_id="docId",
                layer_name="layerName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.insert(
            doc_id, layer_name, file=file, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def insert_blank(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesInsertBlankRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesInsertBlank200Response:
        """
        Body is `{"size": {"width", "height"}, "count"?, "destIndex"?}` — size in PDF points, count in [1, 100], destIndex omitted → append.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesInsertBlankRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesInsertBlank200Response
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
            await client.doc.pages.insert_blank(
                doc_id="docId",
                layer_name="layerName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.insert_blank(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def move(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesMoveRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesMove200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesMoveRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesMove200Response
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
            await client.doc.pages.move(
                doc_id="docId",
                layer_name="layerName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.move(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def set_name(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesSetNameRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesSetName200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesSetNameRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesSetName200Response
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
            await client.doc.pages.set_name(
                doc_id="docId",
                layer_name="layerName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_name(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def remove_name(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesRemoveNameRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesRemoveName200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesRemoveNameRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesRemoveName200Response
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
            await client.doc.pages.remove_name(
                doc_id="docId",
                layer_name="layerName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_name(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def rotate(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocPagesRotateRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocPagesRotate200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocPagesRotateRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocPagesRotate200Response
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
            await client.doc.pages.rotate(
                doc_id="docId",
                layer_name="layerName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rotate(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data
