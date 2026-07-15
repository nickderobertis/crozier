

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connectors_filter import ConnectorsFilter
from ..types.get_connector_response import GetConnectorResponse
from ..types.get_connectors_response import GetConnectorsResponse
from .raw_client import AsyncRawConnectorsClient, RawConnectorsClient


class ConnectorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectorsClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ConnectorsFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectorsResponse:
        """
        List Connectors

        Parameters
        ----------
        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ConnectorsFilter]
            Apply filters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectorsResponse
            Connectors

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connectors.all_()
        """
        _response = self._raw_client.all_(cursor=cursor, limit=limit, filter=filter, request_options=request_options)
        return _response.data

    def one(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetConnectorResponse:
        """
        Get Connector

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectorResponse
            Connectors

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connectors.one(
            id="id",
        )
        """
        _response = self._raw_client.one(id, request_options=request_options)
        return _response.data


class AsyncConnectorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectorsClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ConnectorsFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectorsResponse:
        """
        List Connectors

        Parameters
        ----------
        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ConnectorsFilter]
            Apply filters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectorsResponse
            Connectors

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connectors.all_()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            cursor=cursor, limit=limit, filter=filter, request_options=request_options
        )
        return _response.data

    async def one(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetConnectorResponse:
        """
        Get Connector

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectorResponse
            Connectors

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connectors.one(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, request_options=request_options)
        return _response.data
