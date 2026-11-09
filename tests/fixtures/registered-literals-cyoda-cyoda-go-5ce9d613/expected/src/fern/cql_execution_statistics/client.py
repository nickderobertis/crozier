

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.table_time_stats_dto import TableTimeStatsDto
from .raw_client import AsyncRawCqlExecutionStatisticsClient, RawCqlExecutionStatisticsClient


class CqlExecutionStatisticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCqlExecutionStatisticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCqlExecutionStatisticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCqlExecutionStatisticsClient
        """
        return self._raw_client

    def get_all(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[TableTimeStatsDto]:
        """
        Returns detailed execution statistics for all tracked tables, including per-operation breakdowns and minute-by-minute statistics.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TableTimeStatsDto]
            Full statistics for all tables

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cql_execution_statistics.get_all()
        """
        _response = self._raw_client.get_all(request_options=request_options)
        return _response.data

    def get_all_brief(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TableTimeStatsDto]:
        """
        Returns summary execution statistics for all tracked tables without per-operation or minute-level details.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TableTimeStatsDto]
            Brief statistics for all tables

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cql_execution_statistics.get_all_brief()
        """
        _response = self._raw_client.get_all_brief(request_options=request_options)
        return _response.data

    def clear(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Clears all accumulated CQL execution statistics for all tables. This operation cannot be undone.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cql_execution_statistics.clear()
        """
        _response = self._raw_client.clear(request_options=request_options)
        return _response.data

    def get_table(self, table: str, *, request_options: typing.Optional[RequestOptions] = None) -> TableTimeStatsDto:
        """
        Returns detailed execution statistics for a specific Cassandra table, including timing distributions and operation breakdowns.

        Parameters
        ----------
        table : str
            Name of the Cassandra table, case sensitive, including quotes if needed

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TableTimeStatsDto
            Statistics for the specified table

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cql_execution_statistics.get_table(
            table="ENTITY_DATA",
        )
        """
        _response = self._raw_client.get_table(table, request_options=request_options)
        return _response.data

    def get_tables(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Returns a sorted list of all Cassandra table names that have execution statistics tracked.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of table names

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cql_execution_statistics.get_tables()
        """
        _response = self._raw_client.get_tables(request_options=request_options)
        return _response.data


class AsyncCqlExecutionStatisticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCqlExecutionStatisticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCqlExecutionStatisticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCqlExecutionStatisticsClient
        """
        return self._raw_client

    async def get_all(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TableTimeStatsDto]:
        """
        Returns detailed execution statistics for all tracked tables, including per-operation breakdowns and minute-by-minute statistics.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TableTimeStatsDto]
            Full statistics for all tables

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cql_execution_statistics.get_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all(request_options=request_options)
        return _response.data

    async def get_all_brief(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TableTimeStatsDto]:
        """
        Returns summary execution statistics for all tracked tables without per-operation or minute-level details.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TableTimeStatsDto]
            Brief statistics for all tables

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cql_execution_statistics.get_all_brief()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_brief(request_options=request_options)
        return _response.data

    async def clear(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Clears all accumulated CQL execution statistics for all tables. This operation cannot be undone.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cql_execution_statistics.clear()


        asyncio.run(main())
        """
        _response = await self._raw_client.clear(request_options=request_options)
        return _response.data

    async def get_table(
        self, table: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TableTimeStatsDto:
        """
        Returns detailed execution statistics for a specific Cassandra table, including timing distributions and operation breakdowns.

        Parameters
        ----------
        table : str
            Name of the Cassandra table, case sensitive, including quotes if needed

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TableTimeStatsDto
            Statistics for the specified table

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cql_execution_statistics.get_table(
                table="ENTITY_DATA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_table(table, request_options=request_options)
        return _response.data

    async def get_tables(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Returns a sorted list of all Cassandra table names that have execution statistics tracked.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of table names

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cql_execution_statistics.get_tables()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tables(request_options=request_options)
        return _response.data
