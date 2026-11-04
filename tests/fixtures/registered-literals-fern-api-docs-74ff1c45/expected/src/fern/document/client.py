

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_document_response import CreateDocumentResponse
from ..types.delete_document_request import DeleteDocumentRequest
from ..types.delete_document_response import DeleteDocumentResponse
from ..types.delete_documents_response import DeleteDocumentsResponse
from ..types.get_document_response import GetDocumentResponse
from ..types.get_documents_response import GetDocumentsResponse
from ..types.update_document_response import UpdateDocumentResponse
from .raw_client import AsyncRawDocumentClient, RawDocumentClient


OMIT = typing.cast(typing.Any, ...)


class DocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDocumentClient
        """
        return self._raw_client

    def create_document(
        self,
        domain: str,
        *,
        request: typing.Any,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CreateDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Any

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreateDocumentResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.document.create_document(
            domain="domain",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_document(
            domain, request=request, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    def batch_create_document(
        self,
        domain: str,
        *,
        request: typing.Sequence[typing.Any],
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CreateDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Sequence[typing.Any]

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreateDocumentResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.document.batch_create_document(
            domain="domain",
            request=[],
        )
        """
        _response = self._raw_client.batch_create_document(
            domain, request=request, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    def get_document_by_id(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDocumentResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.document.get_document_by_id(
            domain="domain",
            document_id="document_id",
        )
        """
        _response = self._raw_client.get_document_by_id(
            domain, document_id, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    def delete_document(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDocumentResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.document.delete_document(
            domain="domain",
            document_id="document_id",
        )
        """
        _response = self._raw_client.delete_document(
            domain, document_id, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    def update_document(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        document: typing.Optional[str] = OMIT,
        chunk: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        product: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        authed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        document : typing.Optional[str]
            The updated content of the document that will be returned to Ask Fern during document retrieval. If not provided, this field will remain unchanged.

        chunk : typing.Optional[str]
            The updated textual content that should be vectorized when indexing the document. If not provided, this field will remain unchanged.

        title : typing.Optional[str]
            The updated title of the document. If not provided, this field will remain unchanged.

        url : typing.Optional[str]
            The updated url of the document. If not provided, this field will remain unchanged.

        version : typing.Optional[str]
            The updated version of the document. If not provided, this field will remain unchanged.

        product : typing.Optional[str]
            The updated product of the document. If not provided, this field will remain unchanged.

        keywords : typing.Optional[typing.Sequence[str]]
            The updated keywords of the document. If not provided, this field will remain unchanged.

        authed : typing.Optional[bool]
            The updated authed status of the document. If not provided, this field will remain unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateDocumentResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.document.update_document(
            domain="domain",
            document_id="document_id",
        )
        """
        _response = self._raw_client.update_document(
            domain,
            document_id,
            fern_basepath=fern_basepath,
            document=document,
            chunk=chunk,
            title=title,
            url=url,
            version=version,
            product=product,
            keywords=keywords,
            authed=authed,
            request_options=request_options,
        )
        return _response.data

    def delete_document_by_id(
        self,
        domain: str,
        *,
        document_id: str,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        document_id : str
            The unique identifier of the document to delete

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDocumentResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.document.delete_document_by_id(
            domain="domain",
            document_id="document_id",
        )
        """
        _response = self._raw_client.delete_document_by_id(
            domain, document_id=document_id, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    def batch_delete_document(
        self,
        domain: str,
        *,
        request: typing.Sequence[DeleteDocumentRequest],
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        request : typing.Sequence[DeleteDocumentRequest]

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDocumentResponse
            Successful Response

        Examples
        --------
        from fern import DeleteDocumentRequest, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.document.batch_delete_document(
            domain="domain",
            request=[
                DeleteDocumentRequest(
                    document_id="document_id",
                )
            ],
        )
        """
        _response = self._raw_client.batch_delete_document(
            domain, request=request, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    def get_documents(
        self,
        domain: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDocumentsResponse:
        """
        Parameters
        ----------
        domain : str

        page : typing.Optional[int]
            The page number for pagination

        limit : typing.Optional[int]
            The number of documents per page

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDocumentsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.document.get_documents(
            domain="domain",
        )
        """
        _response = self._raw_client.get_documents(
            domain, page=page, limit=limit, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    def delete_documents(
        self,
        domain: str,
        *,
        product: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        url_prefix: typing.Optional[str] = None,
        all_: typing.Optional[bool] = None,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDocumentsResponse:
        """
        Delete the documents of a domain, narrowed by the provided filters. Filters are combined with AND, so a document is
        only deleted when it matches all of them. At least one filter is required, or pass `all=true` to delete every
        document. The `x-fern-basepath` header narrows the deletion to a single basepath.

        Parameters
        ----------
        domain : str

        product : typing.Optional[str]
            Only delete documents whose product matches this value exactly.

        version : typing.Optional[str]
            Only delete documents whose version matches this value exactly.

        url_prefix : typing.Optional[str]
            Only delete documents whose url starts with this value.

        all_ : typing.Optional[bool]
            Delete every document in the domain and basepath. Cannot be combined with the product, version or url_prefix filters.

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDocumentsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.document.delete_documents(
            domain="domain",
        )
        """
        _response = self._raw_client.delete_documents(
            domain,
            product=product,
            version=version,
            url_prefix=url_prefix,
            all_=all_,
            fern_basepath=fern_basepath,
            request_options=request_options,
        )
        return _response.data

    def delete_all_documents(
        self,
        domain: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDocumentResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.document.delete_all_documents(
            domain="domain",
        )
        """
        _response = self._raw_client.delete_all_documents(
            domain, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data


class AsyncDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDocumentClient
        """
        return self._raw_client

    async def create_document(
        self,
        domain: str,
        *,
        request: typing.Any,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CreateDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Any

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreateDocumentResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.document.create_document(
                domain="domain",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_document(
            domain, request=request, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    async def batch_create_document(
        self,
        domain: str,
        *,
        request: typing.Sequence[typing.Any],
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CreateDocumentResponse]:
        """
        Parameters
        ----------
        domain : str

        request : typing.Sequence[typing.Any]

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreateDocumentResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.document.batch_create_document(
                domain="domain",
                request=[],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_create_document(
            domain, request=request, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    async def get_document_by_id(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.document.get_document_by_id(
                domain="domain",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_document_by_id(
            domain, document_id, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    async def delete_document(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.document.delete_document(
                domain="domain",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_document(
            domain, document_id, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    async def update_document(
        self,
        domain: str,
        document_id: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        document: typing.Optional[str] = OMIT,
        chunk: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        product: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        authed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        document_id : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        document : typing.Optional[str]
            The updated content of the document that will be returned to Ask Fern during document retrieval. If not provided, this field will remain unchanged.

        chunk : typing.Optional[str]
            The updated textual content that should be vectorized when indexing the document. If not provided, this field will remain unchanged.

        title : typing.Optional[str]
            The updated title of the document. If not provided, this field will remain unchanged.

        url : typing.Optional[str]
            The updated url of the document. If not provided, this field will remain unchanged.

        version : typing.Optional[str]
            The updated version of the document. If not provided, this field will remain unchanged.

        product : typing.Optional[str]
            The updated product of the document. If not provided, this field will remain unchanged.

        keywords : typing.Optional[typing.Sequence[str]]
            The updated keywords of the document. If not provided, this field will remain unchanged.

        authed : typing.Optional[bool]
            The updated authed status of the document. If not provided, this field will remain unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.document.update_document(
                domain="domain",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_document(
            domain,
            document_id,
            fern_basepath=fern_basepath,
            document=document,
            chunk=chunk,
            title=title,
            url=url,
            version=version,
            product=product,
            keywords=keywords,
            authed=authed,
            request_options=request_options,
        )
        return _response.data

    async def delete_document_by_id(
        self,
        domain: str,
        *,
        document_id: str,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        document_id : str
            The unique identifier of the document to delete

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.document.delete_document_by_id(
                domain="domain",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_document_by_id(
            domain, document_id=document_id, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    async def batch_delete_document(
        self,
        domain: str,
        *,
        request: typing.Sequence[DeleteDocumentRequest],
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        request : typing.Sequence[DeleteDocumentRequest]

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DeleteDocumentRequest

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.document.batch_delete_document(
                domain="domain",
                request=[
                    DeleteDocumentRequest(
                        document_id="document_id",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_delete_document(
            domain, request=request, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    async def get_documents(
        self,
        domain: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDocumentsResponse:
        """
        Parameters
        ----------
        domain : str

        page : typing.Optional[int]
            The page number for pagination

        limit : typing.Optional[int]
            The number of documents per page

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDocumentsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.document.get_documents(
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_documents(
            domain, page=page, limit=limit, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data

    async def delete_documents(
        self,
        domain: str,
        *,
        product: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        url_prefix: typing.Optional[str] = None,
        all_: typing.Optional[bool] = None,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDocumentsResponse:
        """
        Delete the documents of a domain, narrowed by the provided filters. Filters are combined with AND, so a document is
        only deleted when it matches all of them. At least one filter is required, or pass `all=true` to delete every
        document. The `x-fern-basepath` header narrows the deletion to a single basepath.

        Parameters
        ----------
        domain : str

        product : typing.Optional[str]
            Only delete documents whose product matches this value exactly.

        version : typing.Optional[str]
            Only delete documents whose version matches this value exactly.

        url_prefix : typing.Optional[str]
            Only delete documents whose url starts with this value.

        all_ : typing.Optional[bool]
            Delete every document in the domain and basepath. Cannot be combined with the product, version or url_prefix filters.

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDocumentsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.document.delete_documents(
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_documents(
            domain,
            product=product,
            version=version,
            url_prefix=url_prefix,
            all_=all_,
            fern_basepath=fern_basepath,
            request_options=request_options,
        )
        return _response.data

    async def delete_all_documents(
        self,
        domain: str,
        *,
        fern_basepath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDocumentResponse:
        """
        Parameters
        ----------
        domain : str

        fern_basepath : typing.Optional[str]
            The basepath of the docs site that the document belongs to, e.g. `/plants` for a site served at `docs.example.com/plants`. Omit this for sites served at the root of the domain. Documents are only retrieved by Ask Fern on the site matching the domain and basepath they were created with.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDocumentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.document.delete_all_documents(
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_all_documents(
            domain, fern_basepath=fern_basepath, request_options=request_options
        )
        return _response.data
