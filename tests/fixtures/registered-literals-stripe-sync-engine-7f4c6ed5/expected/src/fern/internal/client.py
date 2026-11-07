

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawInternalClient, RawInternalClient
from .types.internal_query_response import InternalQueryResponse


OMIT = typing.cast(typing.Any, ...)


class InternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalClient
        """
        return self._raw_client

    def query(
        self,
        *,
        sql: str,
        connection_string: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalQueryResponse:
        """
        Parameters
        ----------
        sql : str

        connection_string : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalQueryResponse
            Query results

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.query(
            sql="sql",
        )
        """
        _response = self._raw_client.query(
            sql=sql, connection_string=connection_string, url=url, request_options=request_options
        )
        return _response.data


class AsyncInternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalClient
        """
        return self._raw_client

    async def query(
        self,
        *,
        sql: str,
        connection_string: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalQueryResponse:
        """
        Parameters
        ----------
        sql : str

        connection_string : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalQueryResponse
            Query results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.query(
                sql="sql",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query(
            sql=sql, connection_string=connection_string, url=url, request_options=request_options
        )
        return _response.data
