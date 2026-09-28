

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawClusterClient, RawClusterClient
from .types.get_mockserver_cluster_response import GetMockserverClusterResponse


class ClusterClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClusterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClusterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClusterClient
        """
        return self._raw_client

    def retrieve_cluster_membership_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverClusterResponse:
        """
        Reports whether this instance is running clustered, its node id, whether it is the coordinator, and the current member list. `clusterName` is omitted entirely when the instance is not clustered.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverClusterResponse
            cluster status returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.cluster.retrieve_cluster_membership_status()
        """
        _response = self._raw_client.retrieve_cluster_membership_status(request_options=request_options)
        return _response.data


class AsyncClusterClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClusterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClusterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClusterClient
        """
        return self._raw_client

    async def retrieve_cluster_membership_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverClusterResponse:
        """
        Reports whether this instance is running clustered, its node id, whether it is the coordinator, and the current member list. `clusterName` is omitted entirely when the instance is not clustered.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverClusterResponse
            cluster status returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.cluster.retrieve_cluster_membership_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_cluster_membership_status(request_options=request_options)
        return _response.data
