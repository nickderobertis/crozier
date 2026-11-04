

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cluster_out import ClusterOut
from .raw_client import AsyncRawClustersClient, RawClustersClient


OMIT = typing.cast(typing.Any, ...)


class ClustersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClustersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClustersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClustersClient
        """
        return self._raw_client

    def list_clusters(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ClusterOut]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ClusterOut]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.clusters.list_clusters()
        """
        _response = self._raw_client.list_clusters(request_options=request_options)
        return _response.data

    def create_cluster(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterOut:
        """
        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClusterOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.clusters.create_cluster(
            name="name",
        )
        """
        _response = self._raw_client.create_cluster(name=name, description=description, request_options=request_options)
        return _response.data

    def delete_cluster(self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        cluster_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.clusters.delete_cluster(
            cluster_id="cluster_id",
        )
        """
        _response = self._raw_client.delete_cluster(cluster_id, request_options=request_options)
        return _response.data


class AsyncClustersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClustersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClustersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClustersClient
        """
        return self._raw_client

    async def list_clusters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ClusterOut]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ClusterOut]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.clusters.list_clusters()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_clusters(request_options=request_options)
        return _response.data

    async def create_cluster(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterOut:
        """
        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClusterOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.clusters.create_cluster(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_cluster(
            name=name, description=description, request_options=request_options
        )
        return _response.data

    async def delete_cluster(self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        cluster_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.clusters.delete_cluster(
                cluster_id="cluster_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_cluster(cluster_id, request_options=request_options)
        return _response.data
