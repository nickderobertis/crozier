

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.container_response import ContainerResponse
from .raw_client import AsyncRawContainersClient, RawContainersClient


class ContainersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContainersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContainersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContainersClient
        """
        return self._raw_client

    def get_container(
        self, container_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContainerResponse:
        """
        Parameters
        ----------
        container_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContainerResponse
            Container metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.containers.get_container(
            container_id="container_id",
        )
        """
        _response = self._raw_client.get_container(container_id, request_options=request_options)
        return _response.data


class AsyncContainersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContainersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContainersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContainersClient
        """
        return self._raw_client

    async def get_container(
        self, container_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContainerResponse:
        """
        Parameters
        ----------
        container_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContainerResponse
            Container metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.containers.get_container(
                container_id="container_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_container(container_id, request_options=request_options)
        return _response.data
