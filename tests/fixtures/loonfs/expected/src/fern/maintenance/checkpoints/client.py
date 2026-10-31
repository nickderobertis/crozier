

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.pagination import AsyncPager, SyncPager
from ...core.request_options import RequestOptions
from ...types.checkpoint import Checkpoint
from ...types.list_checkpoints_response import ListCheckpointsResponse
from .raw_client import AsyncRawCheckpointsClient, RawCheckpointsClient


class CheckpointsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCheckpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCheckpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCheckpointsClient
        """
        return self._raw_client

    def list(
        self,
        namespace_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[Checkpoint, ListCheckpointsResponse]:
        """
        Lists every pin, snapshots and fork pins, in checkpoint ID order. This is the inventory of what keeps manifests from garbage collection. An expired snapshot stays in the list until garbage collection deletes it, after its expiry plus the grace window. A cursor continues the listing against the current set of pins.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        limit : typing.Optional[int]
            The maximum page size.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Checkpoint, ListCheckpointsResponse]
            Existing checkpoint objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.maintenance.checkpoints.list(
            namespace_id="namespace_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(namespace_id, limit=limit, cursor=cursor, request_options=request_options)

    def retrieve(
        self, namespace_id: str, checkpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Checkpoint:
        """
        Returns one existing pin, as the checkpoint listing returns it, including an expired snapshot that garbage collection hasn't deleted. A missing ID returns `snapshot_not_found`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        checkpoint_id : str
            The checkpoint ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Checkpoint
            Existing checkpoint

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.maintenance.checkpoints.retrieve(
            namespace_id="namespace_id",
            checkpoint_id="checkpoint_id",
        )
        """
        _response = self._raw_client.retrieve(namespace_id, checkpoint_id, request_options=request_options)
        return _response.data


class AsyncCheckpointsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCheckpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCheckpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCheckpointsClient
        """
        return self._raw_client

    async def list(
        self,
        namespace_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[Checkpoint, ListCheckpointsResponse]:
        """
        Lists every pin, snapshots and fork pins, in checkpoint ID order. This is the inventory of what keeps manifests from garbage collection. An expired snapshot stays in the list until garbage collection deletes it, after its expiry plus the grace window. A cursor continues the listing against the current set of pins.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        limit : typing.Optional[int]
            The maximum page size.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Checkpoint, ListCheckpointsResponse]
            Existing checkpoint objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.maintenance.checkpoints.list(
                namespace_id="namespace_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(namespace_id, limit=limit, cursor=cursor, request_options=request_options)

    async def retrieve(
        self, namespace_id: str, checkpoint_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Checkpoint:
        """
        Returns one existing pin, as the checkpoint listing returns it, including an expired snapshot that garbage collection hasn't deleted. A missing ID returns `snapshot_not_found`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        checkpoint_id : str
            The checkpoint ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Checkpoint
            Existing checkpoint

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.maintenance.checkpoints.retrieve(
                namespace_id="namespace_id",
                checkpoint_id="checkpoint_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(namespace_id, checkpoint_id, request_options=request_options)
        return _response.data
