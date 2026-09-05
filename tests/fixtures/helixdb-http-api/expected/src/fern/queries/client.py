

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.query_request import QueryRequest
from ..types.query_response import QueryResponse
from .raw_client import AsyncRawQueriesClient, RawQueriesClient


OMIT = typing.cast(typing.Any, ...)


class QueriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueriesClient
        """
        return self._raw_client

    def execute_query(
        self,
        *,
        request: QueryRequest,
        helix_database_id: typing.Optional[str] = None,
        helix_warm: typing.Optional[bool] = None,
        helix_require_writer: typing.Optional[bool] = None,
        helix_await_durable: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[QueryResponse]:
        """
        Executes one read or write batch. request_type must match the closed read or write variant under query. Local servers accept request bodies up to 16 MiB. Helix Cloud gateways accept request bodies up to 2 MiB.

        Parameters
        ----------
        request : QueryRequest

        helix_database_id : typing.Optional[str]
            Database identifier shown in Helix Cloud connection details. Required by the GA shared gateway, not needed by a standalone local server, and not allowed by a database-specific cluster-mode gateway. The legacy X-Helix-Tenant-Id alias is also accepted in GA mode.

        helix_warm : typing.Optional[bool]
            Warm read execution state. Valid only for read requests.

        helix_require_writer : typing.Optional[bool]
            Reject the request unless it reaches a writer-capable server.

        helix_await_durable : typing.Optional[bool]
            Flush the writer before acknowledging success. Valid only for write requests.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[QueryResponse]
            Query executed successfully.

        Examples
        --------
        from fern import (
            Batch,
            BatchEntryQuery,
            FernApi,
            NamedQuery,
            QueryRequest_Read,
            ReadBatchQuery,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.queries.execute_query(
            request=QueryRequest_Read(
                query=ReadBatchQuery(
                    read=Batch(
                        entries=[
                            BatchEntryQuery(
                                query=NamedQuery(
                                    root={"key": "value"},
                                ),
                            )
                        ],
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.execute_query(
            request=request,
            helix_database_id=helix_database_id,
            helix_warm=helix_warm,
            helix_require_writer=helix_require_writer,
            helix_await_durable=helix_await_durable,
            request_options=request_options,
        )
        return _response.data


class AsyncQueriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueriesClient
        """
        return self._raw_client

    async def execute_query(
        self,
        *,
        request: QueryRequest,
        helix_database_id: typing.Optional[str] = None,
        helix_warm: typing.Optional[bool] = None,
        helix_require_writer: typing.Optional[bool] = None,
        helix_await_durable: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[QueryResponse]:
        """
        Executes one read or write batch. request_type must match the closed read or write variant under query. Local servers accept request bodies up to 16 MiB. Helix Cloud gateways accept request bodies up to 2 MiB.

        Parameters
        ----------
        request : QueryRequest

        helix_database_id : typing.Optional[str]
            Database identifier shown in Helix Cloud connection details. Required by the GA shared gateway, not needed by a standalone local server, and not allowed by a database-specific cluster-mode gateway. The legacy X-Helix-Tenant-Id alias is also accepted in GA mode.

        helix_warm : typing.Optional[bool]
            Warm read execution state. Valid only for read requests.

        helix_require_writer : typing.Optional[bool]
            Reject the request unless it reaches a writer-capable server.

        helix_await_durable : typing.Optional[bool]
            Flush the writer before acknowledging success. Valid only for write requests.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[QueryResponse]
            Query executed successfully.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Batch,
            BatchEntryQuery,
            NamedQuery,
            QueryRequest_Read,
            ReadBatchQuery,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.queries.execute_query(
                request=QueryRequest_Read(
                    query=ReadBatchQuery(
                        read=Batch(
                            entries=[
                                BatchEntryQuery(
                                    query=NamedQuery(
                                        root={"key": "value"},
                                    ),
                                )
                            ],
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_query(
            request=request,
            helix_database_id=helix_database_id,
            helix_warm=helix_warm,
            helix_require_writer=helix_require_writer,
            helix_await_durable=helix_await_durable,
            request_options=request_options,
        )
        return _response.data
