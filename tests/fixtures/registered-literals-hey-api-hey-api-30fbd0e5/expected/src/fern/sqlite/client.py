

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.result_set import ResultSet
from .raw_client import AsyncRawSqliteClient, RawSqliteClient
from .types.sqlite_batch_request_mode import SqliteBatchRequestMode
from .types.sqlite_batch_request_statements_item import SqliteBatchRequestStatementsItem
from .types.sqlite_execute_request_statement import SqliteExecuteRequestStatement


OMIT = typing.cast(typing.Any, ...)


class SqliteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSqliteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSqliteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSqliteClient
        """
        return self._raw_client

    def execute(
        self, *, statement: SqliteExecuteRequestStatement, request_options: typing.Optional[RequestOptions] = None
    ) -> ResultSet:
        """
        Execute a single SQLite statement and return results

        Parameters
        ----------
        statement : SqliteExecuteRequestStatement

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResultSet
            Result of executing an SQL statement.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sqlite.execute(
            statement="SELECT 1;",
        )
        """
        _response = self._raw_client.execute(statement=statement, request_options=request_options)
        return _response.data

    def batch(
        self,
        *,
        statements: typing.Sequence[SqliteBatchRequestStatementsItem],
        mode: typing.Optional[SqliteBatchRequestMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ResultSet]:
        """
        Execute a batch of SQLite statements and return results for all of them

        Parameters
        ----------
        statements : typing.Sequence[SqliteBatchRequestStatementsItem]

        mode : typing.Optional[SqliteBatchRequestMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ResultSet]
            Array of results from the statements executed

        Examples
        --------
        from fern.sqlite import SqliteBatchRequestMode

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sqlite.batch(
            statements=["SELECT 1;"],
            mode=SqliteBatchRequestMode.READ,
        )
        """
        _response = self._raw_client.batch(statements=statements, mode=mode, request_options=request_options)
        return _response.data


class AsyncSqliteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSqliteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSqliteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSqliteClient
        """
        return self._raw_client

    async def execute(
        self, *, statement: SqliteExecuteRequestStatement, request_options: typing.Optional[RequestOptions] = None
    ) -> ResultSet:
        """
        Execute a single SQLite statement and return results

        Parameters
        ----------
        statement : SqliteExecuteRequestStatement

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResultSet
            Result of executing an SQL statement.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sqlite.execute(
                statement="SELECT 1;",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute(statement=statement, request_options=request_options)
        return _response.data

    async def batch(
        self,
        *,
        statements: typing.Sequence[SqliteBatchRequestStatementsItem],
        mode: typing.Optional[SqliteBatchRequestMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ResultSet]:
        """
        Execute a batch of SQLite statements and return results for all of them

        Parameters
        ----------
        statements : typing.Sequence[SqliteBatchRequestStatementsItem]

        mode : typing.Optional[SqliteBatchRequestMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ResultSet]
            Array of results from the statements executed

        Examples
        --------
        import asyncio

        from fern.sqlite import SqliteBatchRequestMode

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sqlite.batch(
                statements=["SELECT 1;"],
                mode=SqliteBatchRequestMode.READ,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch(statements=statements, mode=mode, request_options=request_options)
        return _response.data
