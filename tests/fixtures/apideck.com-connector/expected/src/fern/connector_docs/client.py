

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawConnectorDocsClient, RawConnectorDocsClient


class ConnectorDocsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectorDocsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectorDocsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectorDocsClient
        """
        return self._raw_client

    def one(self, id: str, doc_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get Connector Doc content

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        doc_id : str
            ID of the Doc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Connectors

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connector_docs.one()
        """
        _response = self._raw_client.one(id, doc_id, request_options=request_options)
        return _response.data


class AsyncConnectorDocsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectorDocsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectorDocsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectorDocsClient
        """
        return self._raw_client

    async def one(self, id: str, doc_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get Connector Doc content

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        doc_id : str
            ID of the Doc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
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
            await client.connector_docs.one()


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, doc_id, request_options=request_options)
        return _response.data
