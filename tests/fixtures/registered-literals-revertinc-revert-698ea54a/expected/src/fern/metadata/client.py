

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.crm_metadata_response import CrmMetadataResponse
from .raw_client import AsyncRawMetadataClient, RawMetadataClient


class MetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetadataClient
        """
        return self._raw_client

    def getcrms(self, *, request_options: typing.Optional[RequestOptions] = None) -> CrmMetadataResponse:
        """
        Retrieve a list of CRMs available for this account from the database based on the public token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmMetadataResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.metadata.getcrms()
        """
        _response = self._raw_client.getcrms(request_options=request_options)
        return _response.data


class AsyncMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetadataClient
        """
        return self._raw_client

    async def getcrms(self, *, request_options: typing.Optional[RequestOptions] = None) -> CrmMetadataResponse:
        """
        Retrieve a list of CRMs available for this account from the database based on the public token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmMetadataResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.metadata.getcrms()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcrms(request_options=request_options)
        return _response.data
