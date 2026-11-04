

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.worker_out import WorkerOut
from .raw_client import AsyncRawWorkersClient, RawWorkersClient


class WorkersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkersClient
        """
        return self._raw_client

    def list_workers(
        self, *, cluster_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WorkerOut]:
        """
        Parameters
        ----------
        cluster_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkerOut]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workers.list_workers()
        """
        _response = self._raw_client.list_workers(cluster_id=cluster_id, request_options=request_options)
        return _response.data

    def delete_worker(self, worker_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        worker_id : str

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
        client.workers.delete_worker(
            worker_id="worker_id",
        )
        """
        _response = self._raw_client.delete_worker(worker_id, request_options=request_options)
        return _response.data


class AsyncWorkersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkersClient
        """
        return self._raw_client

    async def list_workers(
        self, *, cluster_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WorkerOut]:
        """
        Parameters
        ----------
        cluster_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkerOut]
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
            await client.workers.list_workers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_workers(cluster_id=cluster_id, request_options=request_options)
        return _response.data

    async def delete_worker(self, worker_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        worker_id : str

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
            await client.workers.delete_worker(
                worker_id="worker_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_worker(worker_id, request_options=request_options)
        return _response.data
