

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.execution_metadata_get_response import ExecutionMetadataGetResponse
from .raw_client import AsyncRawExecutionMetadataClient, RawExecutionMetadataClient


class ExecutionMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExecutionMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExecutionMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExecutionMetadataClient
        """
        return self._raw_client

    def get_execution_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExecutionMetadataGetResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecutionMetadataGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.execution_metadata.get_execution_metadata()
        """
        _response = self._raw_client.get_execution_metadata(request_options=request_options)
        return _response.data


class AsyncExecutionMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExecutionMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExecutionMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExecutionMetadataClient
        """
        return self._raw_client

    async def get_execution_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExecutionMetadataGetResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecutionMetadataGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.execution_metadata.get_execution_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_execution_metadata(request_options=request_options)
        return _response.data
