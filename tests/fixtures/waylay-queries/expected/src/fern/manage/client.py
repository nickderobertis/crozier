

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_response import DeleteResponse
from ..types.queries_list_response import QueriesListResponse
from ..types.query_input import QueryInput
from ..types.query_response import QueryResponse
from .raw_client import AsyncRawManageClient, RawManageClient
from .types.update_query_queries_v1query_query_name_put_request_body import (
    UpdateQueryQueriesV1QueryQueryNamePutRequestBody,
)


OMIT = typing.cast(typing.Any, ...)


class ManageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManageClient
        """
        return self._raw_client

    def list_queries(
        self,
        *,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueriesListResponse:
        """
        List named queries.

        Parameters
        ----------
        q : typing.Optional[str]
            The QDSL filter condition for the stored queries. Note that this value needs to be escaped when passed as an url paramater.

        limit : typing.Optional[int]
            Maximal number of items return in one response.

        offset : typing.Optional[int]
            Numbers of items to skip before listing results in the response page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueriesListResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.manage.list_queries(
            q="resource:APL4995",
        )
        """
        _response = self._raw_client.list_queries(q=q, limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def post_query(
        self,
        *,
        name: str,
        query: QueryInput,
        meta: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryResponse:
        """
        Create a new named query.

        Parameters
        ----------
        name : str
            Name of the stored query definition.

        query : QueryInput

        meta : typing.Optional[typing.Dict[str, typing.Any]]
            User metadata for the query definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, QueryInput

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.manage.post_query(
            name="name",
            query=QueryInput(),
        )
        """
        _response = self._raw_client.post_query(name=name, query=query, meta=meta, request_options=request_options)
        return _response.data

    def get_query(self, query_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> QueryResponse:
        """
        Get the definition of a named query.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.manage.get_query(
            query_name="query_name",
        )
        """
        _response = self._raw_client.get_query(query_name, request_options=request_options)
        return _response.data

    def update_query(
        self,
        query_name: str,
        *,
        request: UpdateQueryQueriesV1QueryQueryNamePutRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryResponse:
        """
        Create or update a named query definition.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request : UpdateQueryQueriesV1QueryQueryNamePutRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, QueryUpdateInput

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.manage.update_query(
            query_name="query_name",
            request=QueryUpdateInput(),
        )
        """
        _response = self._raw_client.update_query(query_name, request=request, request_options=request_options)
        return _response.data

    def remove_query(
        self, query_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteResponse:
        """
        Remove definition of a named query.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.manage.remove_query(
            query_name="query_name",
        )
        """
        _response = self._raw_client.remove_query(query_name, request_options=request_options)
        return _response.data


class AsyncManageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManageClient
        """
        return self._raw_client

    async def list_queries(
        self,
        *,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueriesListResponse:
        """
        List named queries.

        Parameters
        ----------
        q : typing.Optional[str]
            The QDSL filter condition for the stored queries. Note that this value needs to be escaped when passed as an url paramater.

        limit : typing.Optional[int]
            Maximal number of items return in one response.

        offset : typing.Optional[int]
            Numbers of items to skip before listing results in the response page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueriesListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.manage.list_queries(
                q="resource:APL4995",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_queries(
            q=q, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def post_query(
        self,
        *,
        name: str,
        query: QueryInput,
        meta: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryResponse:
        """
        Create a new named query.

        Parameters
        ----------
        name : str
            Name of the stored query definition.

        query : QueryInput

        meta : typing.Optional[typing.Dict[str, typing.Any]]
            User metadata for the query definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, QueryInput

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.manage.post_query(
                name="name",
                query=QueryInput(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_query(
            name=name, query=query, meta=meta, request_options=request_options
        )
        return _response.data

    async def get_query(
        self, query_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryResponse:
        """
        Get the definition of a named query.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.manage.get_query(
                query_name="query_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_query(query_name, request_options=request_options)
        return _response.data

    async def update_query(
        self,
        query_name: str,
        *,
        request: UpdateQueryQueriesV1QueryQueryNamePutRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryResponse:
        """
        Create or update a named query definition.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request : UpdateQueryQueriesV1QueryQueryNamePutRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, QueryUpdateInput

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.manage.update_query(
                query_name="query_name",
                request=QueryUpdateInput(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_query(query_name, request=request, request_options=request_options)
        return _response.data

    async def remove_query(
        self, query_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteResponse:
        """
        Remove definition of a named query.

        Parameters
        ----------
        query_name : str
            Name of the stored query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.manage.remove_query(
                query_name="query_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_query(query_name, request_options=request_options)
        return _response.data
