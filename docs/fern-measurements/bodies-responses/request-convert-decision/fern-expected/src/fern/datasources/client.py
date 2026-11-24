

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.datasource_query import DatasourceQuery
from ..types.datasource_tags import DatasourceTags
from .raw_client import AsyncRawDatasourcesClient, RawDatasourcesClient


OMIT = typing.cast(typing.Any, ...)


class DatasourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatasourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatasourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatasourcesClient
        """
        return self._raw_client

    def query_datasource(
        self, *, request: DatasourceQuery, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : DatasourceQuery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.datasources.query_datasource(
            request={},
        )
        """
        _response = self._raw_client.query_datasource(request=request, request_options=request_options)
        return _response.data

    def tag_datasource(
        self, *, request: DatasourceTags, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : DatasourceTags

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.datasources.tag_datasource(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.tag_datasource(request=request, request_options=request_options)
        return _response.data


class AsyncDatasourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatasourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatasourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatasourcesClient
        """
        return self._raw_client

    async def query_datasource(
        self, *, request: DatasourceQuery, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : DatasourceQuery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.datasources.query_datasource(
                request={},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query_datasource(request=request, request_options=request_options)
        return _response.data

    async def tag_datasource(
        self, *, request: DatasourceTags, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : DatasourceTags

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.datasources.tag_datasource(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tag_datasource(request=request, request_options=request_options)
        return _response.data
