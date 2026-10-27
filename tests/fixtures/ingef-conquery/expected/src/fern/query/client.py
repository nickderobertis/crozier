

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dataset_id import DatasetId
from ..types.execution_id import ExecutionId
from ..types.full_execution_status import FullExecutionStatus
from ..types.query import Query
from ..types.query_status import QueryStatus
from .raw_client import AsyncRawQueryClient, RawQueryClient


OMIT = typing.cast(typing.Any, ...)


class QueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueryClient
        """
        return self._raw_client

    def list_queries(
        self, dataset: DatasetId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[QueryStatus]:
        """
        Parameters
        ----------
        dataset : DatasetId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[QueryStatus]
            The Status and Metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.query.list_queries(
            dataset="dataset",
        )
        """
        _response = self._raw_client.list_queries(dataset, request_options=request_options)
        return _response.data

    def post_query(
        self, dataset: DatasetId, *, request: Query, request_options: typing.Optional[RequestOptions] = None
    ) -> FullExecutionStatus:
        """
        Parameters
        ----------
        dataset : DatasetId

        request : Query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FullExecutionStatus
            Status of the submitted query.

        Examples
        --------
        from fern import ConceptQueryType, FernApi, Query_ConceptQuery

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.query.post_query(
            dataset="dataset",
            request=Query_ConceptQuery(
                type=ConceptQueryType.CONCEPT_QUERY,
            ),
        )
        """
        _response = self._raw_client.post_query(dataset, request=request, request_options=request_options)
        return _response.data

    def get_query_status(
        self, query: ExecutionId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FullExecutionStatus:
        """
        Parameters
        ----------
        query : ExecutionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FullExecutionStatus
            The Status and Metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.query.get_query_status(
            query="query",
        )
        """
        _response = self._raw_client.get_query_status(query, request_options=request_options)
        return _response.data

    def delete_query(self, query: ExecutionId, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        query : ExecutionId

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
        )
        client.query.delete_query(
            query="query",
        )
        """
        _response = self._raw_client.delete_query(query, request_options=request_options)
        return _response.data

    def patch_query(
        self, query: ExecutionId, *, request: Query, request_options: typing.Optional[RequestOptions] = None
    ) -> FullExecutionStatus:
        """
        Parameters
        ----------
        query : ExecutionId

        request : Query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FullExecutionStatus
            Description of the updated execution

        Examples
        --------
        from fern import ConceptQueryType, FernApi, Query_ConceptQuery

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.query.patch_query(
            query="query",
            request=Query_ConceptQuery(
                type=ConceptQueryType.CONCEPT_QUERY,
            ),
        )
        """
        _response = self._raw_client.patch_query(query, request=request, request_options=request_options)
        return _response.data

    def cancel_query(self, query: ExecutionId, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        query : ExecutionId

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
        )
        client.query.cancel_query(
            query="query",
        )
        """
        _response = self._raw_client.cancel_query(query, request_options=request_options)
        return _response.data

    def reexecute_query(
        self, query: ExecutionId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FullExecutionStatus:
        """
        Parameters
        ----------
        query : ExecutionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FullExecutionStatus
            Description of restarted Query.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.query.reexecute_query(
            query="query",
        )
        """
        _response = self._raw_client.reexecute_query(query, request_options=request_options)
        return _response.data


class AsyncQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueryClient
        """
        return self._raw_client

    async def list_queries(
        self, dataset: DatasetId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[QueryStatus]:
        """
        Parameters
        ----------
        dataset : DatasetId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[QueryStatus]
            The Status and Metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.query.list_queries(
                dataset="dataset",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_queries(dataset, request_options=request_options)
        return _response.data

    async def post_query(
        self, dataset: DatasetId, *, request: Query, request_options: typing.Optional[RequestOptions] = None
    ) -> FullExecutionStatus:
        """
        Parameters
        ----------
        dataset : DatasetId

        request : Query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FullExecutionStatus
            Status of the submitted query.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConceptQueryType, Query_ConceptQuery

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.query.post_query(
                dataset="dataset",
                request=Query_ConceptQuery(
                    type=ConceptQueryType.CONCEPT_QUERY,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_query(dataset, request=request, request_options=request_options)
        return _response.data

    async def get_query_status(
        self, query: ExecutionId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FullExecutionStatus:
        """
        Parameters
        ----------
        query : ExecutionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FullExecutionStatus
            The Status and Metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.query.get_query_status(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_query_status(query, request_options=request_options)
        return _response.data

    async def delete_query(
        self, query: ExecutionId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        query : ExecutionId

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
        )


        async def main() -> None:
            await client.query.delete_query(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_query(query, request_options=request_options)
        return _response.data

    async def patch_query(
        self, query: ExecutionId, *, request: Query, request_options: typing.Optional[RequestOptions] = None
    ) -> FullExecutionStatus:
        """
        Parameters
        ----------
        query : ExecutionId

        request : Query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FullExecutionStatus
            Description of the updated execution

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConceptQueryType, Query_ConceptQuery

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.query.patch_query(
                query="query",
                request=Query_ConceptQuery(
                    type=ConceptQueryType.CONCEPT_QUERY,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_query(query, request=request, request_options=request_options)
        return _response.data

    async def cancel_query(
        self, query: ExecutionId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        query : ExecutionId

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
        )


        async def main() -> None:
            await client.query.cancel_query(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_query(query, request_options=request_options)
        return _response.data

    async def reexecute_query(
        self, query: ExecutionId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FullExecutionStatus:
        """
        Parameters
        ----------
        query : ExecutionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FullExecutionStatus
            Description of restarted Query.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.query.reexecute_query(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reexecute_query(query, request_options=request_options)
        return _response.data
