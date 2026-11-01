

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.operation_list import OperationList
from .raw_client import AsyncRawOperationsClient, RawOperationsClient


class OperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOperationsClient
        """
        return self._raw_client

    def list(self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None) -> OperationList:
        """
        This method gets all the operations.

        Parameters
        ----------
        api_version : str
            The API Version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationList
            The supported operations list.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.operations.list(
            api_version="api-version",
        )
        """
        _response = self._raw_client.list(api_version=api_version, request_options=request_options)
        return _response.data


class AsyncOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOperationsClient
        """
        return self._raw_client

    async def list(self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None) -> OperationList:
        """
        This method gets all the operations.

        Parameters
        ----------
        api_version : str
            The API Version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OperationList
            The supported operations list.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.operations.list(
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(api_version=api_version, request_options=request_options)
        return _response.data
