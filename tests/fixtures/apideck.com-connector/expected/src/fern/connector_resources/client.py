

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_connector_resource_response import GetConnectorResourceResponse
from ..types.unified_api_id import UnifiedApiId
from .raw_client import AsyncRawConnectorResourcesClient, RawConnectorResourcesClient


class ConnectorResourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectorResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectorResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectorResourcesClient
        """
        return self._raw_client

    def one(
        self,
        id: str,
        resource_id: str,
        *,
        unified_api: typing.Optional[UnifiedApiId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectorResourceResponse:
        """
        Get Connector Resource

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        resource_id : str
            ID of the resource you are acting upon.

        unified_api : typing.Optional[UnifiedApiId]
            Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectorResourceResponse
            ConnectorResources

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connector_resources.one(
            id="id",
            resource_id="resource_id",
        )
        """
        _response = self._raw_client.one(id, resource_id, unified_api=unified_api, request_options=request_options)
        return _response.data


class AsyncConnectorResourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectorResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectorResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectorResourcesClient
        """
        return self._raw_client

    async def one(
        self,
        id: str,
        resource_id: str,
        *,
        unified_api: typing.Optional[UnifiedApiId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectorResourceResponse:
        """
        Get Connector Resource

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        resource_id : str
            ID of the resource you are acting upon.

        unified_api : typing.Optional[UnifiedApiId]
            Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectorResourceResponse
            ConnectorResources

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connector_resources.one(
                id="id",
                resource_id="resource_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(
            id, resource_id, unified_api=unified_api, request_options=request_options
        )
        return _response.data
