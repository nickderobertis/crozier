

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDatabasesClient, RawDatabasesClient


class DatabasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatabasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatabasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatabasesClient
        """
        return self._raw_client

    def retrieve_a_database(
        self, database_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieves a database object using the ID specified. Returns database metadata including the list of data source IDs contained in the database.

        Parameters
        ----------
        database_id : str
            Identifier for a Notion database

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )
        client.databases.retrieve_a_database(
            database_id="database_id",
        )
        """
        _response = self._raw_client.retrieve_a_database(database_id, request_options=request_options)
        return _response.data


class AsyncDatabasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatabasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatabasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatabasesClient
        """
        return self._raw_client

    async def retrieve_a_database(
        self, database_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieves a database object using the ID specified. Returns database metadata including the list of data source IDs contained in the database.

        Parameters
        ----------
        database_id : str
            Identifier for a Notion database

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            notion_version="YOUR_NOTION_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.databases.retrieve_a_database(
                database_id="database_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_database(database_id, request_options=request_options)
        return _response.data
