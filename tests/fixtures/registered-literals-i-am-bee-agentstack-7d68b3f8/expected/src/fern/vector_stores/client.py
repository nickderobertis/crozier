

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output16 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output17 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17,
)
from ..types.paginated_result_vector_store_document import PaginatedResultVectorStoreDocument
from ..types.paginated_result_vector_store_search_result import PaginatedResultVectorStoreSearchResult
from ..types.vector_store_item import VectorStoreItem
from .raw_client import AsyncRawVectorStoresClient, RawVectorStoresClient


OMIT = typing.cast(typing.Any, ...)


class VectorStoresClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVectorStoresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVectorStoresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVectorStoresClient
        """
        return self._raw_client

    def create_vector_store(
        self,
        *,
        name: str,
        dimension: int,
        model_id: str,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16:
        """
        Create a new vector store.

        Parameters
        ----------
        name : str
            Name of the vector store

        dimension : int
            Dimension of the vectors to be stored

        model_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_stores.create_vector_store(
            name="name",
            dimension=1,
            model_id="model_id",
        )
        """
        _response = self._raw_client.create_vector_store(
            name=name, dimension=dimension, model_id=model_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    def get_vector_store(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17:
        """
        Get a vector store by ID.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_stores.get_vector_store(
            vector_store_id="vector_store_id",
        )
        """
        _response = self._raw_client.get_vector_store(
            vector_store_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    def add_items(
        self,
        vector_store_id: str,
        *,
        request: typing.Sequence[VectorStoreItem],
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        vector_store_id : str

        request : typing.Sequence[VectorStoreItem]

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, VectorStoreItem

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_stores.add_items(
            vector_store_id="vector_store_id",
            request=[
                VectorStoreItem(
                    document_id="document_id",
                    text="text",
                    embedding=[1.1],
                )
            ],
        )
        """
        _response = self._raw_client.add_items(
            vector_store_id, request=request, context_id=context_id, request_options=request_options
        )
        return _response.data

    def delete_vector_store(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a vector store by ID.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_stores.delete_vector_store(
            vector_store_id="vector_store_id",
        )
        """
        _response = self._raw_client.delete_vector_store(
            vector_store_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    def search_with_vector(
        self,
        vector_store_id: str,
        *,
        query_vector: typing.Sequence[float],
        context_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultVectorStoreSearchResult:
        """
        Search a vector store using either text or a vector.

        Parameters
        ----------
        vector_store_id : str

        query_vector : typing.Sequence[float]
            Vector to search for

        context_id : typing.Optional[str]

        limit : typing.Optional[int]
            Maximum number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultVectorStoreSearchResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_stores.search_with_vector(
            vector_store_id="vector_store_id",
            query_vector=[1.1],
        )
        """
        _response = self._raw_client.search_with_vector(
            vector_store_id,
            query_vector=query_vector,
            context_id=context_id,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def list_documents(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultVectorStoreDocument:
        """
        List all documents in a vector store.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultVectorStoreDocument
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_stores.list_documents(
            vector_store_id="vector_store_id",
        )
        """
        _response = self._raw_client.list_documents(
            vector_store_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    def delete_document(
        self,
        vector_store_id: str,
        document_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a document by ID.

        Parameters
        ----------
        vector_store_id : str

        document_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.vector_stores.delete_document(
            vector_store_id="vector_store_id",
            document_id="document_id",
        )
        """
        _response = self._raw_client.delete_document(
            vector_store_id, document_id, context_id=context_id, request_options=request_options
        )
        return _response.data


class AsyncVectorStoresClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVectorStoresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVectorStoresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVectorStoresClient
        """
        return self._raw_client

    async def create_vector_store(
        self,
        *,
        name: str,
        dimension: int,
        model_id: str,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16:
        """
        Create a new vector store.

        Parameters
        ----------
        name : str
            Name of the vector store

        dimension : int
            Dimension of the vectors to be stored

        model_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_stores.create_vector_store(
                name="name",
                dimension=1,
                model_id="model_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_vector_store(
            name=name, dimension=dimension, model_id=model_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    async def get_vector_store(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17:
        """
        Get a vector store by ID.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_stores.get_vector_store(
                vector_store_id="vector_store_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vector_store(
            vector_store_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    async def add_items(
        self,
        vector_store_id: str,
        *,
        request: typing.Sequence[VectorStoreItem],
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        vector_store_id : str

        request : typing.Sequence[VectorStoreItem]

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, VectorStoreItem

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_stores.add_items(
                vector_store_id="vector_store_id",
                request=[
                    VectorStoreItem(
                        document_id="document_id",
                        text="text",
                        embedding=[1.1],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_items(
            vector_store_id, request=request, context_id=context_id, request_options=request_options
        )
        return _response.data

    async def delete_vector_store(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a vector store by ID.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_stores.delete_vector_store(
                vector_store_id="vector_store_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_vector_store(
            vector_store_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    async def search_with_vector(
        self,
        vector_store_id: str,
        *,
        query_vector: typing.Sequence[float],
        context_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultVectorStoreSearchResult:
        """
        Search a vector store using either text or a vector.

        Parameters
        ----------
        vector_store_id : str

        query_vector : typing.Sequence[float]
            Vector to search for

        context_id : typing.Optional[str]

        limit : typing.Optional[int]
            Maximum number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultVectorStoreSearchResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_stores.search_with_vector(
                vector_store_id="vector_store_id",
                query_vector=[1.1],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_with_vector(
            vector_store_id,
            query_vector=query_vector,
            context_id=context_id,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def list_documents(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultVectorStoreDocument:
        """
        List all documents in a vector store.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultVectorStoreDocument
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_stores.list_documents(
                vector_store_id="vector_store_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_documents(
            vector_store_id, context_id=context_id, request_options=request_options
        )
        return _response.data

    async def delete_document(
        self,
        vector_store_id: str,
        document_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a document by ID.

        Parameters
        ----------
        vector_store_id : str

        document_id : str

        context_id : typing.Optional[str]

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vector_stores.delete_document(
                vector_store_id="vector_store_id",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_document(
            vector_store_id, document_id, context_id=context_id, request_options=request_options
        )
        return _response.data
